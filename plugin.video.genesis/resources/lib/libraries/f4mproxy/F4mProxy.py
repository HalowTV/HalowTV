"""
XBMCLocalProxy 0.1
Copyright 2011 Torben Gerkensmeyer
 
Modified for F4M format by Shani
 
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""
 
import base64
import re
import time
import urllib
import urllib2
import sys
import traceback
import socket
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from urllib import *
import urlparse
from f4mDownloader import F4MDownloader
from interalSimpleDownloader import interalSimpleDownloader
from hlsDownloader import HLSDownloader
import xbmc
import thread
import zlib
from StringIO import StringIO
import hmac
import hashlib
import base64
import threading 
import xbmcgui,xbmcplugin
import xbmc 
import hashlib
g_stopEvent=None
g_downloader=None

class MyHandler(BaseHTTPRequestHandler):
    """
   Serves a HEAD request
   """
    def do_HEAD(self):
        print "XBMCLocalProxy: Serving HEAD request..."
        self.send_response(200)
        rtype="flv-application/octet-stream"  #default type could have gone to the server to get it.
        #self.send_header("Accept-Ranges","bytes")
        self.end_headers() 
        #s.answer_request(False)
    """
   Serves a GET request.
   """
    def do_GET(s):
        print "XBMCLocalProxy: Serving GET request..."
        s.answer_request(True)
 
    def answer_request(self, sendData):
        global g_stopEvent
        global g_downloader
        try:

            #Pull apart request path
            request_path=self.path[1:]       
            request_path=re.sub(r"\?.*","",request_path)
            #If a request to stop is sent, shut down the proxy

            if request_path.lower()=="stop":# all special web interfaces here
                sys.exit()
                return
            if request_path.lower()=="favicon.ico":
                print 'dont have no icone here, may be in future'
                self.wfile.close()
                return


            (url,proxy,use_proxy_for_chunks,maxbitrate,simpledownloader, auth,streamtype)=self.decode_url(request_path)
            print 'simpledownloaderxxxxxxxxxxxxxxx',simpledownloader
            if streamtype=='' or streamtype==None or streamtype=='none': streamtype='HDS'
            
            if streamtype=='HDS':

                print 'Url received at proxy',url,proxy,use_proxy_for_chunks,maxbitrate


                #Send file request
                #self.handle_send_request(download_id,file_url, file_name, requested_range,download_mode ,keep_file,connections)
                
                downloader=None
                #downloader=g_downloader
                
                if not downloader or downloader.live==True or  not (downloader.init_done and downloader.init_url ==url):
                    downloader=F4MDownloader()
                    if not downloader.init(self.wfile,url,proxy,use_proxy_for_chunks,g_stopEvent,maxbitrate,auth):
                        print 'cannot init'
                        return
                    g_downloader=downloader
                    print 'init...' 
                
                enableSeek=False
                requested_range=self.headers.getheader("Range")
                if requested_range==None: requested_range=""
                srange, erange=(None,None)
                
                
                            
                if downloader.live==False and len(requested_range)>0 and not requested_range=="bytes=0-0": #we have to stream?
                    enableSeek=True
                    (srange, erange) = self.get_range_request(requested_range, downloader.total_frags)
                

                print 'PROXY DATA',downloader.live,enableSeek,requested_range,downloader.total_frags,srange, erange
                enableSeek=False ##disabled for time being, couldn't find better way to handle
                
                framgementToSend=0
                inflate=1815002#(6526684-466/3)#*373/downloader.total_frags# 4142*1024*243/8/40 #1#1024*1024
                if enableSeek:
                    #rtype="video/x-flv" #just as default
                    self.send_response(206)
                    rtype="flv-application/octet-stream"  #default type could have gone to the server to get it.
                    self.send_header("Content-Type", rtype)
                    self.send_header("Accept-Ranges","bytes")
                    print 'not LIVE,enable seek',downloader.total_frags
                    
                    totalsize=downloader.total_frags*inflate
                    
                    framgementToSend=1#downloader.total_frags
                    erange=srange+framgementToSend*inflate
                    if erange>=totalsize:
                        erange=totalsize-1
                    
    #                crange="bytes "+str(srange)+"-" +str(int(downloader.total_frags-1))+"/"+str(downloader.total_frags)#recalculate crange based on srange, portionLen and content_size 
    #                crange="bytes "+str(srange)+"-" +str(int(totalsize-1))+"/"+str(totalsize)#recalculate crange based on srange, portionLen and content_size 
                    crange="bytes "+str(srange)+"-" +str(int(erange))+"/*"#+str(totalsize)#recalculate crange based on srange, portionLen and content_size 
                    print srange/inflate,erange/inflate,totalsize/inflate
                    self.send_header("Content-Length", str(totalsize))
                    self.send_header("Content-Range",crange)
                    etag=self.generate_ETag(url)
                    self.send_header("ETag",etag)
                    print crange
                    self.send_header("Last-Modified","Wed, 21 Feb 2000 08:43:39 GMT")
                    self.send_header("Cache-Control","public, must-revalidate")
                    self.send_header("Cache-Control","no-cache")
                    self.send_header("Pragma","no-cache")
                    self.send_header("features","seekable,stridable")
                    self.send_header("client-id","12345")
                    self.send_header("Connection", 'close')
                else:
                    self.send_response(200)
                    rtype="flv-application/octet-stream"  #default type could have gone to the server to get it.
                    self.send_header("Content-Type", rtype)
                    srange=None
                    
            elif streamtype=='SIMPLE' or simpledownloader :
                downloader=interalSimpleDownloader();
                if not downloader.init(self.wfile,url,proxy,g_stopEvent,maxbitrate):
                    print 'cannot init'
                    return
                srange,framgementToSend=(None,None)
                self.send_response(200)
                rtype="flv-application/octet-stream"  #default type could have gone to the server to get it.
                self.send_header("Content-Type", rtype)
                srange=None
            elif streamtype=='HLS' or simpledownloader :
                downloader=HLSDownloader()
                if not downloader.init(self.wfile,url,proxy,use_proxy_for_chunks,g_stopEvent,maxbitrate,auth):
                    print 'cannot init'
                    return
                    
                srange,framgementToSend=(None,None)
                self.send_response(200)
                rtype="flv-application/octet-stream"  #default type could have gone to the server to get it.
                self.send_header("Content-Type", rtype)
                srange=None
            

            #rtype="flv-application/octet-stream"  #default type could have gone to the server to get it. 
            #self.send_header("Content-Type", rtype)    
               
            self.end_headers()
            if not srange==None:
                srange=srange/inflate
             
            if sendData:
                downloader.keep_sending_video(self.wfile,srange,framgementToSend)
                #runningthread=thread.start_new_thread(downloader.download,(self.wfile,url,proxy,use_proxy_for_chunks,))
                print 'srange,framgementToSend',srange,framgementToSend
                #runningthread=thread.start_new_thread(downloader.keep_sending_video,(self.wfile,srange,framgementToSend,))
                
                xbmc.sleep(500)
                while not downloader.status=="finished":
                    xbmc.sleep(200);


        except:
            #Print out a stack trace
            traceback.print_exc()
            g_stopEvent.set()
            self.send_response(404)
            #Close output stream file
            self.wfile.close()
            return

        #Close output stream file
        self.wfile.close()
        return 
   
    def generate_ETag(self, url):
        md=hashlib.md5()
        md.update(url)
        return md.hexdigest()
        
    def get_range_request(self, hrange, file_size):
        if hrange==None:
            srange=0
            erange=None
        else:
            try:
                #Get the byte value from the request string.
                hrange=str(hrange)
                splitRange=hrange.split("=")[1].split("-")
                srange=int(splitRange[0])
                erange = splitRange[1]
                if erange=="":
                    erange=int(file_size)-1
                #Build range string
                
            except:
                # Failure to build range string? Create a 0- range.
                srange=0
                erange=int(file_size-1);
        return (srange, erange)
        
    def decode_url(self, url):
        print 'in params'
        params=urlparse.parse_qs(url)
        print 'params',params # TODO read all params
        #({'url': url, 'downloadmode': downloadmode, 'keep_file':keep_file,'connections':connections})
        received_url = params['url'][0]#
        use_proxy_for_chunks =False
        proxy=None
        try:
            proxy = params['proxy'][0]#
            use_proxy_for_chunks =  params['use_proxy_for_chunks'][0]#
        except: pass
        
        maxbitrate=0
        try:
            maxbitrate = int(params['maxbitrate'][0])
        except: pass
        auth=None
        try:
            auth = params['auth'][0]
        except: pass

        if auth=='None' and auth=='':
            auth=None

        if proxy=='None' or proxy=='':
            proxy=None
        if use_proxy_for_chunks=='False':
            use_proxy_for_chunks=False
        simpledownloader=False
        try:
            simpledownloader =  params['simpledownloader'][0]#
            if simpledownloader.lower()=='true':
                print 'params[simpledownloader][0]',params['simpledownloader'][0]
                simpledownloader=True
            else:
                simpledownloader=False
        except: pass
        streamtype='HDS'
        try:
            streamtype =  params['streamtype'][0]#            
        except: pass 
        if streamtype=='None' and streamtype=='': streamtype='HDS'
        return (received_url,proxy,use_proxy_for_chunks,maxbitrate,simpledownloader,auth,streamtype)   
    """
   Sends the requested file and add additional headers.
   """

 
class Server(HTTPServer):
    """HTTPServer class with timeout."""
 
    def get_request(self):
        """Get the request and client address from the socket."""
        self.socket.settimeout(5.0)
        result = None
        while result is None:
            try:
                result = self.socket.accept()
            except socket.timeout:
                pass
        result[0].settimeout(1000)
        return result
 
class ThreadedHTTPServer(ThreadingMixIn, Server):
    """Handle requests in a separate thread."""
 
HOST_NAME = '127.0.0.1'
PORT_NUMBER = 55333

class f4mProxy():

    def start(self,stopEvent,port=PORT_NUMBER):
        global PORT_NUMBER
        global HOST_NAME
        global g_stopEvent
        print 'port',port,'HOST_NAME',HOST_NAME
        g_stopEvent = stopEvent
        socket.setdefaulttimeout(10)
        server_class = ThreadedHTTPServer
        #MyHandler.protocol_version = "HTTP/1.1"
        MyHandler.protocol_version = "HTTP/1.1"
        httpd = server_class((HOST_NAME, port), MyHandler)
        
        print "XBMCLocalProxy Starts - %s:%s" % (HOST_NAME, port)
        while(True and not stopEvent.isSet()):
            httpd.handle_request()
        httpd.server_close()
        print "XBMCLocalProxy Stops %s:%s" % (HOST_NAME, port)
    def prepare_url(self,url,proxy=None, use_proxy_for_chunks=True,port=PORT_NUMBER, maxbitrate=0,simpleDownloader=False,auth=None, streamtype='HDS'):
        global PORT_NUMBER
        global PORT_NUMBER
        newurl=urllib.urlencode({'url': url,'proxy':proxy,'use_proxy_for_chunks':use_proxy_for_chunks,'maxbitrate':maxbitrate,'simpledownloader':simpleDownloader,'auth':auth,'streamtype':streamtype})
        link = 'http://'+HOST_NAME+(':%s/'%str(port)) + newurl
        return (link) #make a url that caller then call load into player

class f4mProxyHelper():

    def playF4mLink(self,url,name,proxy=None,use_proxy_for_chunks=False, maxbitrate=0, simpleDownloader=False, auth=None, streamtype='HDS',setResolved=False):
        print "URL: " + url
        stopPlaying=threading.Event()
        progress = xbmcgui.DialogProgress()

        
        f4m_proxy=f4mProxy()
        stopPlaying.clear()
        runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
        progress.create('Starting local proxy')
        stream_delay = 1
        progress.update( 20, "", 'Loading local proxy', "" )
        xbmc.sleep(stream_delay*1000)
        progress.update( 100, "", 'Loading local proxy', "" )
        url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth, streamtype=streamtype)
        listitem = xbmcgui.ListItem(name,path=url_to_play)
        listitem.setInfo('video', {'Title': name})

        if setResolved:
            return url_to_play, listitem
        mplayer = MyPlayer()    
        mplayer.stopPlaying = stopPlaying
        progress.close() 
        mplayer.play(url_to_play,listitem)
       
        #xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, listitem)
        firstTime=True
        while True:
            if stopPlaying.isSet():
                break;
            #if not xbmc.Player().isPlaying():
            #    break
            xbmc.log('Sleeping...')
            xbmc.sleep(200)
            #if firstTime:
            #    xbmc.executebuiltin('Dialog.Close(all,True)')
            #    firstTime=False
        stopPlaying.isSet()

        print 'Job done'
        return
        
    def start_proxy(self,url,name,proxy=None,use_proxy_for_chunks=False, maxbitrate=0,simpleDownloader=False,auth=None,streamtype='HDS'):
        print "URL: " + url
        stopPlaying=threading.Event()
        f4m_proxy=f4mProxy()
        stopPlaying.clear()
        runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
        stream_delay = 1
        xbmc.sleep(stream_delay*1000)
        url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype)
        return url_to_play, stopPlaying



class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 


            