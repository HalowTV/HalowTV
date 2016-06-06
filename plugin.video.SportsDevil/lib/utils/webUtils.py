# -*- coding: utf-8 -*-

import os
import re
import urllib
import urlparse
import requests
import cookielib
import socket
from HTMLParser import HTMLParser
from fileUtils import fileExists, setFileContent, getFileContent

#------------------------------------------------------------------------------
socket.setdefaulttimeout(30)

#use ipv4 only
origGetAddrInfo = socket.getaddrinfo

def getAddrInfoWrapper(host, port, family=0, socktype=0, proto=0, flags=0):
    return origGetAddrInfo(host, port, socket.AF_INET, socktype, proto, flags)

# replace the original socket.getaddrinfo by our version
socket.getaddrinfo = getAddrInfoWrapper
#------------------------------------------------------------------------------

'''
    REQUEST classes
'''

class BaseRequest(object):
    
    def __init__(self, cookie_file=None):
        self.cookie_file = cookie_file
        self.s = requests.Session()
        if fileExists(self.cookie_file):
            self.s.cookies = self.load_cookies_from_lwp(self.cookie_file)
        self.s.headers.update({'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36'})
        self.s.headers.update({'Accept-Language' : 'en-US,en;q=0.5'})
        self.url = ''
    
    def save_cookies_lwp(self, cookiejar, filename):
        lwp_cookiejar = cookielib.LWPCookieJar()
        for c in cookiejar:
            args = dict(vars(c).items())
            args['rest'] = args['_rest']
            del args['_rest']
            c = cookielib.Cookie(**args)
            lwp_cookiejar.set_cookie(c)
        lwp_cookiejar.save(filename, ignore_discard=True)

    def load_cookies_from_lwp(self, filename):
        lwp_cookiejar = cookielib.LWPCookieJar()
        lwp_cookiejar.load(filename, ignore_discard=True)
        return lwp_cookiejar
    
    def fixurl(self, url):
        #url is unicode (quoted or unquoted)
        try:
            #url is already quoted
            url = url.encode('ascii')
        except:
            #quote url if it is unicode
            parsed_link = urlparse.urlsplit(url)
            parsed_link = parsed_link._replace(netloc=parsed_link.netloc.encode('idna'),
                                               path=urllib.quote(parsed_link.path.encode('utf-8')),
                                               query=urllib.quote(parsed_link.query.encode('utf-8'),safe='+?=&'),
                                               fragment=urllib.quote(parsed_link.fragment.encode('utf-8')))
            url = parsed_link.geturl().encode('ascii')
        #url is str (quoted)
        return url

    def getSource(self, url, form_data, referer, xml=False, mobile=False):
        url = self.fixurl(url)

        if not referer:
            referer = url
        else:
            referer = self.fixurl(referer)
        
        headers = {'Referer': referer}
        if mobile:
            self.s.headers.update({'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13E238 Safari/601.1'})
            
        if xml:
            headers['X-Requested-With'] = 'XMLHttpRequest'
            
        if 'dinozap.info' in urlparse.urlsplit(url).netloc:
            headers['X-Forwarded-For'] = '178.162.222.111'
        if 'playerhd2.pw' in urlparse.urlsplit(url).netloc:
            headers['X-Forwarded-For'] = '178.162.222.121'
        if 'playerapp1.pw' in urlparse.urlsplit(url).netloc:
            headers['X-Forwarded-For'] = '178.162.222.122'
        
        if 'cndhlsstream.pw' in urlparse.urlsplit(url).netloc:
            del self.s.headers['Accept-Encoding']
        
        if form_data:
            #zo**tv
            if 'uagent' in form_data[0]:
                form_data[0] = ('uagent',self.s.headers['User-Agent'])

            r = self.s.post(url, headers=headers, data=form_data, timeout=20)
        else:
            try:
                r = self.s.get(url, headers=headers, timeout=20)
            except (requests.exceptions.MissingSchema):
                return 'pass'
        
        #many utf8 encodings are specified in HTTP body not headers and requests only checks headers, maybe use html5lib
        #https://github.com/kennethreitz/requests/issues/2086
        if 'streamlive.to' in urlparse.urlsplit(url).netloc \
        or 'sport365.live' in urlparse.urlsplit(url).netloc \
        or 'vipleague' in urlparse.urlsplit(url).netloc \
        or 'cinestrenostv.tv' in urlparse.urlsplit(url).netloc \
        or 'batmanstream.com' in urlparse.urlsplit(url).netloc \
        or 'sportcategory.com' in urlparse.urlsplit(url).netloc:
            r.encoding = 'utf-8'
        if 'lfootball.ws' in urlparse.urlsplit(url).netloc:
            r.encoding = 'windows-1251'
            
        response  = r.text
        if len(response) > 10:
            if self.cookie_file:
                self.save_cookies_lwp(self.s.cookies, self.cookie_file)

        return HTMLParser().unescape(response)


#------------------------------------------------------------------------------

class DemystifiedWebRequest(BaseRequest):

    def __init__(self, cookiePath):
        super(DemystifiedWebRequest,self).__init__(cookiePath)

    def getSource(self, url, form_data, referer='', xml=False, mobile=False, demystify=False):
        data = super(DemystifiedWebRequest, self).getSource(url, form_data, referer, xml, mobile)
        if not data:
            return None

        if not demystify:
            # remove comments
            r = re.compile('<!--.*?(?!//)--!*>', re.IGNORECASE + re.DOTALL + re.MULTILINE)
            m = r.findall(data)
            if m:
                for comment in m:
                    data = data.replace(comment,'')
        else:
            import decryptionUtils as crypt
            data = crypt.doDemystify(data)

        return data

#------------------------------------------------------------------------------

class CachedWebRequest(DemystifiedWebRequest):

    def __init__(self, cookiePath, cachePath):
        super(CachedWebRequest,self).__init__(cookiePath)
        self.cachePath = cachePath
        self.cachedSourcePath = os.path.join(self.cachePath, 'page.html')
        self.currentUrlPath = os.path.join(self.cachePath, 'currenturl')
        self.lastUrlPath = os.path.join(self.cachePath, 'lasturl')

    def __setLastUrl(self, url):
        setFileContent(self.lastUrlPath, url)

    def __getCachedSource(self):
        try:
            data = getFileContent(self.cachedSourcePath)
        except:
            pass
        return data

    def getLastUrl(self):
        return getFileContent(self.lastUrlPath)
        

    def getSource(self, url, form_data, referer='', xml=False, mobile=False, ignoreCache=False, demystify=False):
        if 'live.xml' in url:
            self.cachedSourcePath = url
            data = self.__getCachedSource()
            return data
            
        if url == self.getLastUrl() and not ignoreCache:
            data = self.__getCachedSource()
        else:
            data = super(CachedWebRequest,self).getSource(url, form_data, referer, xml, mobile, demystify)
            if data:
                # Cache url
                self.__setLastUrl(url)
                # Cache page
                setFileContent(self.cachedSourcePath, data)
        return data
