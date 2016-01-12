### ############################################################################################################
###	#	
### # Author: 			#		The Highway
### # Description: 	#		Common File For:  The Binary Highway
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
import os,sys,string,StringIO,logging,random,array,time,datetime,re
import urllib,urllib2,htmllib
from config import *
#import urlresolver
#import copy
#try: import json
#except ImportError: import simplejson as json
#try: import StorageServer
#except: import storageserverdummy as StorageServer
#cache = StorageServer.StorageServer(plugin_id)
try: 			from addon.common.net 					import Net
except:
	try: 		from t0mm0.common.net 					import Net
	except: 
		try: from c_t0mm0_common_net 					import Net
		except: pass
try: 			from addon.common.addon 				import Addon
except:
	try: 		from t0mm0.common.addon 				import Addon
	except: 
		try: from c_t0mm0_common_addon 				import Addon
		except: pass
#try: 		from sqlite3 										import dbapi2 as sqlite; print "Loading sqlite3 as DB engine"
#except: from pysqlite2 									import dbapi2 as sqlite; print "Loading pysqlite2 as DB engine"
#try: 		from script.module.metahandler 	import metahandlers
#except: from metahandler 								import metahandlers
#import c_Extract as extract #extract.all(lib,addonfolder,dp)
#import cHiddenDownloader as downloader #downloader.download(url,destfile,destpath,useResolver=True)

### ############################################################################################################
__plugin__=ps('__plugin__'); __authors__=ps('__authors__'); __credits__=ps('__credits__'); 
### ############################################################################################################
##### Addon / Plugin Basic Setup #####
_addon_id=ps('_addon_id'); _plugin_id=ps('_addon_id'); 
_addon=Addon(ps('_addon_id'), sys.argv); addon=_addon; 
_plugin=xbmcaddon.Addon(id=ps('_addon_id')); 
try:
	try: import StorageServer as StorageServer
	except: 
		try: import c_StorageServer as StorageServer
		except:
			try: import storageserverdummy as StorageServer
			except:
				try: import c_storageserverdummy as StorageServer
				except: pass
	cache=StorageServer.StorageServer(ps('_addon_id'))
except: pass
##### Paths #####
#_database_name=ps('_database_name')
#_database_file=os.path.join(xbmc.translatePath("special://database"),ps('_database_name')+'.db'); 
#DB=_database_file; 
_domain_url=ps('_domain_url'); _du=ps('_domain_url'); 
_addonPath	=xbmc.translatePath(_plugin.getAddonInfo('path'))
_artPath		=xbmc.translatePath(os.path.join(_addonPath,ps('_addon_path_art')))
_thumbArtPath=xbmc.translatePath(os.path.join(_addonPath,'thumbs'))
_datapath 	=xbmc.translatePath(_addon.get_profile()); 
_artIcon		=_addon.get_icon(); 
_artFanart	=_addon.get_fanart(); 
xbmcLogFile =xbmc.translatePath(os.path.join('special://logpath','xbmc.log'))
##### Important Functions with some dependencies #####
def dPath(s,fe=''): return xbmc.translatePath(os.path.join(_datapath,s+fe))
CookFile=dPath('StreamupCookie.txt'); 
def addstv(id,value=''): _addon.addon.setSetting(id=id,value=value) ## Save Settings
def addst(r,s=''): return _addon.get_setting(r)   ## Get Settings
def addpr(r,s=''): return _addon.queries.get(r,s) ## Get Params
def tfalse(r,d=False): ## Get True / False
	if   (r.lower()=='true' ) or (r.lower()=='t') or (r.lower()=='y') or (r.lower()=='1') or (r.lower()=='yes'): return True
	elif (r.lower()=='false') or (r.lower()=='f') or (r.lower()=='n') or (r.lower()=='0') or (r.lower()=='no'): return False
	else: return d
def tfalse_old(r,d=False): ## Get True / False
	if   (r.lower()=='true' ): return True
	elif (r.lower()=='false'): return False
	else: return d
def art(f,fe=''): return xbmc.translatePath(os.path.join(_artPath,f+fe)) ### for Making path+filename+ext data for Art Images. ###
def artp(f,fe='.png'): return art(f,fe)
def artj(f,fe='.jpg'): return art(f,fe)
def thumbart(f,fe=''): return xbmc.translatePath(os.path.join(_thumbArtPath,f+fe)) ### for Making path+filename+ext data for Art Images. ###
def thumbartp(f,fe='.png'): return thumbart(f,fe)
def thumbartj(f,fe='.jpg'): return thumbart(f,fe)
##### Settings #####
_setting={}; 
_setting['enableMeta']	=	_enableMeta			=tfalse(addst("enableMeta"))
_setting['debug-enable']=	_debugging			=tfalse(addst("debug-enable")); 
_setting['debug-show']	=	_shoDebugging		=tfalse(addst("debug-show"))
debugging=_debugging
##### Variables #####
_default_section_=ps('default_section'); 
net=Net(); 
BASE_URL=ps('_domain_url');

### ############################################################################################################
### ############################################################################################################
def eod(): _addon.end_of_directory()
def notification(header="", message="", sleep=5000 ): xbmc.executebuiltin( "XBMC.Notification(%s,%s,%i)" % ( header, message, sleep ) )
def myNote(header='',msg='',delay=5000,image='http://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/US_99_%281961%29.svg/40px-US_99_%281961%29.svg.png'): _addon.show_small_popup(title=header,msg=msg,delay=delay,image=image)
def cFL( t,c=ps('default_cFL_color')): return '[COLOR '+c+']'+t+'[/COLOR]' ### For Coloring Text ###
def cFL_(t,c=ps('default_cFL_color')): return '[COLOR '+c+']'+t[0:1]+'[/COLOR]'+t[1:] ### For Coloring Text (First Letter-Only) ###
def WhereAmI(t): ### for Writing Location Data to log file ###
	if (_debugging==True): print 'Where am I:  '+t
def deb(s,t): ### for Writing Debug Data to log file ###
	if (_debugging==True): print s+':  '+t
def debob(t): ### for Writing Debug Object to log file ###
	if (_debugging==True): print t
def nolines(t):
	it=t.splitlines(); t=''
	for L in it: t=t+L
	t=((t.replace("\r","")).replace("\n","").replace("\a",""))
	return t
def isPath(path): return os.path.exists(path)
def isFile(filename): return os.path.isfile(filename)
def getFileExtension(filename):
	ext_pos = filename.rfind('.')
	if ext_pos != -1: return filename[ext_pos+1:]
	else: return ''
def get_immediate_subdirectories(directory):
	return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
def findInSubdirectory(filename, subdirectory=''):
	if subdirectory: path = subdirectory
	else: path = _addonPath
	for root, _, names in os.walk(path):
		if filename in names: return os.path.join(root, filename)
	raise 'File not found'
def get_xbmc_os():
	try: xbmc_os = os.environ.get('OS')
	except: xbmc_os = "unknown"
	return xbmc_os
def get_xbmc_version():
	rev_re = re.compile('r(\d+)')
	try: xbmc_version = xbmc.getInfoLabel('System.BuildVersion')
	except: xbmc_version = 'Unknown'
	return xbmc_version
def get_xbmc_revision():
	rev_re = re.compile('r(\d+)')
	try: xbmc_version = xbmc.getInfoLabel('System.BuildVersion')
	except: xbmc_version = 'Unknown'
	try: xbmc_rev=int(rev_re.search(xbmc_version).group(1)); deb("addoncompat.py: XBMC Revision",xbmc_rev)
	except: xbmc_rev=0; deb("addoncompat.py: XBMC Revision not available - Version String",xbmc_version)
	return xbmc_rev
def _SaveFile(path,data):
	file=open(path,'w')
	file.write(data)
	file.close()
def _OpenFile(path):
	deb('File',path)
	if os.path.isfile(path): ## File found.
		deb('Found',path)
		file = open(path, 'r')
		contents=file.read()
		file.close()
		return contents
	else: return '' ## File not found.
def _CreateDirectory(dir_path):
	dir_path = dir_path.strip()
	if not os.path.exists(dir_path): os.makedirs(dir_path)
def _get_dir(mypath, dirname): #...creates sub-directories if they are not found.
	subpath = os.path.join(mypath, dirname)
	if not os.path.exists(subpath): os.makedirs(subpath)
	return subpath
def askSelection(option_list=[],txtHeader=''):
	if (option_list==[]): 
		debob('askSelection() >> option_list is empty')
		return None
	dialogSelect = xbmcgui.Dialog();
	index=dialogSelect.select(txtHeader, option_list)
	return index
def iFL(t): return '[I]'+t+'[/I]' ### For Italic Text ###
def bFL(t): return '[B]'+t+'[/B]' ### For Bold Text ###
def _FL(t,c,e=''): ### For Custom Text Tags ###
	if (e==''): d=''
	else: d=' '+e
	return '['+c.upper()+d+']'+t+'[/'+c.upper()+']'
