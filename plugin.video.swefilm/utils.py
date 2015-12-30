import urllib2
import HTMLParser

def fetch_html(url):
    request = urllib2.Request(url, headers={
        'Accept' : '*/*',
        'Accept-Encoding': '*',
        'User-Agent': 'curl/7.43.0'
    })
    contents = urllib2.urlopen(request).read()
    return contents

def safe_decode(word):
    h = HTMLParser.HTMLParser()
    word = h.unescape(word)
    s = ''
    for letter in word:
        if ord(letter) > 127:
            s += '_'
        else:
            s += letter
    return s

