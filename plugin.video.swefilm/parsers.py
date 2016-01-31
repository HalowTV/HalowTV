import base64
import re
from collections import namedtuple

Movie = namedtuple('Movie', ['title', 'year', 'length', 'poster', 'resolution', 'player_url'])

def do_ntimes(fn, arg, count):
    res = arg
    for i in range(count):
        res = fn(res)
    return res

def parse_player(html):
    atob = re.search(r"atob\('(.*?)'\)", html)
    atob_count = html.count('atob(')
    if atob:
        base64_string = atob.group(1)
        content = do_ntimes(base64.b64decode, base64_string, atob_count) #base64.b64decode(base64_string)
        video_sources = extract_source_tags(content)
        subtitles = extract_subtitles(content)
        return video_sources, subtitles


def parse_movie_page(html):
    movie_list = re.search(r'<div class="m_list(.*?)</ul>', html, re.DOTALL)
    if movie_list:
        return extract_movie_items(movie_list.group())
    return []

def get_player_link(html):
    player_link = re.search(r'<a class="icons btn_watch_detail".*?href="(.*?)"', html)
    if player_link:
        return player_link.group(1)
    return ''

def get_player_iframe_src(html):
    iframe_match = re.search(r'<iframe.*?src="(http://player.swefilm.tv.*?)"', html);
    if iframe_match:
        return iframe_match.group(1)

    return None

def parse_search(html):
    return parse_movie_page(html)

def parse_episodes(html):
    result = []

    svep_match = re.search(r'<span class="svep">(.*?)</span>', html)
    if svep_match:
        inner_html = svep_match.group()
        episodes = re.findall(r'<a.*?href="(.*?)">(.*?)</a>', inner_html)
        for episode in episodes:
            [url, title] = episode
            result.append((url, title))
    return result

def extract_subtitles(html):
    subtitle_tags = re.findall(r'(<track.*?\/>)', html)
    if subtitle_tags:
        subtitles = []
        for subtitle_tag in subtitle_tags:
            match = re.search(r'src="(.*?)"', subtitle_tag)
            if match:
                return [match.group(1)]

        return None

def extract_source_tags(html):
    source_tags = re.findall(r'(<source.*?\/>)', html)
    if source_tags:
        streams = []
        for source_tag in source_tags:
            match = re.search(r'src=\'(.*?)\'.*?(label|data-res|res)="(.*?)"', source_tag)
            if match:
                streams.append((match.group(3), match.group(1)))

        return streams

def extract_movie_item(html):
    main_match = re.search(r'<a.*?href="(.*?)".*?src="(.*?)".*?</a>.*?<a href.*?>(.*?)<\/a>', html, re.DOTALL)
    [url, poster, title] = main_match.groups()
    detail_match = re.search(r'<span class="q">(.*?)</span><span class="y">(.*?)</span><span class="p">(.*?)</span>', html)
    [length, year, resolution] = detail_match.groups()
    return Movie(title=title, player_url=url,
                 year=year, length=length,
                 poster=poster, resolution=resolution)

    return [url, title, poster]

def extract_movie_items(html):
    items = re.findall(r'(<li>.*?</li>)', html, re.DOTALL)
    return map(extract_movie_item, items)