def aSortMeth(sM,h=int(sys.argv[1])):
	xbmcplugin.addSortMethod(handle=h, sortMethod=sM)
def set_view(content='none',view_mode=50,do_sort=False):
	deb('content type: ',str(content))
	deb('view mode: ',str(view_mode))
	h=int(sys.argv[1])
	if (content is not 'none'): xbmcplugin.setContent(h, content)
	if (tfalse(addst("auto-view"))==True): xbmc.executebuiltin("Container.SetViewMode(%s)" % str(view_mode))
def showkeyboard(txtMessage="",txtHeader="",passwordField=False):
	if txtMessage=='None': txtMessage=''
	keyboard = xbmc.Keyboard(txtMessage, txtHeader, passwordField)#("text to show","header text", True="password field"/False="show text")
	keyboard.doModal()
	if keyboard.isConfirmed():
		return keyboard.getText()
	else:
		return False # return ''
def ParseDescription(plot): ## Cleans up the dumb number stuff thats ugly.
	if ("&amp;"  in plot):  plot=plot.replace('&amp;'  ,'&')#&amp;#x27;
	if ("&nbsp;" in plot):  plot=plot.replace('&nbsp;' ," ")
	if ("&rsquo;" in plot):  plot=plot.replace('&rsquo;' ,"'")
	if ("&#8211;" in plot): plot=plot.replace("&#8211;","-")
	if ('&#' in plot) and (';' in plot):
		if ("&#8211;" in plot): plot=plot.replace("&#8211;","-") #unknown
		if ("&#8216;" in plot): plot=plot.replace("&#8216;","'")
		if ("&#8217;" in plot): plot=plot.replace("&#8217;","'")
		if ("&#8220;" in plot): plot=plot.replace('&#8220;','"')
		if ("&#8221;" in plot): plot=plot.replace('&#8221;','"')
		if ("&#215;"  in plot): plot=plot.replace('&#215;' ,'x')
		if ("&#x27;"  in plot): plot=plot.replace('&#x27;' ,"'")
		if ("&#xF4;"  in plot): plot=plot.replace('&#xF4;' ,"o")
		if ("&#xb7;"  in plot): plot=plot.replace('&#xb7;' ,"-")
		if ("&#xFB;"  in plot): plot=plot.replace('&#xFB;' ,"u")
		if ("&#xE0;"  in plot): plot=plot.replace('&#xE0;' ,"a")
		if ("&#0421;" in plot): plot=plot.replace('&#0421;',"")
		if ("&#xE9;" in plot):  plot=plot.replace('&#xE9;' ,"e")
		if ("&#xE2;" in plot):  plot=plot.replace('&#xE2;' ,"a")
		if ("&#038;" in plot):  plot=plot.replace('&#038;' ,"&")
		#if (chr(239) in plot):  plot=plot.replace(chr(239) ,"'")
		#plot=plot.replace(chr('0x92'),"'")
		if ('&#' in plot) and (';' in plot):
			try:		matches=re.compile('&#(.+?);').findall(plot)
			except:	matches=''
			if (matches is not ''):
				for match in matches:
					if (match is not '') and (match is not ' ') and ("&#"+match+";" in plot):  
						try: plot=plot.replace("&#"+match+";" ,"")
						except: pass
		#if ("\xb7"  in plot):  plot=plot.replace('\xb7'   ,"-")
		#if ('&#' in plot) and (';' in plot): plot=unescape_(plot)
	for i in xrange(127,256):
		try: plot=plot.replace(chr(i),"")
		except: pass
	return plot
def unescape_(s):
	p = htmllib.HTMLParser(None)
	p.save_bgn()
	p.feed(s)
	return p.save_end()
def messupText(t,_html=False,_ende=False,_a=False,Slashes=False):
	if (_html==True): 
		try: t=HTMLParser.HTMLParser().unescape(t)
		except: t=t
		try: t=ParseDescription(t)
		except: t=t
	if (_ende==True): 
		try: 
			#t=t.encode('ascii', 'ignore'); t=t.decode('iso-8859-1')
			t=t.encode('utf8'); 
			#for z in [0xc2,0xc3]: t=t.replace(chr(int(z)),'')
		except:
			try: t=t.encode('ascii', 'ignore'); t=t.decode('iso-8859-1')
			except: pass
	if (_a==True): 
		try: t=_addon.decode(t); t=_addon.unescape(t)
		except: t=t
	if (Slashes==True): 
		try: t=t.replace( '_',' ')
		except: t=t
	#t=t.replace("text:u","")
	return t
def nURL(url,method='get',form_data={},headers={},html='',proxy='',User_Agent='',cookie_file='',load_cookie=False,save_cookie=False,compression=True):
	if url=='': return ''
	dhtml=''+html
	if len(User_Agent) > 0: net.set_user_agent(User_Agent)
	else: net.set_user_agent(ps('User-Agent'))
	if len(proxy) > 9: net.set_proxy(proxy)
	if (len(cookie_file) > 0) and (load_cookie==True): 
		if isFile(cookie_file)==True:
			net.set_cookies(cookie_file)
	if   method.lower()=='get':
		try: html=net.http_GET(url,headers=headers,compression=compression).content
		except urllib2.HTTPError,e: 
			debob(['urllib2.HTTPError',e]); 
			try: debob({'code':e.code,'reason':e.reason,'url':url}); 
			except: debob({'code':e.code,'reason':e.msg,'url':url}); 
			html=dhtml
		except Exception,e: debob(['Exception',e]); html=dhtml
		except: html=dhtml
	elif method.lower()=='post':
		try: html=net.http_POST(url,form_data=form_data,headers=headers,compression=compression).content #,compression=False
		except urllib2.HTTPError,e: 
			debob(['urllib2.HTTPError',e]); 
			try: debob({'code':e.code,'reason':e.reason,'url':url}); 
			except: debob({'code':e.code,'reason':e.msg,'url':url}); 
			html=dhtml
		except Exception,e: debob(['Exception',e]); html=dhtml
		except: html=dhtml
	elif method.lower()=='head':
		try: html=net.http_HEAD(url,headers=headers).content
		except urllib2.HTTPError,e: debob(['urllib2.HTTPError',e]); debob({'code':e.code,'reason':e.reason,'url':url}); html=dhtml
		except Exception,e: debob(['Exception',e]); html=dhtml
		except: html=dhtml
	if (len(html) > 0) and (len(cookie_file) > 0) and (save_cookie==True): 
		Cookie_Path=os.path.join(_datapath,_addon_id)
		if not isPath(Cookie_Path): os.makedirs(Cookie_Path)
		net.save_cookies(cookie_file)
	return html
def BusyAnimationShow(): 				xbmc.executebuiltin('ActivateWindow(busydialog)')
def BusyAnimationHide(): 				xbmc.executebuiltin('Dialog.Close(busydialog,true)')
def closeAllDialogs():   				xbmc.executebuiltin('Dialog.Close(all, true)') 
def popYN(title='',line1='',line2='',line3='',n='',y=''):
	diag=xbmcgui.Dialog()
	r=diag.yesno(title,line1,line2,line3,n,y)
	if r: return r
	else: return False
	#del diag
def popOK(msg="",title="",line2="",line3=""):
	dialog=xbmcgui.Dialog()
	#ok=dialog.ok(title, msg, line2, line3)
	dialog.ok(title, msg, line2, line3)

def spAfterSplit(t,ss):
	if ss in t: t=t.split(ss)[1]
	return t
def spBeforeSplit(t,ss):
	if ss in t: t=t.split(ss)[0]
	return t
def TP(s): return xbmc.translatePath(s)
def TPap(s,fe='.py'): return xbmc.translatePath(os.path.join(_addonPath,s+fe))
def TPapp(s,fe=''): return xbmc.translatePath(os.path.join(_addonPath,s+fe))

def CopyAFile(tFrom,tTo):
	try:
		import shutil
		shutil.copy(tFrom,tTo)
	except: pass






def checkHostProblems(url,b=False,t=True):
	if   ('embed.yourupload.com/' in url) or ('novamov.com/' in url) or ('veevr.com/' in url): b=t
	#if   'embed.yourupload.com/' in url: b=t
	#elif 'novamov.com/' in url: b=t
	return b
	
