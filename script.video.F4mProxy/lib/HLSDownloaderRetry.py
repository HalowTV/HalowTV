"""
Simple HTTP Live Streaming client.

References:
    http://tools.ietf.org/html/draft-pantos-http-live-streaming-08

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://sam.zoy.org/wtfpl/COPYING for more details.

Last updated: July 22, 2012
MODIFIED BY shani to make it work with F4mProxy
"""

import urlparse, urllib2, subprocess, os,traceback,cookielib,re,Queue,threading
import xml.etree.ElementTree as etree
import base64
from struct import unpack, pack
import struct
import sys
import io
import os
import time
import itertools
import xbmcaddon
import xbmc
import urllib2,urllib
import traceback
import urlparse
import posixpath
import re
import hmac
import hashlib
import binascii 
import zlib
from hashlib import sha256
import cookielib
import array, random, string
import requests
#from Crypto.Cipher import AES
'''
from crypto.cipher.aes      import AES
from crypto.cipher.cbc      import CBC
from crypto.cipher.base     import padWithPadLen
from crypto.cipher.rijndael import Rijndael
from crypto.cipher.aes_cbc import AES_CBC
'''
gproxy=None
gauth=None
try:
    from Crypto.Cipher import AES
    USEDec=1 ## 1==crypto 2==local, local pycrypto
except:
    print 'pycrypt not available using slow decryption'
    USEDec=3 ## 1==crypto 2==local, local pycrypto

if USEDec==1:
    #from Crypto.Cipher import AES
    print 'using pycrypto'
elif USEDec==2:
    from decrypter import AESDecrypter
    AES=AESDecrypter()
else:
    from f4mUtils import python_aes
#from decrypter import AESDecrypter

iv=None
key=None
value_unsafe = '%+&;#'
VALUE_SAFE = ''.join(chr(c) for c in range(33, 127)
    if chr(c) not in value_unsafe)
    
SUPPORTED_VERSION=3

cookieJar=cookielib.LWPCookieJar()
clientHeader=None
    
class HLSDownloaderRetry():
    global cookieJar
    """
    A downloader for f4m manifests or AdobeHDS.
    """

    def __init__(self):
        self.init_done=False

    def init(self, out_stream, url, proxy=None,use_proxy_for_chunks=True,g_stopEvent=None, maxbitrate=0, auth='', callbackpath="", callbackparam=""):
        global clientHeader,gproxy,gauth
        try:
            self.init_done=False
            self.init_url=url
            clientHeader=None
            self.status='init'
            self.proxy = proxy
            self.auth=auth
            self.callbackpath=callbackpath
            self.callbackparam=callbackparam
            if self.auth ==None or self.auth =='None'  or self.auth=='':
                self.auth=None
            if self.auth:
                gauth=self.auth
            
            if self.proxy and len(self.proxy)==0:
                self.proxy=None
            gproxy=self.proxy
            self.use_proxy_for_chunks=use_proxy_for_chunks
            self.out_stream=out_stream
            self.g_stopEvent=g_stopEvent
            self.maxbitrate=maxbitrate
            if '|' in url:
                sp = url.split('|')
                url = sp[0]
                clientHeader = sp[1]
                print clientHeader
                clientHeader= urlparse.parse_qsl(clientHeader)
                print 'header recieved now url and headers are',url, clientHeader 
            self.status='init done'
            self.url=url
            return self.preDownoload()
        except: 
            traceback.print_exc()
            self.status='finished'
        return False
        
    def preDownoload(self):
        
        print 'code here'
        return True
        
    def keep_sending_video(self,dest_stream, segmentToStart=None, totalSegmentToSend=0):
        try:
            self.status='download Starting'

            downloadInternal(self.url,dest_stream,self.maxbitrate,self.g_stopEvent , self.callbackpath,  self.callbackparam)
        except: 
            traceback.print_exc()
        self.status='finished'

        
def getUrl(url,timeout=15,returnres=False,stream =False):
    global cookieJar
    global clientHeader
    try:
        post=None
        #print 'url',url
        session = requests.Session()
        session.cookies = cookieJar

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:42.0) Gecko/20100101 Firefox/42.0 Iceweasel/42.0'}
        if clientHeader:
            for n,v in clientHeader:
                headers[n]=v
        proxies={}
        
        if gproxy:
            proxies= {"http": "http://"+gproxy}
        #import random
        #headers['User-Agent'] =headers['User-Agent'] + str(int(random.random()*100000))
        if post:
            req = session.post(url, headers = headers, data= post, proxies=proxies,verify=False,timeout=timeout,stream=stream)
        else:
            req = session.get(url, headers=headers,proxies=proxies,verify=False ,timeout=timeout,stream=stream)

        req.raise_for_status()
        if returnres: 
            return req
        else:
            return req.text

    except:
        print 'Error in getUrl'
        traceback.print_exc()
        raise 
        return None
        
    
