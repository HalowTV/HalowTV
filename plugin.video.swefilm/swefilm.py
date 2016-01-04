import utils
import urllib
import parsers

BASE_URL = 'http://swefilm.tv'
SERIES_URL = 'http://swefilm.tv/list/tvseries/?order=%s&page-%s'
MOVIES_URL = 'http://swefilm.tv/list/film/?order=%s&page-%s'
SEARCH_URL = 'http://swefilm.tv/search/%s'

GENRES = {
    'Action': 'http://swefilm.tv/genre/film-action/',
    'Adventure': 'http://swefilm.tv/genre/film-adventure/',
    'Animation': 'http://swefilm.tv/genre/film-animation/',
    'Biography': 'http://swefilm.tv/genre/film-biography/',
    'Comedy': 'http://swefilm.tv/genre/film-comedy/',
    'Crime': 'http://swefilm.tv/genre/film-crime/',
    'Documentary': 'http://swefilm.tv/genre/film-documentary/',
    'Drama': 'http://swefilm.tv/genre/film-drama/',
    'Family': 'http://swefilm.tv/genre/film-family/',
    'Fantasy': 'http://swefilm.tv/genre/film-fantasy/',
    'Game Show': 'http://swefilm.tv/genre/film-game-show/',
    'History': 'http://swefilm.tv/genre/film-history/',
    'Horror': 'http://swefilm.tv/genre/film-horror/',
    'Kids': 'http://swefilm.tv/genre/film-kids/',
    'Musical': 'http://swefilm.tv/genre/film-musical/',
    'Mystery': 'http://swefilm.tv/genre/film-mystery/',
    'News': 'http://swefilm.tv/genre/film-news/',
    'Romance': 'http://swefilm.tv/genre/film-romance/',
    'Sci-Fi': 'http://swefilm.tv/genre/film-sci-fi/',
    'Sport': 'http://swefilm.tv/genre/film-sport/',
    'Thriller': 'http://swefilm.tv/genre/film-thriller/',
    'War': 'http://swefilm.tv/genre/film-war/',
    'Western': 'http://swefilm.tv/genre/film-western/',
    'English Sub': 'http://swefilm.tv/genre/film-english-sub/',
    'Trailer': 'http://swefilm.tv/genre/film-trailer/'
}

def list_movies(page, order='view'):
    html = utils.fetch_html(MOVIES_URL % (order, page))
    return parsers.parse_movie_page(html)


def list_series(page, order='view'):
    html = utils.fetch_html(SERIES_URL % (order, page))
    return parsers.parse_movie_page(html)


def list_episodes(url):
    movie_html = utils.fetch_html(url)
    player_link =  parsers.get_player_link(movie_html)
    html = utils.fetch_html(player_link)
    return parsers.parse_episodes(html)


def list_genres():
    return GENRES.keys()


def list_genre(genre, page):
    url = GENRES[genre]
    url += '?page-%s' % page
    html = utils.fetch_html(url)
    return parsers.parse_movie_page(html)


def get_movie_streams(movie_url):
    movie_html = utils.fetch_html(movie_url)
    player_link =  parsers.get_player_link(movie_html)
    player_frame = utils.fetch_html(player_link)
    player_frame_src = parsers.get_player_iframe_src(player_frame)
    player_html = utils.fetch_html(player_frame_src)
    return parsers.parse_player(player_html)

def get_movie_stream_from_player(player_url):
    player_frame = utils.fetch_html(player_url)
    player_frame_src = parsers.get_player_iframe_src(player_frame)
    player_html = utils.fetch_html(player_frame_src)
    return parsers.parse_player(player_html)


def search(q):
    search_url = SEARCH_URL % urllib.quote_plus(q)
    html_result = utils.fetch_html(search_url)
    return parsers.parse_search(html_result)

if __name__ == '__main__':
    print list_movies()