### #Metahandler
#try: 		from script.module.metahandler 	import metahandlers
#except: from metahandler 								import metahandlers
#grab=metahandlers.MetaData(preparezip=False)
#def GRABMETA(name,types):
#	type=types
#	EnableMeta=tfalse(addst("enableMeta"))
#	if (EnableMeta==True):
#		if ('movie' in type):
#			### grab.get_meta(media_type, name, imdb_id='', tmdb_id='', year='', overlay=6)
#			meta=grab.get_meta('movie',name,'',None,None,overlay=6)
#			infoLabels={'rating': meta['rating'],'duration': meta['duration'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],'plot': meta['plot'],'title': meta['title'],'writer': meta['writer'],'cover_url': meta['cover_url'],'director': meta['director'],'cast': meta['cast'],'backdrop': meta['backdrop_url'],'backdrop_url': meta['backdrop_url'],'tmdb_id': meta['tmdb_id'],'year': meta['year'],'votes': meta['votes'],'tagline': meta['tagline'],'premiered': meta['premiered'],'trailer_url': meta['trailer_url'],'studio': meta['studio'],'imdb_id': meta['imdb_id'],'thumb_url': meta['thumb_url']}
#			#infoLabels={'rating': meta['rating'],'duration': meta['duration'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],'plot': meta['plot'],'title': meta['title'],'writer': meta['writer'],'cover_url': meta['cover_url'],'director': meta['director'],'cast': meta['cast'],'backdrop_url': meta['backdrop_url'],'backdrop_url': meta['backdrop_url'],'tmdb_id': meta['tmdb_id'],'year': meta['year']}
#		elif ('tvshow' in type):
#			meta=grab.get_meta('tvshow',name,'','',None,overlay=6)
#			#print meta
#			infoLabels={'rating': meta['rating'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],'plot': meta['plot'],'title': meta['title'],'cover_url': meta['cover_url'],'cast': meta['cast'],'studio': meta['studio'],'banner_url': meta['banner_url'],'backdrop_url': meta['backdrop_url'],'status': meta['status'],'premiered': meta['premiered'],'imdb_id': meta['imdb_id'],'tvdb_id': meta['tvdb_id'],'year': meta['year'],'imgs_prepacked': meta['imgs_prepacked'],'overlay': meta['overlay'],'duration': meta['duration']}
#			#infoLabels={'rating': meta['rating'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],'plot': meta['plot'],'title': meta['title'],'cover_url': meta['cover_url'],'cast': meta['cast'],'studio': meta['studio'],'banner_url': meta['banner_url'],'backdrop_url': meta['backdrop_url'],'status': meta['status']}
#		else: infoLabels={}
#	else: infoLabels={}
#	return infoLabels

def MetaGrab(media_type,meta_name,imdb_id='',tmdb_id='',year='',season='',episode=''):
	default_infoLabels={'overlay':6,'title':meta_name,'tvdb_id':'','imdb_id':'','cover_url':_artIcon,'poster':_artIcon,'trailer_url':'','trailer':'','TVShowTitle':meta_name,'backdrop_url':_artFanart,'banner_url':''}
	try: from metahandler import metahandlers
	except: debob("filed to import metahandler"); return default_infoLabels
	grab=metahandlers.MetaData(preparezip=False)
	try: EnableMeta=tfalse(addst("enableMeta"))
	except: EnableMeta=True
	if (EnableMeta==True):
		if ('movie' in media_type) or (media_type=='m'):
			infoLabels=grab.get_meta("movie",meta_name,imdb_id=imdb_id,tmdb_id=tmdb_id,year=year)
			
		elif ('tvshow' in media_type) or (media_type=='t'):
			infoLabels=grab.get_meta("tvshow",meta_name,imdb_id=imdb_id)
			
		elif ('episode' in media_type) or (media_type=='e'):
			if len(imdb_id)==0:
				t_infoLabels=grab.get_meta("tvshow",meta_name,imdb_id=imdb_id)
				imdb_id=t_infoLabels['imdb_id']
			try:
				iseason=int(season)
				iepisode=int(episode)
				infoLabels=grab.get_episode_meta(tvshowtitle=meta_name,imdb_id=tv_meta['imdb_id'],season=iseason,episode=iepisode)
			except: infoLabels={'overlay':6,'title':str(season)+'x'+str(episode),'tvdb_id':'','imdb_id':'','cover_url':_artIcon,'poster':_artIcon,'TVShowTitle':meta_name}
		else: infoLabels=default_infoLabels
		#
	else: infoLabels=default_infoLabels
	return infoLabels
	#



### ############################################################################################################
class TextBox2: ## Usage Example: TextBox_FromUrl().load('https://raw.github.com/HIGHWAY99/plugin.video.theanimehighway/master/README.md')
	WINDOW 						=	10147; CONTROL_LABEL 		=	1; CONTROL_TEXTBOX 	=	5; HEADER_MESSAGE		=	"%s - ( v%s )" % (__plugin__,addon.get_version())										# set heading
	def load_url(self, URL_PATH, HEADER_MESSAGE2=''):
		deb('text window from url: ',URL_PATH) #self.URL_PATH
		try: 			text=nURL(URL_PATH)#(self.URL_PATH)
		except: 	text=''
		self.load_window(); self.set_header(HEADER_MESSAGE2); self.set_text(text)
	def load_file(self, FILE_NAME='changelog.txt', HEADER_MESSAGE2='', FILE_PATH=_addonPath):
		txt_path = os.path.join(FILE_PATH,FILE_NAME)
		deb('text window from file: ',txt_path)
		f = open(txt_path)
		text = f.read()
		self.load_window(); self.set_header(HEADER_MESSAGE2); self.set_text(text)
	def load_string(self, text_string='', HEADER_MESSAGE2=''):
		self.load_window(); self.set_header(HEADER_MESSAGE2); self.set_text(text_string)
	def load_window(self, sleeptime=500):
		xbmc.executebuiltin("ActivateWindow(%d)" % ( self.WINDOW, ))				# activate the text viewer window
		self.win = xbmcgui.Window(self.WINDOW)															# get window
		xbmc.sleep(sleeptime)																								# give window time to initialize
	def set_header(self, HEADER_MESSAGE2=''):
		if (HEADER_MESSAGE2==''): HEADER_MESSAGE2=self.HEADER_MESSAGE
		self.win.getControl(self.CONTROL_LABEL).setLabel(HEADER_MESSAGE2)
	def set_text(self, text=''):
		self.win.getControl(self.CONTROL_TEXTBOX).setText(text)
def RefreshList(): xbmc.executebuiltin("XBMC.Container.Refresh")
def String2TextBox(message='',HeaderMessage=''): TextBox2().load_string(message,HeaderMessage); #RefreshList()
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
##### Player Functions #####
def PlayItCustomL(url,stream_url,img,title,studio=''):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	listitem=xbmcgui.ListItem(title,iconImage=img,thumbnailImage=img); listitem.setInfo('video',{'Title':title,'Genre':'Live','Studio':studio})
	PL=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); PL.clear(); #PL.add(stream_url,listitem)
	#
	html=nURL(stream_url); deb('Length of html',str(len(html))); 
	matches=re.compile('\n+\s*(.*?://.*)\s*\n+').findall(html)
	#debob(matches)
	if len(matches) > 0:
		for match in matches:
			#debob(match)
			PL.add(match,listitem)
	#
	try: _addon.resolve_url(url)
	except: t=''
	try: play=xbmc.Player(PlayerMeth); play.play(PL)
	except: t=''

def PlayItCustomL2A(url,stream_url,img,title,studio=''):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	listitem=xbmcgui.ListItem(title,iconImage=img,thumbnailImage=img); listitem.setInfo('video',{'Title':title,'Genre':'Live','Studio':studio})
	PL=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); PL.clear(); #PL.add(stream_url,listitem)
	html=nURL(stream_url); deb('Length of html',str(len(html))); 
	html=html.replace('#EXT-X-STREAM-INF:PROGRAM-ID=','#EXT-X-STREAM-INF:NAME="'+title+'",PROGRAM-ID=')
	PlaylistFile=xbmc.translatePath(os.path.join(_addonPath,'resources','playlist.txt')); debob(PlaylistFile)
	_SaveFile(PlaylistFile,html)
	PL.add(PlaylistFile,listitem)
	try: _addon.resolve_url(url)
	except: t=''
	try: play=xbmc.Player(PlayerMeth); play.play(PL)
	except: t=''

def PlayItCustom(url,stream_url,img,title,studio=''):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	listitem=xbmcgui.ListItem(thumbnailImage=img); listitem.setInfo('video',{'Title':title,'Genre':'Live','Studio':studio})
	PL=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); PL.clear(); PL.add(stream_url,listitem)
	try: _addon.resolve_url(url)
	except: t=''
	try: play=xbmc.Player(PlayerMeth); play.play(PL)
	except: t=''

def PlayURL(url):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	play=xbmc.Player(PlayerMeth) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	try: _addon.resolve_url(url)
	except: t=''
	try: play.play(url)
	except: t=''