def getUrlold(url,timeout=20, returnres=False):
    global cookieJar
    global clientHeader
    try:
        post=None
        #print 'url',url
        
        #openner = urllib2.build_opener(urllib2.HTTPHandler, urllib2.HTTPSHandler)
        cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
        openner = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
        
        #print cookieJar

        if post:
            req = urllib2.Request(url, post)
        else:
            req = urllib2.Request(url)
        
        ua_header=False
        if clientHeader:
            for n,v in clientHeader:
                req.add_header(n,v)
                if n=='User-Agent':
                    ua_header=True

        if not ua_header:
            req.add_header('User-Agent','AppleCoreMedia/1.0.0.12B411 (iPhone; U; CPU OS 8_1 like Mac OS X; en_gb)')
        
        #req.add_header('X-Playback-Session-Id','9A1E596D-6AB6-435F-85D1-59BDD0E62D24')
        if gproxy:
            req.set_proxy(gproxy, 'http')
        response = openner.open(req)
        
        if returnres: return response
        data=response.read()

        #print len(data)

        return data

    except:
        print 'Error in getUrl'
        traceback.print_exc()
        return None

def download_chunks(URL, chunk_size=4096, enc=None):
    #conn=urllib2.urlopen(URL)
    #print 'starting download'
    
    conn=getUrl(URL,returnres=True,stream=True)
    #while 1:
    chunk_size=chunk_size*100
    
    for chunk in conn.iter_content(chunk_size=chunk_size):
        yield chunk


def download_file(URL):
    return ''.join(download_chunks(URL))

def validate_m3u(conn):
    ''' make sure file is an m3u, and returns the encoding to use. '''
    return 'utf8'
    mime = conn.headers.get('Content-Type', '').split(';')[0].lower()
    if mime == 'application/vnd.apple.mpegurl':
        enc = 'utf8'
    elif mime == 'audio/mpegurl':
        enc = 'iso-8859-1'
    elif conn.url.endswith('.m3u8'):
        enc = 'utf8'
    elif conn.url.endswith('.m3u'):
        enc = 'iso-8859-1'
    else:
        raise Exception("Stream MIME type or file extension not recognized")
    if conn.readline().rstrip('\r\n') != '#EXTM3U':
        raise Exception("Stream is not in M3U format")
    return enc

def gen_m3u(url, skip_comments=True):
    global cookieJar

    conn = getUrl(url,returnres=True )#urllib2.urlopen(url)
    enc = validate_m3u(conn)
    #print conn
    for line in conn.iter_lines():#.split('\n'):
        line = line.rstrip('\r\n').decode(enc)
        if not line:
            # blank line
            continue
        elif line.startswith('#EXT'):
            # tag
            yield line
        elif line.startswith('#'):
            # comment
            if skip_comments:
                continue
            else:
                yield line
        else:
            # media file
            yield line

def parse_m3u_tag(line):
    if ':' not in line:
        return line, []
    tag, attribstr = line.split(':', 1)
    attribs = []
    last = 0
    quote = False
    for i,c in enumerate(attribstr+','):
        if c == '"':
            quote = not quote
        if quote:
            continue
        if c == ',':
            attribs.append(attribstr[last:i])
            last = i+1
    return tag, attribs

def parse_kv(attribs, known_keys=None):
    d = {}
    for item in attribs:
        k, v = item.split('=', 1)
        k=k.strip()
        v=v.strip().strip('"')
        if known_keys is not None and k not in known_keys:
            raise ValueError("unknown attribute %s"%k)
        d[k] = v
    return d

