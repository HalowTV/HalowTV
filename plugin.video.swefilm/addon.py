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
            'label': 'Popular movies',
            'path': plugin.url_for('movies', order='view', page='1')
        },
        {
            'label': 'Popular series',
            'path': plugin.url_for('series', order='view', page='1')
        },
        {
            'label': 'Latest updated movies',
            'path': plugin.url_for('movies', order='new', page='1')
        },
        {
            'label': 'Latest updated series',
            'path': plugin.url_for('series', order='new', page='1')
        },
        {
            'label': 'Genres',
            'path': plugin.url_for('genres')
        }
    ]

@plugin.route('/movies/<order>/<page>')
def movies(order, page='1'):
    page = int(page)
    movies = swefilm.list_movies(page, order)
    items = map(to_kodi_movie_item, movies)
    items.append({
        'label': 'next...',
        'path': plugin.url_for('movies', order=order, page=str(page + 1)),
        'is_playable': True
    })
    return items

@plugin.route('/series/<order>/<page>')
def series(order, page='1'):
    page = int(page)
    series = swefilm.list_series(page, order)
    items = map(to_kodi_serie_item, series)
    items.append({
        'label': 'next...',
        'path': plugin.url_for('series', order=order, page=str(page + 1))
    })
    return items

@plugin.route('/genres/')
def genres():
    def to_genre_item(item):
        return {
            'label': item,
            'path': plugin.url_for('genre', genre=item, page=1)
        }
    items = map(to_genre_item, swefilm.list_genres())
    return items

@plugin.route('/genre/<genre>/<page>/')
def genre(genre, page=1):
    page = int(page)
    genres = swefilm.list_genre(genre, page)
    items = map(to_kodi_item, genres)
    items.append({
        'label': 'next...',
        'path': plugin.url_for('genre', genre=genre, page=str(page + 1))
    })
    return items


@plugin.route('/play_movie/<url>/')
def play_movie(url):
    streams, subtitles = swefilm.get_movie_streams(url)
    print streams
    if len(streams) == 0:
        raise Exception("Failed to open stream")
    stream = quality_select_dialog(streams)
    plugin.set_resolved_url(stream, subtitles[0] if len(subtitles) else None)


@plugin.route('/play_episode/<url>/')
def play_episode(url):
    streams, subtitles = swefilm.get_movie_stream_from_player(url)
    if len(streams) == 0:
        raise Exception("Failed to open stream")
    stream = quality_select_dialog(streams)
    plugin.set_resolved_url(stream, subtitles[0] if len(subtitles) else None)

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