def PlayURLs(url):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	play=xbmc.Player(PlayerMeth) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	filename=xbmc.translatePath(os.path.join(_addonPath,'resources','test.strm'))
	try: _addon.resolve_url(url)
	except: pass
	if ':' in url: uPre=url.split(':')[0]
	else: uPre='____'
	if (uPre.lower()=='mss') or (uPre.lower()=='mssh') or (uPre.lower()=='rtsp'):
		_SaveFile(filename,url)
		try: play.play(filename) #(url)
		except: pass
	elif (uPre.lower()=='http'):
		import urlresolver
		try:
			stream_url=urlresolver.HostedMediaFile(url).resolve()
			play.play(stream_url)
		except:
			try: play.play(url)
			except: pass
	else:
		try: play.play(url)
		except: pass
	#

def PlayURLs2(url):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	play=xbmc.Player(PlayerMeth) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	filename=xbmc.translatePath(os.path.join(_addonPath,'resources','test.strm'))
	try: _addon.resolve_url(url)
	except: pass
	if ':' in url: uPre=url.split(':')[0]
	else: uPre='____'
	if (uPre.lower()=='mss') or (uPre.lower()=='mssh') or (uPre.lower()=='rtsp'):
		_SaveFile(filename,url)
		try: play.play(filename) #(url)
		except: pass
	else:
		try: play.play(url)
		except: pass

def PlayURLstrm(url):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	play=xbmc.Player(PlayerMeth) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	filename=xbmc.translatePath(os.path.join(_addonPath,'resources','test.strm'))
	_SaveFile(filename,url)
	try: _addon.resolve_url(url)
	except: t=''
	try: play.play(filename) #(url)
	except: t=''

def PlayVideo(url):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	play=xbmc.Player(PlayerMeth) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#import urlresolver
	infoLabels={"Studio":addpr('studio',''),"ShowTitle":addpr('showtitle',''),"Title":addpr('title','')}
	li=xbmcgui.ListItem(addpr('title',''),iconImage=addpr('img',''),thumbnailImage=addpr('img',''))
	li.setInfo(type="Video", infoLabels=infoLabels ); li.setProperty('IsPlayable', 'true')
	#xbmc.Player().stop()
	try: _addon.resolve_url(url)
	except: t=''
	try: play.play(url, li)
	except: t=''

def PlayPictures(url):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	play=xbmc.Player(PlayerMeth) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#import urlresolver
	infoLabels={"Studio":addpr('studio',''),"ShowTitle":addpr('showtitle',''),"Title":addpr('title','')}
	li=xbmcgui.ListItem(addpr('title',''),iconImage=addpr('img',''),thumbnailImage=addpr('img',''))
	li.setInfo(type="pictures", infoLabels=infoLabels ); li.setProperty('IsPlayable', 'true')
	#xbmc.Player().stop()
	try: _addon.resolve_url(url)
	except: t=''
	try: play.play(url, li)
	except: t=''

def PlayFromHost(url):
	PlayerMethod=addst("core-player")
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	play=xbmc.Player(PlayerMeth) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	import urlresolver
	infoLabels={"Studio":addpr('studio',''),"ShowTitle":addpr('showtitle',''),"Title":addpr('title','')}
	li=xbmcgui.ListItem(addpr('title',''),iconImage=addpr('img',''),thumbnailImage=addpr('img',''))
	li.setInfo(type="Video", infoLabels=infoLabels ); li.setProperty('IsPlayable', 'true')
	deb('url',url)
	###
	#try: _addon.resolve_url(url)
	#except: t=''
	#stream_url='http://s6.vidcache.net/stream/a4133ca7743c0a0f4ff063f715d934472bb1d513?client_file_id=524368'
	#play.play(stream_url, li)
	###
	if ('youtube.com' in url):
		stream_url=url
	else:
		debob(urlresolver.HostedMediaFile(url))
		#stream_url = urlresolver.HostedMediaFile(url).resolve()
		try: stream_url = urlresolver.HostedMediaFile(url).resolve()
		except: deb('Link URL Was Not Resolved',url); myNote("urlresolver.HostedMediaFile(url).resolve()","Failed to Resolve Playable URL."); return
	try: debob(stream_url) #deb('stream_url',stream_url)
	except: t=''
	#xbmc.Player().stop()
	try: _addon.resolve_url(url)
	except: t=''
	wwT=addpr("wwT"); wwB=tfalse(addpr("MarkAsWatched","false")); 
	deb("MarkAsWatched",str(wwB)); 
	try: 
		if (wwB==True) and (len(wwT) > 0): deb("Attempting to add episode to watched list",wwT); visited_add(wwT); 
		play.play(stream_url,li); 
	except: 
		if (wwB==True) and (len(wwT) > 0): deb("Attempting to remove episode to watched list",wwT); visited_remove(wwT); 
		t=''; 

### ############################################################################################################
### ############################################################################################################

def filename_filter_out_year(name=''):
	years=re.compile(' \((\d+)\)').findall('__'+name+'__')
	for year in years:
		name=name.replace(' ('+year+')','')
	name=name.strip()
	return name

def QP(v): return urllib.quote_plus(v)

def DoLabs2LB(labs,subfav=''):
	LB={}
	n='title'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='year'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='img'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='fanart'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='plot'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='url'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='country'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='genres'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='todoparams'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='commonid'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='commonid2'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='plot'
	try: LB[n]=str(labs[n])
	except: LB[n]=''
	n='site'
	try: LB[n]=labs[n]
	except: 
		try: LB[n]=addpr(n,'')
		except: LB[n]=''
	n='section'
	try: LB[n]=labs[n]
	except: 
		try: LB[n]=addpr(n,'')
		except: LB[n]=''
	##try: LB['subfav']=subfav
	##except: LB['subfav']=''
	#n=''
	#try: LB[n]=labs[n]
	#except: LB[n]=''
	return LB

def ContextMenu_Favorites(labs={}):
	contextMenuItems=[]; nameonly=filename_filter_out_year(labs['title'])
	try: site=labs['site']
	except: site=addpr('site','')
	try: section=labs['section']
	except: section=addpr('section','')
	try: _subfav=addpr('subfav','')
	except: _subfav=''
	if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	try:
		if _subfav=='': _sf='1'
		else: _sf=_subfav
		WRFC=ps('WhatRFavsCalled')
		LB=DoLabs2LB(labs); LB['mode']='cFavoritesAdd'; P1='XBMC.RunPlugin(%s)'
		if _sf is not '1': LB['subfav']= ''; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.1.name'),Pars))
		if _sf is not '2': LB['subfav']='2'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.2.name'),Pars))
		if _sf is not '3': LB['subfav']='3'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.3.name'),Pars))
		if _sf is not '4': LB['subfav']='4'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.4.name'),Pars))
		if _sf is not '5': LB['subfav']='5'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.5.name'),Pars))
		if _sf is not '6': LB['subfav']='6'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.6.name'),Pars))
		if _sf is not '7': LB['subfav']='7'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.7.name'),Pars))
		LB['mode']='cFavoritesRemove'; LB['subfav']=_subfav; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append(('Remove: '+WRFC+addst('fav.tv.'+_sf+'.name'),Pars))
	except: pass
	
	
	return contextMenuItems