def handle_basic_m3u(url):
    global iv
    global key
    global USEDec
    global gauth
    seq = 1
    enc = None
    nextlen = 5
    duration = 5
    targetduration=5
    aesdone=False
    for line in gen_m3u(url):
        if line.startswith('#EXT'):
            tag, attribs = parse_m3u_tag(line)
            if tag == '#EXTINF':
                duration = float(attribs[0])
            elif tag == '#EXT-X-TARGETDURATION':
                assert len(attribs) == 1, "too many attribs in EXT-X-TARGETDURATION"
                targetduration = int(attribs[0])
                pass
            elif tag == '#EXT-X-MEDIA-SEQUENCE':
                assert len(attribs) == 1, "too many attribs in EXT-X-MEDIA-SEQUENCE"
                seq = int(attribs[0])
            elif tag == '#EXT-X-KEY':
                attribs = parse_kv(attribs, ('METHOD', 'URI', 'IV'))
                assert 'METHOD' in attribs, 'expected METHOD in EXT-X-KEY'
                if attribs['METHOD'] == 'NONE':
                    assert 'URI' not in attribs, 'EXT-X-KEY: METHOD=NONE, but URI found'
                    assert 'IV' not in attribs, 'EXT-X-KEY: METHOD=NONE, but IV found'
                    enc = None
                elif attribs['METHOD'] == 'AES-128':
                    if not aesdone:
                        aesdone=False
                        assert 'URI' in attribs, 'EXT-X-KEY: METHOD=AES-128, but no URI found'
                        #from Crypto.Cipher import AES
                        codeurl=attribs['URI'].strip('"')
                        if gauth:
                            codeurl=gauth
                        
                        #key = download_file(codeurl)
                        
                        if not codeurl.startswith('http'):
                            import urlparse
                            codeurl=urlparse.urljoin(url, codeurl)
                            
                        assert len(key) == 16, 'EXT-X-KEY: downloaded key file has bad length'
                        if 'IV' in attribs:
                            assert attribs['IV'].lower().startswith('0x'), 'EXT-X-KEY: IV attribute has bad format'
                            iv = attribs['IV'][2:].zfill(32).decode('hex')
                            assert len(iv) == 16, 'EXT-X-KEY: IV attribute has bad length'
                        else:
                            iv = '\0'*8 + struct.pack('>Q', seq)
                        enc=(codeurl,iv)
                        #if not USEDec==3:
                        #    enc = AES.new(key, AES.MODE_CBC, iv)
                        #else:
                        #    ivb=array.array('B',iv)
                        #    keyb= array.array('B',key)
                        #    enc=python_aes.new(keyb, 2, ivb)
                        #enc = AES_CBC(key)
                        #print key
                        #print iv
                        #enc=AESDecrypter.new(key, 2, iv)
                else:
                    assert False, 'EXT-X-KEY: METHOD=%s unknown'%attribs['METHOD']
            elif tag == '#EXT-X-PROGRAM-DATE-TIME':
                assert len(attribs) == 1, "too many attribs in EXT-X-PROGRAM-DATE-TIME"
                # TODO parse attribs[0] as ISO8601 date/time
                pass
            elif tag == '#EXT-X-ALLOW-CACHE':
                # XXX deliberately ignore
                pass
            elif tag == '#EXT-X-ENDLIST':
                assert not attribs
                yield None
                return
            elif tag == '#EXT-X-STREAM-INF':
                raise ValueError("don't know how to handle EXT-X-STREAM-INF in basic playlist")
            elif tag == '#EXT-X-DISCONTINUITY':
                assert not attribs
                print "[warn] discontinuity in stream"
            elif tag == '#EXT-X-VERSION':
                assert len(attribs) == 1
                if int(attribs[0]) > SUPPORTED_VERSION:
                    print "[warn] file version %s exceeds supported version %d; some things might be broken"%(attribs[0], SUPPORTED_VERSION)
            #else:
            #    raise ValueError("tag %s not known"%tag)
        else:
            yield (seq, enc, duration, targetduration, line)
            seq += 1

def player_pipe(queue, control,file):
    while 1:
        block = queue.get(block=True)
        if block is None: return
        file.write(block)
        file.flush()
        
def send_back(data,file):
    file.write(data)
    file.flush()
        
