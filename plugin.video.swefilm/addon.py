from xbmcswift2 import Plugin, xbmc, xbmcgui
import swefilm
import utils

plugin = Plugin()
        
@plugin.route('/')
def index():
    return [
        {
            'label': 'Search',
            'path': plugin.url_for('search')
        },
        {
            'label': 'List movies',
            'path': plugin.url_for('movies', page='1')
        },
        {
            'label': 'List series',
            'path': plugin.url_for('series', page='1')
        }
    ]

@plugin.route('/movies/<page>')
def movies(page='1'):
    page = int(page)
    movies = swefilm.list_movies(page)
    items = map(to_kodi_movie_item, movies)
    items.append({
        'label': 'next...',
        'path': plugin.url_for('movies', page=str(page + 1)),
        'is_playable': True
    })
    return items

@plugin.route('/series/<page>')
def series(page='1'):
    page = int(page)
    series = swefilm.list_series(page)
    items = map(to_kodi_serie_item, series)
    items.append({
        'label': 'next...',
        'path': plugin.url_for('series', page=str(page + 1))
    })
    return items

@plugin.route('/play_movie/<url>/')
def play_movie(url):
    streams = swefilm.get_movie_streams(url)
    stream = quality_select_dialog(streams)
    plugin.set_resolved_url(stream)


@plugin.route('/play_episode/<url>/')
def play_episode(url):
    streams = swefilm.get_movie_stream_from_player(url)
    stream = quality_select_dialog(streams)
    plugin.set_resolved_url(stream)

@plugin.route('/search/')
def search():
    kb = xbmc.Keyboard('', 'Search', False)
    kb.doModal()
    if kb.isConfirmed():
        text = kb.getText()
    else:
        return
    items = swefilm.search(text)
    return map(to_kodi_item, items)

@plugin.route('/list_episodes/<url>/')
def list_episodes(url):
    print 'listing episodes'
    episodes = swefilm.list_episodes(url)
    print episodes
    def to_item(episode):
        [url, title] = episode
        print 'episode url: ', url
        return {
            'label': title,
            'path': plugin.url_for('play_episode', url=url),
            'is_playable': True
        }
    return map(to_item, episodes)

def quality_select_dialog(stream_urls):
    qualities = [s[0] for s in stream_urls]
    dialog = xbmcgui.Dialog()
    answer = 0
    if len(qualities) > 1:
        answer = dialog.select("Quality Select", qualities)
        if answer == -1:
            return
    url = stream_urls[answer][1].strip()
    return url


def to_kodi_serie_item(item):
    return {
        'label': utils.safe_decode(item.title),
        'path': plugin.url_for('list_episodes', url=item.player_url),
        'thumbnail': swefilm.BASE_URL + item.poster
    }

def to_kodi_movie_item(item):
    return {
        'label': utils.safe_decode(item.title),
        'path': plugin.url_for('play_movie', url=item.player_url),
        'thumbnail': swefilm.BASE_URL + item.poster,
        'is_playable': True
    }

def to_kodi_item(item):
    if 'Season' in item.title:
        return to_kodi_serie_item(item)
    return to_kodi_movie_item(item)


if __name__ == '__main__':
    plugin.run()