def ContextMenu_Movies(labs={}):
	contextMenuItems=[]; nameonly=filename_filter_out_year(labs['title'])
	try: site=labs['site']
	except: site=addpr('site','')
	try: section=labs['section']
	except: section=addpr('section','')
	if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Movie Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	if (tfalse(addst("CMI_SearchKissAnime"))==True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.kissanime')): contextMenuItems.append(('Search KissAnime', 'XBMC.Container.Update(%s?mode=%s&pageno=1&pagecount=1&title=%s)' % ('plugin://plugin.video.kissanime/','Search',nameonly)))
	if (tfalse(addst("CMI_SearchSolarMovieso"))==True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.solarmovie.so')): contextMenuItems.append(('Search Solarmovie.so', 'XBMC.Container.Update(%s?mode=%s&section=%s&title=%s)' % ('plugin://plugin.video.solarmovie.so/','Search','movies',nameonly)))
	if (tfalse(addst("CMI_Search1Channel"))==True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.1channel')): contextMenuItems.append(('Search 1Channel', 'XBMC.Container.Update(%s?mode=7000&section=%s&query=%s)' % ('plugin://plugin.video.1channel/','movies',nameonly)))
	#if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.merdb'): contextMenuItems.append(('Search MerDB', 'XBMC.Container.Update(%s?mode=%s&section=%s&url=%s&title=%s)' % ('plugin://plugin.video.merdb/','Search','movies',urllib.quote_plus('http://merdb.ru/'),nameonly)))
	#if os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.icefilms'): contextMenuItems.append(('Search Icefilms','XBMC.Container.Update(%s?mode=555&url=%s&search=%s&nextPage=%s)' % ('plugin://plugin.video.icefilms/', 'http://www.icefilms.info/', title, '1')))
	try:
		WRFC=ps('WhatRFavsCalled')
		LB=DoLabs2LB(labs); LB['mode']='cFavoritesAdd'; P1='XBMC.RunPlugin(%s)'
		LB['subfav']= ''; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.movies.1.name'),Pars))
		LB['subfav']='2'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.movies.2.name'),Pars))
		LB['subfav']='3'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.movies.3.name'),Pars))
		LB['subfav']='4'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.movies.4.name'),Pars))
		LB['subfav']='5'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.movies.5.name'),Pars))
		LB['subfav']='6'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.movies.6.name'),Pars))
		LB['subfav']='7'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.movies.7.name'),Pars))
	except: pass
	
	
	
	return contextMenuItems

def ContextMenu_Series(labs={}):
	contextMenuItems=[]; nameonly=filename_filter_out_year(labs['title'])
	try: site=labs['site']
	except: site=addpr('site','')
	try: section=labs['section']
	except: section=addpr('section','')
	if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Show Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	if (tfalse(addst("CMI_FindAirDates"))==True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.solarmovie.so')): contextMenuItems.append(('Find AirDates', 'XBMC.Container.Update(%s?mode=%s&title=%s)' % ('plugin://plugin.video.solarmovie.so/','SearchForAirDates',labs['title'])))
	if (tfalse(addst("CMI_SearchKissAnime"))==True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.kissanime')): contextMenuItems.append(('Search KissAnime', 'XBMC.Container.Update(%s?mode=%s&pageno=1&pagecount=1&title=%s)' % ('plugin://plugin.video.kissanime/','Search',nameonly)))
	if (tfalse(addst("CMI_SearchSolarMovieso"))==True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.solarmovie.so')): contextMenuItems.append(('Search Solarmovie.so', 'XBMC.Container.Update(%s?mode=%s&section=%s&title=%s)' % ('plugin://plugin.video.solarmovie.so/','Search','tv',nameonly)))
	if (tfalse(addst("CMI_Search1Channel"))==True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.1channel')): contextMenuItems.append(('Search 1Channel', 'XBMC.Container.Update(%s?mode=7000&section=%s&query=%s)' % ('plugin://plugin.video.1channel/','tv',nameonly)))
	if (tfalse(addst("CMI_SearchMerDBru"))==True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.merdb')): contextMenuItems.append(('Search MerDB', 'XBMC.Container.Update(%s?mode=%s&section=%s&url=%s&title=%s)' % ('plugin://plugin.video.merdb/','Search','tvshows',urllib.quote_plus('http://merdb.ru/tvshow/'),nameonly)))
	if (tfalse(addst("CMI_SearchIceFilms"))==True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.icefilms')): contextMenuItems.append(('Search Icefilms','XBMC.Container.Update(%s?mode=555&url=%s&search=%s&nextPage=%s)' % ('plugin://plugin.video.icefilms/', 'http://www.icefilms.info/', labs['title'], '1')))
	try:
	#if site==site:
		WRFC=ps('WhatRFavsCalled'); WRFCr='Remove: '
		LB=DoLabs2LB(labs); McFA='cFavoritesAdd'; McFR='cFavoritesRemove'; LB['mode']=McFA; P1='XBMC.RunPlugin(%s)'
		#LB['mode']=McFA; LB['subfav']= ''; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.1.name'),Pars))
		LB['subfav']='1'; 
		if fav__COMMON__check(LB['site'],LB['section'],LB['title'],LB['year'],LB['subfav'])==True: LB['mode']=McFR; LabelName=WRFCr+WRFC+addst('fav.tv.'+LB['subfav']+'.name'); 
		else: LB['mode']=McFA; LabelName=WRFC+addst('fav.tv.'+LB['subfav']+'.name'); 
		LB['subfav']=''; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((LabelName,Pars)); 
		for nn in ['2','3','4','5','6','7']:
			LB['subfav']=nn; 
			if fav__COMMON__check(LB['site'],LB['section'],LB['title'],LB['year'],LB['subfav'])==True: LB['mode']=McFR; LabelName=WRFCr+WRFC+addst('fav.tv.'+LB['subfav']+'.name'); 
			else: LB['mode']=McFA; LabelName=WRFC+addst('fav.tv.'+LB['subfav']+'.name'); 
			Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((LabelName,Pars)); 
		#LB['mode']=McFA; LB['subfav']='2'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.2.name'),Pars))
		#LB['mode']=McFA; LB['subfav']='3'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.3.name'),Pars))
		#LB['mode']=McFA; LB['subfav']='4'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.4.name'),Pars))
		#LB['mode']=McFA; LB['subfav']='5'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.5.name'),Pars))
		#LB['mode']=McFA; LB['subfav']='7'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.7.name'),Pars))
		LB['mode']='refresh_meta'; LabelName='Refresh MetaData'; 
		LB['imdb_id']=LB['commonid']; LB['alt_id']='imdbnum'; LB['video_type']='tvshow'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((LabelName,Pars)); 
		
	except: pass
	
	return contextMenuItems

def ContextMenu_Episodes(labs={}):
	contextMenuItems=[] #; nameonly=filename_filter_out_year(labs['title'])
	if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Episode Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	
	
	return contextMenuItems

def ContextMenu_Hosts(labs={},contextMenuItems=[]):
	contextMenuItems=[] #; nameonly=filename_filter_out_year(labs['title'])
	#if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Host Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	if tfalse(addst("CMI_JDownloaderResolver"))==True: contextMenuItems.append(('JDownloader (UrlResolver)','XBMC.RunPlugin(%s?mode=%s&url=%s&useResolver=%s)' % ('plugin://'+ps('addon_id')+'/','toJDownloader',urllib.quote_plus(labs['url']),'true')))
	if tfalse(addst("CMI_JDownloader"))==True: contextMenuItems.append(('JDownloader (Url)','XBMC.RunPlugin(%s?mode=%s&url=%s&useResolver=%s)' % ('plugin://'+ps('addon_id')+'/','toJDownloader',urllib.quote_plus(labs['url']),'false')))
	if ('destfile' in labs) and (len(addst('download_folder_default','')) > 0):
		contextMenuItems.append(('Download','XBMC.RunPlugin(%s?mode=%s&url=%s&useResolver=%s&destpath=%s&destfile=%s)' % ('plugin://'+ps('addon_id')+'/','Download',urllib.quote_plus(labs['url']),'true',urllib.quote_plus(addst('download_folder_default','')),urllib.quote_plus(labs['destfile']) ) ))
	#elif ('title' in labs) and (len(addst('download_folder_default','')) > 0):
	
	
	
	return contextMenuItems

def ContextMenu_LiveStreams(labs={},contextMenuItems=[]):
	contextMenuItems=[] #; nameonly=filename_filter_out_year(labs['title'])
	try: site=labs['site']
	except: site=addpr('site','')
	try: section=labs['section']
	except: section=addpr('section','')
	if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Stream Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	#try:
	#	WRFC=ps('WhatRFavsCalled')
	#	LB=DoLabs2LB(labs); LB['mode']='cFavoritesAdd'; P1='XBMC.RunPlugin(%s)'
	#	LB['subfav']= ''; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.1.name'),Pars))
	#	#LB['subfav']='2'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.2.name'),Pars))
	#	#LB['subfav']='3'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.3.name'),Pars))
	#	#LB['subfav']='4'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.4.name'),Pars))
	#	#LB['subfav']='5'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.5.name'),Pars))
	#	#LB['subfav']='6'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.6.name'),Pars))
	#	#LB['subfav']='7'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.7.name'),Pars))
	#except: pass

	
	
	return contextMenuItems

def ContextMenu_VideoUrls(labs={},contextMenuItems=[]):
	contextMenuItems=[] #; nameonly=filename_filter_out_year(labs['title'])
	#if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Url Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	if tfalse(addst("CMI_JDownloader"))==True: contextMenuItems.append(('JDownloader (Url)','XBMC.RunPlugin(%s?mode=%s&url=%s&useResolver=%s)' % ('plugin://'+ps('addon_id')+'/','toJDowfnloader',urllib.quote_plus(labs['url']),'false')))
	#contextMenuItems.append(('Downloader','XBMC.RunPlugin(%s?mode=%s&url=%s&useResolver=%s&destpath=%s&destfile=%s)' % ('plugin://'+ps('addon_id')+'/','Download',labs['url'],'false','','')))
	
	
	return contextMenuItems

def ContextMenu_ImageUrls(labs={},contextMenuItems=[]):
	contextMenuItems=[] #; nameonly=filename_filter_out_year(labs['title'])
	if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Url Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	
	
	return contextMenuItems

def ContextMenu_AudioUrls(labs={},contextMenuItems=[]):
	contextMenuItems=[] #; nameonly=filename_filter_out_year(labs['title'])
	if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Url Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	
	
	return contextMenuItems

def ContextMenu_AudioStreams(labs={},contextMenuItems=[]):
	contextMenuItems=[] #; nameonly=filename_filter_out_year(labs['title'])
	if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Url Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	
	
	return contextMenuItems

def ContextMenu_AudioRadioStreams(labs={},contextMenuItems=[]):
	contextMenuItems=[] #; nameonly=filename_filter_out_year(labs['title'])
	if tfalse(addst("CMI_ShowInfo"))==True: contextMenuItems.append(('Url Info',ps('cMI.showinfo.url')))
	if labs=={}: return contextMenuItems
	
	
	return contextMenuItems





















def XBMC_RunPlugin(plugId,plugParams,plugFile=''): xbmc.executebuiltin("XBMC.RunPlugin(plugin://%s/%s?%s)" % (plugId,plugFile,plugParams) )
def XBMC_ContainerUpdate(plugId,plugParams,plugFile=''): xbmc.executebuiltin("XBMC.Container.Update(plugin://%s/%s?%s)" % (plugId,plugFile,plugParams) )



### ############################################################################################################
### ############################################################################################################

def SendTo_JDownloader(url,useResolver=True):
	myNote('Download','sending to jDownloader plugin',15000)
	if useResolver==True:
		try: 
			import urlresolver
			link=urlresolver.HostedMediaFile(url).resolve()
		except: link=url
	else: link=url
	xbmc.executebuiltin("XBMC.RunPlugin(plugin://plugin.program.jdownloader/?action=addlink&url=%s)" % link)
	try: _addon.resolve_url(url)
	except: pass

### ############################################################################################################
### ############################################################################################################
#import c_Extract as extract #extract.all(lib,addonfolder,dp)
#import c_HiddenDownloader as downloader #downloader.download(url,destfile,destpath,useResolver=True)
def ExtractThis(filename,destpath):
	import c_Extract as extract
	return extract.allNoProgress(filename,destpath)

def DownloadThis(url,destfile,destpath,useResolver=True):
	destpath=xbmc.translatePath(destpath)
	import c_HiddenDownloader as downloader
	debob(str(useResolver))
	if useResolver==True:
		try: 
			import urlresolver
			#debob(urlresolver.HostedMediaFile(url))
			link=urlresolver.HostedMediaFile(url).resolve()
		except: link=url
	else: link=url
	deb('downloadable url',link)
	downloader.download(link,destfile,destpath,useResolver)
	#downloader.download(url,destfile,destpath,useResolver)

def DownloadThisSilently(url,destfile,destpath,useResolver=True):
	destpath=xbmc.translatePath(destpath)
	import c_HiddenDownloader as downloader
	#debob(str(useResolver))
	if useResolver==True:
		try: 
			import urlresolver
			#debob(urlresolver.HostedMediaFile(url))
			link=urlresolver.HostedMediaFile(url).resolve()
		except: link=url
	else: link=url
	#deb('downloadable url',link)
	downloader.downloadSilent(link,destfile,destpath,useResolver)

### ############################################################################################################
### ############################################################################################################

def XBMC_RefreshRSS(): 					xbmc.executebuiltin("XBMC.RefreshRSS()")
def XBMC_EjectTray(): 					xbmc.executebuiltin("XBMC.EjectTray()")
def XBMC_Mute(): 								xbmc.executebuiltin("XBMC.Mute()")
def XBMC_System_Exec(url): 			xbmc.executebuiltin("XBMC.System.Exec(%s)" % url)
def XBMC_System_ExecWait(url): 	xbmc.executebuiltin("XBMC.System.ExecWait(%s)" % url)
def XBMC_PlayDVD(): 						xbmc.executebuiltin("XBMC.PlayDVD()")
def XBMC_ReloadSkin(): 					xbmc.executebuiltin("XBMC.ReloadSkin()")
def XBMC_UpdateAddonRepos(): 		xbmc.executebuiltin("XBMC.UpdateAddonRepos()")
def XBMC_UpdateLocalAddons(): 	xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
def XBMC_Weather_Refresh(): 		xbmc.executebuiltin("XBMC.Weather.Refresh()")
def XBMC_ToggleDebug(): 				xbmc.executebuiltin("XBMC.ToggleDebug()")
def XBMC_Minimize(): 						xbmc.executebuiltin("XBMC.Minimize()")
def XBMC_ActivateScreensaver(): xbmc.executebuiltin("XBMC.ActivateScreensaver()")

### ############################################################################################################
### ############################################################################################################

def fav__COMMON__empty(site,section,subfav=''): WhereAmI('@ Favorites - Empty - %s%s' % (section,subfav)); favs=[]; cache.set('favs_'+site+'__'+section+subfav+'__', str(favs)); myNote(bFL('Favorites'),bFL('Your Favorites Have Been Wiped Clean. Bye Bye.'))
def fav__COMMON__remove(site,section,name,year,subfav=''):
	WhereAmI('@ Favorites - Remove - %s%s' % (section,subfav)); deb('fav__remove() '+section,name+'  ('+year+')'); saved_favs=cache.get('favs_'+site+'__'+section+subfav+'__'); tf=False
	if saved_favs:
		favs=eval(saved_favs)
		if favs:
			for (_name,_year,_img,_fanart,_country,_url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2) in favs: 
				if (name==_name) and (year==_year): favs.remove((_name,_year,_img,_fanart,_country,_url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2)); cache.set('favs_'+site+'__'+section+subfav+'__', str(favs)); tf=True; myNote(bFL(name.upper()+'  ('+year+')'),bFL('Removed from Favorites')); deb(name+'  ('+year+')','Removed from Favorites. (Hopefully)'); xbmc.executebuiltin("XBMC.Container.Refresh"); return
			if (tf==False): myNote(bFL(name.upper()),bFL('not found in your Favorites'))
		else: myNote(bFL(name.upper()+'  ('+year+')'),bFL('not found in your Favorites'))

def fav__COMMON__add(site,section,name,year='',img=_artIcon,fanart=_artFanart,subfav='',plot='',commonID='',commonID2='',ToDoParams='',Country='',Genres='',Url=''):
	debob(['fav__add()',section,name+'  ('+year+')',img,fanart]); WhereAmI('@ Favorites - Add - %s%s' % (section,subfav)); saved_favs=cache.get('favs_'+site+'__'+section+subfav+'__'); favs=[]; fav_found=False
	if saved_favs:
		#debob(saved_favs)
		favs=eval(saved_favs)
		if favs:
			#debob(favs)
			for (_name,_year,_img,_fanart,_country,_url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2) in favs:
				if (name==_name) and (year==_year): 
					fav_found=True; 
					if len(year) > 0: myNote(bFL(section+':  '+name.upper()+'  ('+year+')'),bFL('Already in your Favorites')); 
					else: myNote(bFL(section+':  '+name.upper()),bFL('Already in your Favorites')); 
					return
	#
	debob(['name',name,'year',year,'img',img,'fanart',fanart,'Country',Country,'Url',Url,'plot',plot,'Genres',Genres,'site',site,'subfav',subfav,'section',section,'ToDoParams',ToDoParams,'commonID',commonID,'commonID2',commonID2])
	if fav_found==False:
		deb('Adding Favorite',site+' - '+section+' - '+subfav)
		favs.append((name,year,img,fanart,Country,Url,plot,Genres,site,subfav,section,ToDoParams,commonID,commonID2))
		##if   (section==ps('section.tvshows')): favs.append((name,year,img,fanart,_param['country'],_param['url'],_param['plot'],_param['genre'],_param['dbid']))
		##elif (section==ps('section.movie')): favs.append((name,year,img,fanart,_param['country'],_param['url'],_param['plot'],_param['genre'],''))
		##else: myNote('Favorites:  '+section,'Section not Found')
		#
		deb('number of favorites found',str(len(favs))); 
		cache.set('favs_'+site+'__'+section+subfav+'__', str(favs)); 
		if len(year) > 0: myNote(bFL(str(len(favs))+' '+name+'  ('+year+')'),bFL('Added to Favorites'))
		else: myNote(str(len(favs))+' '+bFL(name),bFL('Added to Favorites'))
	#

def fav__COMMON__list_fetcher(site,section='',subfav=''):
	WhereAmI('@ Favorites - List - %s%s' % (section,subfav)); saved_favs=cache.get('favs_'+site+'__'+section+subfav+'__'); favs=[]
	if saved_favs:
		debob('saved_favs found'); debob(saved_favs); favs=sorted(eval(saved_favs), key=lambda fav: (fav[1],fav[0]),reverse=True); ItemCount=len(favs)
		if favs:
			debob('favs found'); debob(favs); 
			return favs
			## ((name,year,img,fanart,Country,Url,plot,Genres,site,subfav,section,ToDoParams,commonID,commonID2))
			#for (name,year,img,fanart,country,url,plot,genre,dbid) in favs:
			#		except: deb('Error Listing Item',name+'  ('+year+')')
			#	else: myNote('Favorites:  '+section,'Section not found'); 
			#if   (section==ps('section.tvshows')): 		set_view('tvshows',addst('anime-view'),True)
			#elif (section==ps('section.movie')): 	set_view('movies' ,addst('movies-view'),True)
		else: return ''
	else: return ''
	#

def fav__COMMON__check(site,section,name,year,subfav=''):
	saved_favs=cache.get('favs_'+site+'__'+section+subfav+'__'); 
	if saved_favs:
		favs=eval(saved_favs); 
		if favs:
			for (_name,_year,_img,_fanart,_country,_url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2) in favs: 
				if (name==_name) and (year==_year): return True
			return False
		else: return False






### ############################################################################################################
### ############################################################################################################




### ############################################################################################################
### ############################################################################################################

def filename_filter_out_year(name=''):
	years=re.compile(' \((\d+)\)').findall('__'+name+'__')
	for year in years:
		name=name.replace(' ('+year+')','')
	name=name.strip()
	return name

def filename_filter_colorcodes(name=''):
	if ('[/color]' 				in name): name=name.replace('[/color]','')
	if ('[/COLOR]' 				in name): name=name.replace('[/COLOR]','')
	if ('[color lime]' 		in name): name=name.replace('[color lime]','')
	if ('[COLOR lime]' 		in name): name=name.replace('[COLOR lime]','')
	if ('[COLOR green]' 	in name): name=name.replace('[COLOR green]','')
	if ('[COLOR yellow]' 	in name): name=name.replace('[COLOR yellow]','')
	if ('[COLOR red]' 		in name): name=name.replace('[COLOR red]','')
	if ('[b]' 						in name): name=name.replace('[b]','')
	if ('[B]' 						in name): name=name.replace('[B]','')
	if ('[/b]' 						in name): name=name.replace('[/b]','')
	if ('[/B]' 						in name): name=name.replace('[/B]','')
	if ('[cr]' 						in name): name=name.replace('[cr]','')
	if ('[CR]' 						in name): name=name.replace('[CR]','')
	if ('[i]' 						in name): name=name.replace('[i]','')
	if ('[I]' 						in name): name=name.replace('[I]','')
	if ('[/i]' 						in name): name=name.replace('[/i]','')
	if ('[/I]' 						in name): name=name.replace('[/I]','')
	if ('[uppercase]' 		in name): name=name.replace('[uppercase]','')
	if ('[UPPERCASE]' 		in name): name=name.replace('[UPPERCASE]','')
	if ('[lowercase]' 		in name): name=name.replace('[lowercase]','')
	if ('[LOWERCASE]' 		in name): name=name.replace('[LOWERCASE]','')
	name=name.strip()
	#if ('' in name): name=name.replace('','')
	#if ('' in name): name=name.replace('','')
	#if ('' in name): name=name.replace('','')
	return name

def Download_PrepExt(url,ext='.flv'):
	if    '.zip' in url: ext='.zip' #Compressed Files
	elif  '.rar' in url: ext='.rar'
	elif   '.z7' in url: ext='.z7'
	elif  '.png' in url: ext='.png' #images
	elif  '.jpg' in url: ext='.jpg'
	elif  '.gif' in url: ext='.gif'
	elif  '.bmp' in url: ext='.bmp'
	elif '.jpeg' in url: ext='.jpeg'
	elif  '.mp4' in url: ext='.mp4' #Videos
	elif '.mpeg' in url: ext='.mpeg'
	elif  '.avi' in url: ext='.avi'
	elif  '.flv' in url: ext='.flv'
	elif  '.wmv' in url: ext='.wmv'
	elif  '.mp3' in url: ext='.mp3' #others
	elif  '.txt' in url: ext='.txt'
	#else: 							 ext='.flv' #Default File Extention ('.flv')
	return ext

### ############################################################################################################
### ############################################################################################################
def visited_DoCheck(urlToCheck,s='[B][COLOR yellowgreen]@[/COLOR][/B] ',e='[COLOR black]@[/COLOR] '):
	#visited_empty()
	#return ''
	vc=visited_check(urlToCheck)
	if (vc==True): return s
	else: 
		##visited_add(urlToCheck)
		return e

def visited_check(urlToCheck):
  try: saved_visits = cache.get('visited_')
  except: return False
  erNoFavs='XBMC.Notification([B][COLOR orange]Favorites[/COLOR][/B],[B]You have no favorites saved.[/B],5000,"")'
  if not saved_visits: return False #xbmc.executebuiltin(erNoFavs)
  if saved_visits == '[]': return False #xbmc.executebuiltin(erNoFavs)
  if saved_visits:
  	visits = eval(saved_visits)
  	if (urlToCheck in visits): return True
  return False

def visited_check2(urlToCheck):
  try: saved_visits = cache.get('visited_')
  except: return False
  erNoFavs='XBMC.Notification([B][COLOR orange]Favorites[/COLOR][/B],[B]You have no favorites saved.[/B],5000,"")'
  if not saved_visits: return False #xbmc.executebuiltin(erNoFavs)
  if saved_visits == '[]': return False #xbmc.executebuiltin(erNoFavs)
  if saved_visits:
  	visits = eval(saved_visits)
  	if visits:
  		for (title) in visits:
  			if (urlToCheck in title): return True
  return False

def visited_empty():
  saved_favs = cache.get('visited_')
  favs = []
  cache.set('visited_', str(favs))
  notification('[B][COLOR orange]Visited[/COLOR][/B]','[B] Your Visited Data has been wiped clean. Bye Bye.[/B]')


def visited_remove(urlToRemove):
	saved_visits = cache.get('visited_')
	visits = []
	if saved_visits:
		visits = eval(saved_visits)
		if visits:
			#print visits; print urlToRemove
			for (title) in visits:
				if (urlToRemove==title): 
					visits.remove((urlToRemove)); 
					cache.set('visited_', str(visits))
					#RefreshList(); 
					return
	##########
	##if saved_favs:
	##	favs=eval(saved_favs)
	##	if favs:
	##		for (_name,_year,_img,_fanart,_country,_url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2) in favs: 
	##			if (name==_name) and (year==_year): favs.remove((_name,_year,_img,_fanart,_country,_url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2)); cache.set('favs_'+site+'__'+section+subfav+'__', str(favs)); tf=True; myNote(bFL(name.upper()+'  ('+year+')'),bFL('Removed from Favorites')); deb(name+'  ('+year+')','Removed from Favorites. (Hopefully)'); xbmc.executebuiltin("XBMC.Container.Refresh"); return
	##		if (tf==False): myNote(bFL(name.upper()),bFL('not found in your Favorites'))
	##	else: myNote(bFL(name.upper()+'  ('+year+')'),bFL('not found in your Favorites'))

def visited_add(urlToAdd):
	if (urlToAdd==''): return ''
	elif (urlToAdd==None): return ''
	deb('checking rather url has been visited',urlToAdd)
	saved_visits = cache.get('visited_')
	visits = []
	if saved_visits:
		#deb('saved visits',saved_visits)
		visits = eval(saved_visits)
		if visits:
			if (urlToAdd) in visits: return
	visits.append((urlToAdd))
	cache.set('visited_', str(visits))

def wwCMI(cMI,ww,t): #for Watched State ContextMenuItems
	sRP='XBMC.RunPlugin(%s)'; site=addpr("site"); section=addpr("section"); 
	if   ww==7: 
		cMI.append(("Unmark",sRP % _addon.build_plugin_url({'mode':'RemoveVisit','title':t,'site':site,'section':section})))
		cMI.append(("Empty Visits",sRP % _addon.build_plugin_url({'mode':'EmptyVisit','site':site,'section':section})))
	elif ww==6: 
		cMI.append(("Mark",sRP % _addon.build_plugin_url({'mode':'AddVisit','title':t,'site':site,'section':section})))
	return cMI

### ############################################################################################################
### ############################################################################################################
def refresh_meta(video_type,old_title,imdb,alt_id,year,new_title=''):
	try: from metahandler import metahandlers
	except: return
	__metaget__=metahandlers.MetaData()
	if new_title: search_title=new_title
	else: search_title=old_title
	if video_type=='tvshow':
		api=metahandlers.TheTVDB(); results=api.get_matching_shows(search_title); search_meta=[]
		for item in results: option={'tvdb_id':item[0],'title':item[1],'imdb_id':item[2],'year':year}; search_meta.append(option)
	else: search_meta=__metaget__.search_movies(search_title)
	debob(search_meta); #deb('search_meta',search_meta); 
	option_list=['Manual Search...']
	for option in search_meta:
		if 'year' in option: disptitle='%s (%s)' % (option['title'],option['year'])
		else: disptitle=option['title']
		option_list.append(disptitle)
	dialog=xbmcgui.Dialog(); index=dialog.select('Choose',option_list)
	if index==0: refresh_meta_manual(video_type,old_title,imdb,alt_id,year)
	elif index > -1:
		new_imdb_id=search_meta[index-1]['imdb_id']
		#Temporary workaround for metahandlers problem:
		#Error attempting to delete from cache table: no such column: year
		if video_type=='tvshow': year=''
		try: _1CH.log(search_meta[index-1])
		except: pass
		__metaget__.update_meta(video_type,old_title,imdb,year=year); xbmc.executebuiltin('Container.Refresh')

def refresh_meta_manual(video_type,old_title,imdb,alt_id,year):
	keyboard=xbmc.Keyboard()
	if year: disptitle='%s (%s)' % (old_title,year)
	else: disptitle=old_title
	keyboard.setHeading('Enter a title'); keyboard.setDefault(disptitle); keyboard.doModal()
	if keyboard.isConfirmed():
		search_string=keyboard.getText()
		refresh_meta(video_type,old_title,imdb,alt_id,year,search_string)

### ############################################################################################################
### ############################################################################################################

def DoE(e): xbmc.executebuiltin(e)
def DoAW(e): xbmc.executebuiltin("ActivateWindow(%s)" % str(e))
def DoRW(e): xbmc.executebuiltin("ReplaceWindow(%s)" % str(e))
def DoRA(e): xbmc.executebuiltin("RunAddon(%s)" % str(e))
def DoRA2(e,e2="1",e3=""): xbmc.executebuiltin('RunAddon(%s,"%s","%s")' % (str(e),str(e2),e3)); 
def DoA(a): xbmc.executebuiltin("Action(%s)" % str(a))
def DoCM(a): xbmc.executebuiltin("Control.Message(windowid=%s)" % (str(a)))
def DoSC(a): xbmc.executebuiltin("SendClick(%s)" % (str(a)))
def DoSC2(a,Id): xbmc.executebuiltin("SendClick(%s,%s)" % (str(a),str(Id)))
def DoStopScript(e): xbmc.executebuiltin("StopScript(%s)" % str(e))
def DoTD(): xbmc.executebuiltin("ToggleDebug")

### ############################################################################################################
### ############################################################################################################
##### SQL #####
try:    from sqlite3   import dbapi2 as orm; dbMethod="sqlite3";   deb("SQL Method","sqlite3"); 
except: from pysqlite2 import dbapi2 as orm; dbMethod="pysqlite2"; deb("SQL Method","pysqlite2"); 
DB_DIR=ps('db filename'); CorrectValueForInitDatabase="1"; 
def init_database():
	try:
		deb('Building Database',DB_DIR); s=[]; db=orm.connect(DB_DIR); 
		#pageUrl='',Name='',Thumb='',roomId='',roomSlug='',plot='',liVe='',
		#streamUrl='',streamkey='',youtubekey='',sourcetype='show'
		s.append('CREATE TABLE IF NOT EXISTS channels (pageurl VARCHAR(255) UNIQUE, title TEXT, streamtype VARCHAR(30), live VARCHAR(30), thumb TEXT, fanart TEXT, roomid VARCHAR(50), roomslug VARCHAR(50), sourcetype VARCHAR(30), streamurl VARCHAR(255), streamkey VARCHAR(40), youtubeposition VARCHAR(20), youtubecurrentindex VARCHAR(20), youtubeduration VARCHAR(20), youtubeplaylistcount VARCHAR(20), youtubevideoid VARCHAR(40), youtubeuuid VARCHAR(20), plot BLOB, timestampyear VARCHAR(4), timestampmonth VARCHAR(2), timestampday VARCHAR(2))')
		##pageurl, title, streamtype, live, thumb, fanart, roomid, roomslug, sourcetype, streamurl, streamkey, youtubeposition, youtubecurrentindex, youtubeduration, youtubeplaylistcount, youtubevideoid, youtubeuuid, plot, timestampyear, timestampmonth, timestampday
		
		#s.append('CREATE TABLE IF NOT EXISTS shows (url VARCHAR(255) UNIQUE, title TEXT, year VARCHAR(10), img TEXT, fanart TEXT, imdbnum TEXT, plot BLOB, timestampyear TEXT, timestampmonth TEXT, timestampday TEXT, visited BOOLEAN, isfav TEXT, fav1 BOOLEAN, fav2 BOOLEAN, fav3 BOOLEAN, fav4 BOOLEAN, showid VARCHAR(10))')
		#s.append('CREATE TABLE IF NOT EXISTS watched (url VARCHAR(255) UNIQUE, title TEXT, episode TEXT, timestampyear TEXT, timestampmonth TEXT, timestampday TEXT)')
		#s.append('CREATE TABLE IF NOT EXISTS visited (url VARCHAR(255) UNIQUE, title TEXT, episode TEXT, timestampyear TEXT, timestampmonth TEXT, timestampday TEXT, img TEXT, fanart TEXT)')
		#s.append('CREATE TABLE IF NOT EXISTS favs1 (url VARCHAR(255) UNIQUE)')
		#s.append('CREATE TABLE IF NOT EXISTS favs2 (url VARCHAR(255) UNIQUE)')
		#s.append('CREATE TABLE IF NOT EXISTS favs3 (url VARCHAR(255) UNIQUE)')
		#s.append('CREATE TABLE IF NOT EXISTS favs4 (url VARCHAR(255) UNIQUE)')
		##s.append('ALTER TABLE shows ADD showid VARCHAR(10)')
		for t in s:
			try: deb("db command",t); db.execute(t); 
			except Exception,e: debob(['Exception',e])
			except: pass
	except Exception,e: debob(['Exception',e])
	except: pass
	try: db.commit(); db.close(); 
	except Exception,e: debob(['Exception',e])
	except: pass
	addstv("init_database",CorrectValueForInitDatabase); 
def check_database():
	if not addst("init_database")==CorrectValueForInitDatabase:
		try:
			init_database(); 
		except: pass
	elif os.path.isfile(DB_DIR)==True: print "Database File Found: "+DB_DIR; 
	else: print "Unable to locate Database File"; init_database(); 
#check_database()

def do_database_test(CoMMaNDS):
	#try:
		db=orm.connect(DB_DIR); 
		for t in CoMMaNDS:
			#try:
				db.execute(t)
			#except: pass
	#except: pass
	#try:
		db.commit(); db.close(); 
	#except: pass

def do_database(CoMMaNDS):
	try:
		db=orm.connect(DB_DIR); 
		for t in CoMMaNDS:
			try:
				db.execute(t)
			except: pass
	except: pass
	try:
		db.commit(); db.close(); 
	except: pass

def do_database2(CoMMaNDS): # [ ["",(..., ..., ...)],["",""] ]
	try:
		db=orm.connect(DB_DIR); 
		for t,s in CoMMaNDS:
			try:
				db.execute(t.replace('?','%s'),s)
			except: pass
	except: pass
	try:
		db.commit(); db.close(); 
	except: pass

def get_database_all(CoMMaND):
	#try:
	db=orm.connect(DB_DIR); 
	db.execute(CoMMaND)
	results=db.execute(CoMMaND).fetchall()
	#except: pass
	try:
		#db.commit(); 
		db.close(); 
		try:
			if not result: return []
			if result==None: return []
		except: pass
		return results
	except: return []

def get_database_1st(CoMMaND):
	try:
		db=orm.connect(DB_DIR); 
		result=db.execute(CoMMaND).fetchone()
	except: pass
	try:
		#db.commit(); 
		db.close(); 
		try:
			if not result: return []
			if result==None: return []
		except: pass
		return result
	except: return []

def get_database_1st_s(CoMMaND):
	try:
		db=orm.connect(DB_DIR); 
		result=db.execute(CoMMaND).fetchone()
	except: pass
	try:
		#db.commit(); 
		db.close(); 
		try:
			if not result: return ""
			if result==None: return ""
		except: pass
		return result
	except: return ""

##### /\
### ############################################################################################################
### ############################################################################################################
try:
	try: from sqlite3 import dbapi2 as ormImgCache
	except: from pysqlite2 import dbapi2 as ormImgCache
	ImgCacheDB='sqlite'; ImgCacheDBDIR=os.path.join(xbmc.translatePath("special://database"),'Textures13.db'); 
	if os.path.isfile(ImgCacheDBDIR)==True:  ImgCacheDBDIRFound=True #print "Texture Database Found: "+ImgCacheDBDIR; 
	else: ImgCacheDBDIRFound=False #print "Unable to locate Texture Database"
except: ImgCacheDBDIRFound=False
def unCacheAnImage(url):
	if (ImgCacheDBDIRFound==True):
		if (len(str(url)) > 0) and (os.path.isfile(ImgCacheDBDIR)==True): 
			try:
				dbImgCache=ormImgCache.connect(ImgCacheDBDIR); 
				s='DELETE FROM texture WHERE url = "%s";'%str(url); #print s; 
				dbImgCache.execute(s); 
				dbImgCache.commit(); dbImgCache.close(); 
			except: pass


### ############################################################################################################
### ############################################################################################################


### ############################################################################################################
### ############################################################################################################