def downloadInternal(url,file,maxbitrate=0,stopEvent=None , callbackpath="",callbackparam=""):
    global key
    global iv
    global USEDec
    global cookieJar
    global clientHeader
    if stopEvent and stopEvent.isSet():
        return
    dumpfile = None
    #dumpfile=open('c:\\temp\\myfile.mp4',"wb")
    variants = []
    variant = None
    veryfirst=True
    #url check if requires redirect
    redirurl=url
    try:
        print 'going gor  ',url
        res=getUrl(url,returnres=True )
        print 'here ', res
        if res.history: 
            print 'history'
            redirurl=res.url
        res.close()
        
    except: traceback.print_exc()
    print 'redirurl',redirurl
    try:
        for line in gen_m3u(url):
            if line.startswith('#EXT'):
                tag, attribs = parse_m3u_tag(line)
                if tag == '#EXT-X-STREAM-INF':
                    variant = attribs
            elif variant:
                variants.append((line, variant))
                variant = None
        if len(variants) == 1:
            url = urlparse.urljoin(redirurl, variants[0][0])
        elif len(variants) >= 2:
            print "More than one variant of the stream was provided."

            choice=-1
            lastbitrate=0
            print 'maxbitrate',maxbitrate
            for i, (vurl, vattrs) in enumerate(variants):
                print i, vurl,
                for attr in vattrs:
                    key, value = attr.split('=')
                    key = key.strip()
                    value = value.strip().strip('"')
                    if key == 'BANDWIDTH':
                        print 'bitrate %.2f kbps'%(int(value)/1024.0)
                        if int(value)<=int(maxbitrate) and int(value)>lastbitrate:
                            choice=i
                            lastbitrate=int(value)
                    elif key == 'PROGRAM-ID':
                        print 'program %s'%value,
                    elif key == 'CODECS':
                        print 'codec %s'%value,
                    elif key == 'RESOLUTION':
                        print 'resolution %s'%value,
                    else:
                        print "unknown STREAM-INF attribute %s"%key
                        #raise ValueError("unknown STREAM-INF attribute %s"%key)
                print
            if choice==-1: choice=0
            #choice = int(raw_input("Selection? "))
            print 'choose %d'%choice
            url = urlparse.urljoin(redirurl, variants[choice][0])
    except: 
        
        raise

    

    last_seq = -1
    targetduration = 5
    changed = 0

    fails=0

    print 'inside HLS RETRY'
    try:
        while 1==1:#thread.isAlive():
            reconnect=False
            if fails>10: break
            if stopEvent and stopEvent.isSet():
                return
            try:
                medialist = list(handle_basic_m3u(url))
            except Exception as inst:
                print 'here in exp',inst
                print fails
                fails+=1
                
                if '403' in repr(inst).lower() and callbackpath and len(callbackpath)>0:
                    print 'callback'
                    import importlib, os
                    foldername=os.path.sep.join(callbackpath.split(os.path.sep)[:-1])
                    urlnew=''
                    if foldername not in sys.path:
                        sys.path.append(foldername)
                    try:
                        callbackfilename= callbackpath.split(os.path.sep)[-1].split('.')[0]
                        callbackmodule = importlib.import_module(callbackfilename)
                        urlnew,cjnew=callbackmodule.f4mcallback(callbackparam, 1, inst, cookieJar , url, clientHeader)
                    except: traceback.print_exc()
                    if urlnew and len(urlnew)>0 and urlnew.startswith('http'):
                        print 'got new url',url
                        url=urlnew
                        cookieJar= cjnew
                        continue
                    else: 
                        return
                        
                raise 

                    
            playedSomething=False
            if medialist==None: return

                ## choose to start playback three files from the end, since this is a live stream
                #medialist = medialist[-6:]
            #print 'medialist',medialist
            addsomewait=False
            for media in medialist:
                 
                if stopEvent and stopEvent.isSet():
                    return
                if media is None:
                    #queue.put(None, block=True)
                    return
                seq, encobj, duration, targetduration, media_url = media
                
                if seq > last_seq:
                    #print 'downloading.............',url
                    
                    enc=None
                    try:
                        data=None
                        try:
                            print 'downloading', urlparse.urljoin(url, media_url)
                            for chunk in download_chunks(urlparse.urljoin(url, media_url)):
                                if stopEvent and stopEvent.isSet():
                                    return
                                #print 'sending chunk', len(chunk)
                                send_back(chunk,file)
                            data="send"
                            addsomewait=True
                        except: traceback.print_exc()
                        if stopEvent and stopEvent.isSet():
                            return

                        if data and len(data)>0:# chunk in download_chunks(urlparse.urljoin(url, media_url),enc=encobj):

                            #if not veryfirst:
                            #    if dumpfile: dumpfile.write(chunk)
                            #    #queue.put(chunk, block=True)
                            #    send_back(data,file)
                            #    #print '3. chunk available %d'%len(chunk)
                            veryfirst=False
                            last_seq = seq
                            changed = 1
                            playedSomething=True
                            fails=0
                        else:
                            reconnect=True
                            fails+=1
                            break
                    except: pass
            
            '''if changed == 1:
                # initial minimum reload delay
                time.sleep(duration)
            elif changed == 0:
                # first attempt
                time.sleep(targetduration*0.5)
            elif changed == -1:
                # second attempt
                time.sleep(targetduration*1.5)
            else:
                # third attempt and beyond
                time.sleep(targetduration*3.0)
            
            changed -= 1
            '''
            
            if not playedSomething:
                xbmc.sleep(3000+ (3000 if addsomewait else 0))
            
    except:
        
        raise

    
