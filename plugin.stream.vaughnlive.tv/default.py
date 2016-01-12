### ############################################################################################################
###	#	
### # Site: 				#		
### # Author: 			#		The Highway
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re,shutil
try: import copy
except: pass
import urllib,urllib2,xbmcaddon,xbmcplugin,xbmcgui
import common as common
from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath,_thumbArtPath)
### ############################################################################################################
### ############################################################################################################
print sys.argv
SiteName=ps('__plugin__'); SiteTag=ps('__plugin__').replace(' ',''); 
#mainSite=addst("site-domain")
#mainSite2='http://www.'+(mainSite.replace('http://',''))
mainSite =    "http://vaughnlive.tv"; mainSite2=    "https://vaughnlive.tv"; 
mainSite3="http://www.vaughnlive.tv"; mainSite4="https://www.vaughnlive.tv"; 
mainSite5="http://instagib.tv"; mainSite6="http://breakers.tv"; mainSite7="http://vapers.tv"; 
VghnCdn='http://cdn.vaughnsoft.com/vaughnsoft'
ImageSize='320' #'125'
iconSite=_artIcon
fanartSite=_artFanart
CR='[CR]'; 
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan','13':'firebrick','14':'mediumpurple'}; 
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']; 
MyGenres=['Action','Adventure','Animation','Comedy','Drama','Family','Fantasy','Thriller','Reality TV','Sport','Sci-Fi','Documentary','Mystery','Talk Show','War','History','Crime','Music','Horror']; 
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']; 
ww6='[COLOR black]@[/COLOR]'; ww7='[COLOR mediumpurple]@[/COLOR]'; 
colorA='FFFFFFFF'; colorB='FFAAAAAA'; colorC='FF777777'; 
### ############################################################################################################
### ############################################################################################################
site=addpr('site',''); section=addpr('section',''); url=addpr('url',''); sections={'series':'series','movies':'movies'}; thumbnail=addpr('img',''); fanart=addpr('fanart',''); page=addpr('page',''); 
### ############################################################################################################
### ############################################################################################################
def About(head=''+cFL(SiteName,'blueviolet')+'',m=''):
	if len(m)==0:
		m+='IRC Chat:  '+cFL('#The_Projects','blueviolet')+' @ '+cFL('irc.snoonet.org','blueviolet')
		m+=CR+'Site Name:  '+SiteName+CR+'Site Tag:  '+SiteTag+CR+'Site Domain:  '+mainSite+CR+'Site Icon:  '+iconSite+CR+'Site Fanart:  '+fanartSite
		m+=CR+'Age:  Please make sure you are of a valid age to watch the material shown.'
		m+=CR+CR+'Known Hosts for Channels:  '
		m+=CR+'* VaughnLive.tv'
		m+=CR+'* Instagib.tv'
		m+=CR+'* Vapers.tv'
		m+=CR+'* Breakers.tv'
		m+=CR+CR+'Features:  '
		m+=CR+'* Browse Channels.'
		m+=CR+'* Browse Categories via Browse Method.'
		m+=CR+'* Browse Categories via TopBar Method.'
		m+=CR+'* Launch Browser to Channel Page.'
		m+=CR+'* Launch Browser to Channel Embed Video.'
		m+=CR+'* Launch Browser to Channel Embed Chat.'
		m+=CR+'* Play RTMP Live Video Streams.'
		m+=CR+'* View Background and Profile Images of Channels/Casters.'
		#m+=CR+CR+'Notes:  '
		#m+=CR+'* '
		#m+=CR+'* '
		m+=CR+''
		#m+=CR+ps('ReferalMsg')
		m+=CR+'I can be found on [COLOR lime]#The_Projects[/COLOR] @ [COLOR red]irc.snoonet.org[/COLOR], an IRC Chat Server.'
		m+=CR+''
		m+=CR+''
		m+=CR+''
	import splash_highway as splash; splash.do_My_Splash(_addon.get_fanart(),5,False); 
	#splash.do_My_Splash(HowLong=5,resize=False); 
	#splash.do_My_Splash('http://i.imgur.com/tMKjZ6j.png',HowLong=5,resize=False); 
	String2TextBox(message=cFL(m,'cornflowerblue'),HeaderMessage=head)
	#RefreshList()
def spAfterSplit(t,ss):
	if ss in t: t=t.split(ss)[1]
	return t
def spBeforeSplit(t,ss):
	if ss in t: t=t.split(ss)[0]
	return t
def AFColoring(t): 
	if len(t)==0: return t
	elif len(t)==1: return cFL(t,colorA) #colorA)
	else: return cFL(cFL_(t,colorA),colorB) #colorA),colorB)
def wwA(t,ww): #for Watched State Display
	if   ww==7: t=ww7+t
	elif ww==6: t=ww6+t
	return t

### ############################################################################################################
### ############################################################################################################
def psgn(x,t=".png"):
	s="http://i.imgur.com/"; d=iconSite #artp('default_icon')
	try:
		return {
			'popular': 				artp('browse_popular') #d #s+""+t
			,'entertainment': artp('browse_entertainment') #d #s+""+t
			,'gaming': 				artp('browse_gaming') #d #s+""+t
			,'music': 				artp('browse_music') #d #s+""+t
			,'social': 				artp('browse_social') #artp('default_user') #d #s+""+t
			,'history 101': 	artp('history_101')
			,'browse my picks list': 			artp('list_mypicks')
			,'browse local list': 				artp('list_local')
			,'browse devs featured': 			artp('featured_dev')
			,'browse featured': 					artp('featured_site')
			,'search': 										artp('search_channels') #s+"L8Ifj8L"+t #L8Ifj8L #MTnRQJ3
			,'search user': 							artp('search_people') #s+"L8Ifj8L"+t #MTnRQJ3
			,'img_next':									artp('browse_next') #d #'http://kissanime.com/Content/images/next.png'
			,'img_prev':									artp('browse_prev') #d #'http://kissanime.com/Content/images/previous.png'
			,'next':											artp('browse_next') #d #'http://kissanime.com/Content/images/next.png'
			,'prev':											artp('browse_prev') #d #'http://kissanime.com/Content/images/previous.png'
			,'browse':										artj('Browse') #d #artp('browse')
			,'topbar':										artj('Top_Bar') #d #artp('browse')
			,'about': 										artj('About') #s+"8BLYGft"+t
			,'all': 											artj('All') #d #s+"hrWVT21"+t
			,'a': 		s+"OvFHLK2"+t
			,'b': 		s+"ezem9mn"+t
			,'c': 		s+"707ILz1"+t
			,'d': 		s+"BUT7dUz"+t
			,'e': 		s+"mzNtW2U"+t
			,'f': 		s+"11cykaC"+t
			,'g': 		s+"l0CvvHo"+t
			,'h': 		s+"VOupMGK"+t
			,'i': 		s+"ps3YPHq"+t
			,'j': 		s+"oNHwZWv"+t
			,'k': 		s+"TwHANG6"+t
			,'l': 		s+"xiuR2WX"+t
			,'m': 		s+"GDEAPud"+t
			,'n': 		s+"9FjSiMu"+t
			,'o': 		s+"TcR1pa0"+t
			,'p': 		s+"OGc4VBR"+t
			,'q': 		s+"hL9tEkx"+t
			,'r': 		s+"37NNHm8"+t
			,'s': 		s+"mFQswUE"+t
			,'t': 		s+"4DBQVrd"+t
			,'u': 		s+"qpovLUW"+t
			,'v': 		s+"bnu5ByY"+t
			,'w': 		s+"0IHoHV2"+t
			,'x': 		s+"ic81iKY"+t
			,'y': 		s+"46IlmRH"+t
			,'z': 		s+"PWUSCsE"+t
			,'0': 		s+"7an2n4W"+t # 0RJOmkw
			#,'search': 										s+"mDSHRJX"+t
			,'plugin settings': 					d #s+"K4OuZcD"+t
			,'local change log': 					d #s+"f1nvgAM"+t
			#,'last': 											s+"FelUdDz"+t
			#,'favorites': 								s+"lUAS5AU"+t
			#,'favorites 2': 							s+"EA49Lt3"+t
			#,'favorites 3': 							s+"lwJoUqT"+t
			#,'favorites 4': 							s+"Wr7GPTf"+t
			,'latest update': 						d #s+"dNCxQbg"+t
			,'completed': 								d #s+"xcqaTKI"+t
			#,'most popular': 							s+"T9LUsM2"+t
			#,'new anime': 								s+"BGZnMf5"+t
			#,'genre': 										s+"AmQHPvY"+t
			,'ongoing': 									d #s+"mBqFW3r"+t #EUak0Sg #ozEg86L
			,'anime list all': 						d #s+"t8b1hSX"+t
			,'anime list alphabet': 			d #s+"R0w0BAM"+t
			,'anime list latest update': 	d #s+"XG0LGQH"+t
			,'anime list newest': 				d #s+"eWAeuLG"+t
			,'anime list popularity': 		d #s+"eTrguP1"+t
			,'urlresolver settings': 			d #s+"PlROfSs"+t
			,'online bookmarks': 					d #s+"68ih1sx"+t
			#,'alphabetical': 							s+"sddCXQo"+t
			,'genre select': 							d #s+"MhNenb6"+t
#			,'': 								s+""+t
#			,'': 								s+""+t
			,'alphabetical': 							d #s+"aLKvpQD"+t
			,'favorites': 								d #s+"mVxogXL"+t #
			,'favorites 1': 							d #s+"cyDyVuh"+t #
			,'favorites 2': 							d #s+"GxH6BbM"+t #yRtrel2
			,'favorites 3': 							d #s+"Z9zKGJU"+t #
			,'favorites 4': 							d #s+"ovjBVu3"+t #
			,'favorites 5': 							d #s+"n8LUh2R"+t #
			,'favorites 6': 							d #s+"qN6FEit"+t #
			,'favorites 7': 							d #s+"3yQYXNh"+t #
			,'genre': 										d #s+"ObKUcJT"+t #XEIr4Cz
			,'icon': 											d #s+"VshtskV"+t
			,'fanart': 										d #s+"OSv7S2u"+t
			,'last': 											d #s+"3g6S9UH"+t
			,'latest episodes': 					d #s+"Skoe3Fm"+t #r19ycox
			,'latest updates': 						d #s+"E86Rnq5"+t
			,'most popular': 							d #s+"DzFexnz"+t #N69lo3G
			,'new anime': 								d #s+"wZN1olE"+t
			,'random anime': 							d #s+"Rjag7b3"+t
			,'_': 												d #s+"bGMWifZ"+t
			,'anime 2013': 								d #s+"4SgqERs"+t
			,'anime 2014': 								d #s+"ijvRzvJ"+t
			,'anime 2015': 								d #s+"IYPai5I"+t
			,'anime 2016': 								d #s+"UqAYilt"+t
			,'anime list': 								d #s+"NTPFfwQ"+t
			,'a-z': 											d #s+"Br4ltnl"+t
			,'hot this season': 					d #s+"KcymQWL"+t
			,'latest animes': 						d #s+"mDFKTFN"+t
			,'movies': 										d #s+"hDYdtIr"+t
			,'random': 										d #s+"5uYkgTx"+t
			,'today': 										d #s+"GPxwlE8"+t
			,'tomorrow': 									d #s+"YX2EKk8"+t
			,'yesterday': 								d #s+"shqgyif"+t
			,'irc': 											s+"7YS28Z5"+".jpg"
			,'forum': 										s+"kZY1JNd"+".png"
			,'forumfa': 									s+"1FWfZPC"+".png"
			,'reddit': 										s+"WImf8TF"+".png"
			,'redditfa': 									s+"ZcAXuNf"+".jpg"
#			,'': 								s+""+t
#			,'': 								s+""+t
#			,'': 								s+""+t
			###
#			,'': 								s+""+t
#			,'': 								s+""+t
#			,'': 								s+""+t
# KissAnimeGenres
# http://imgur.com/a/rws19/all
# http://imgur.com/a/rws19#Q12cars
# http://imgur.com/a/rws19
		}[x.lower()]
	except: 
		print 'failed to find graphc for %s' % (x); 
		return d
		#return ''
### ############################################################################################################
### ############################################################################################################
def getThumb(Id,PathA='vaughn',PathB='profiles',Ext='.jpg',FetchLoc='live',TimeStamp='0'):			
	if len(str(TimeStamp))==0: TimeStamp='0'
	if tfalse(addst('thumbnail-type'))==True: return "http://thumbnails.vaughnsoft.com/%s/fetch/%s/%s.png"%(str(TimeStamp),FetchLoc,Id)
	else: return "%s/%s/img_%s/%s_%s%s"%(VghnCdn,PathA,PathB,Id,ImageSize,Ext)
def getBg(Id,PathA='vaughnlive',PathB='backgrounds',Ext='.jpg'):	return "%s/%s/img_%s/%s%s"   %(VghnCdn,PathA,PathB,Id          ,Ext)
def rcPile(strRegex,strSource,intFind='',strDefault=''):
	try:
		if len(str(strRegex))==0:
			if len(str(intFind))==0: return strSource
			else: return strSource[int(intFind)]
		else: 
			if len(str(intFind))==0: return re.compile(strRegex).findall(strSource)
			else: return re.compile(strRegex).findall(strSource)[int(intFind)]
	except: return strDefault
def decrypt_vaughnlive(encrypted,retVal="",strDefault=''):
	try:
		if ':' in encrypted:
			for val in encrypted.split(':'): 
				#c1=val.replace("0m0",""); c2=int(c1); c3=c2/84; c4=c3/5; retVal+=chr(c4)
				retVal+=chr(int(val.replace("0m0",""))/84/5)
			return retVal
		else: return encrypted.replace("0m0","")
	except: return strDefault
def grbPlyrCORE(): ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	PlayerMethod=addst("core-player"); 
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	return PlayerMeth
def grbPlyr(): return xbmc.Player(grbPlyrCORE()) #return xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
def PlayLiveStream(pageUrl='',Name='',Thumb='',Channel='',roomId='',roomSlug='',plot='',liVe='',streamUrl='',streamkey='',youtubekey='',sourcetype='show'):
	#mainSite5="http://instagib.tv"; mainSite6="http://breakers.tv"; mainSite7="http://vapers.tv"; 
	url=''; print "--DO A PLAYER SPLIT HERE--"; debob(['pageUrl',pageUrl,'Name',Name,'Thumb',Thumb,'roomId',roomId,'roomSlug',roomSlug,'plot',plot,'liVe',liVe,'streamUrl',streamUrl]); fimg=''; 
	tempParams=_addon.queries; debob(['tempParams',tempParams]); 
	play=grbPlyr()
	if len(streamUrl) > 10: url=streamUrl
	else: 
		if pageUrl.startswith('/'): pageUrl=mainSite+pageUrl
		deb('pageUrl',pageUrl); 
		#if len(Channel) > 0: pageUrl=mainSite+"/embed/video/%s" % Channel
		if (len(pageUrl)==0) and (len(Channel) > 0): pageUrl=mainSite+"/%s" % Channel
		elif (not '://' in pageUrl): pageUrl=mainSite+pageUrl
		html=messupText(nolines(nURL(pageUrl)),True,True); deb('length of html',str(len(html))); #debob(html); 
		if len(Channel)==0: Channel=rcPile('vsVars\d+.k2 = "(.+?)";',html,0)
		try: 		SiteDomain=pageUrl.split('://')[1].split('/')[0]
		except: SiteDomain='vaughnlive.tv'
		## VaughnLive	## vaughnlive.tv
		## Vapers			## vapers.tv
		## Breakers		## breakers.tv
		## Gamers			## instagib.tv
		debob(['SiteDomain',SiteDomain]); 
		liVe=rcPile('vsVars\d+.k1 = "(.+?)";',html,0); debob(['liVe',liVe]); 
		TimeStampA=rcPile('vsVars\d+.t = "(\d+)";',html,0); debob(['TimeStampA',TimeStampA]); 
		vidServers=rcPile('(\d+\.\d+\.\d+\.\d+\:443)',html); debob(['vidServers',vidServers]); 
		SwfPath=rcPile('swfobject.embedSWF\("(/\d+/swf/[0-9A-Za-z]+\.swf)"',html,0); debob(['SwfPath',SwfPath]); 
		ServNum=int(addst("server-number"))
		if ServNum > len(vidServers): ServNum=0-1
		vidServer=rcPile('',vidServers,ServNum); 
		#vidServer=rcPile('',vidServers,0); 
		if len(vidServer)==0: vidServer='live.%s:443'%SiteDomain; 
		debob(['vidServer',vidServer]); 
		TOK=''; HaSH=''; 
		HaSHa=rcPile('vsVars\d\d\d\d\d\d\d\d\d\d\d\.[0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z]+\s+=\s+"(.+?)";',html,0); 
		HaSHb=rcPile(  'vsVars\d\d\d\d\d\d\d\d\d\d\.[0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z][0-9A-Za-z]+\s+=\s+"(.+?)";',html,0); 
		HaSHaa=decrypt_vaughnlive(HaSHa); debob(['HaSHa',HaSHa,HaSHaa]); 
		HaSHbb=decrypt_vaughnlive(HaSHb); debob(['HaSHb',HaSHb,HaSHbb]); 
		HaSH=HaSHbb; LiveTag='live'; LiveStatus='true'; TimeOut='30'; AppStatus='live'; 
		 
		TimeOut=str(addst('DefaultTimeOut','30'))
		if   'instagib.' in SiteDomain: LiveTag='instagib'; DomainTag='instagib'
		elif 'vapers.'   in SiteDomain: LiveTag='vapers';   DomainTag='vtv'
		elif 'breakers.' in SiteDomain: LiveTag='breakers'; DomainTag='btv'
		else: LiveTag='live'; DomainTag='live'
		TheReferredPage="http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true"%(SiteDomain,Channel); 
		if LiveTag=='instagib' or LiveTag=='vapers' or LiveTag=='breakers':
			TheReferredPage="http://%s/%s"%(SiteDomain,Channel); 
		## \/ Only Plays for ~7seconds.
		#url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s%s live=%s timeout=%s pageUrl=%s %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,SwfPath,LiveStatus,TimeOut,TheReferredPage,TOK); 
		
		##rtmp://50.7.78.50:443/live?0n0rpp04y0tWUptmHIhkPENXkazBXlSK0dz Playpath=live_docbrown1 swfUrl=http://vaughnlive.tv/4294291713/swf/VaughnSoftPlayer.swf live=true timeout=50 pageUrl=http://vaughnlive.tv/embed/video/docbrown1?viewers=true&watermark=left&autoplay=true  Conn=S:OK --live
		##wowz://50.97.232.189:443/live/_definst_/live_docbrown1
		## \/ Only Plays for ~7seconds.
		#url="rtmp://%s/live/_definst_?%s Playpath=%s_%s swfUrl=http://%s%s live=%s timeout=%s pageUrl=%s %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,SwfPath,LiveStatus,TimeOut,TheReferredPage,TOK); 
		
		#LiveStatus='false'; 
		#url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s%s live=%s timeout=%s pageUrl=%s %s Conn=S:OK" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,SwfPath,LiveStatus,TimeOut,TheReferredPage,TOK); 
		
		#url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s%s live=%s timeout=%s pageUrl=%s %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,SwfPath,LiveStatus,TimeOut,TheReferredPage,TOK); 
		
		#url="http://mvn.vaughnsoft.net/video/edge/{domain}_{channel}" ## << From chrippa's LiveStreamer. ##
		mvnkeyURL="http://mvn.vaughnsoft.net/video/edge/%s_%s"%(DomainTag,Channel); debob({'mvnkeyURL':mvnkeyURL}); 
		mvnkeyHTML=messupText(nolines(nURL(mvnkeyURL)),True,True); debob({'mvnkeyHTML':mvnkeyHTML}); 
		try:
			mvnkeyServerAndPort,mvnkeySERVER,mvnkeyPORT,mvnkeyKEY=re.compile('((\d+\.\d+\.\d+\.\d+):(\d+));:mvnkey-([0-9A-Za-z]+)').findall(mvnkeyHTML)[0]
		except: mvnkeyServerAndPort=vidServer; mvnkeySERVER=''; mvnkeyPORT=''; mvnkeyKEY=''; 
		
		
		url="rtmp://%s/live app=live?%s swfVfy=http://%s%s pageUrl=%s live=%s playpath=%s_%s"%(mvnkeyServerAndPort,mvnkeyKEY,SiteDomain,SwfPath,TheReferredPage,LiveStatus,DomainTag,Channel)
		
		#url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s%s live=%s timeout=%s pageUrl=%s %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,SwfPath,LiveStatus,TimeOut,TheReferredPage,TOK); 
		#url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s%s live=%s timeout=%s pageUrl=http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,SwfPath,LiveStatus,TimeOut,SiteDomain,Channel,TOK); 
		#url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s/4241760954/swf/VaughnSoftPlayer.swf live=%s timeout=%s pageUrl=http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,LiveStatus,TimeOut,SiteDomain,Channel,TOK); 
		##url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s/800021294/swf/VaughnSoftPlayer.swf live=%s timeout=%s pageUrl=http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,LiveStatus,TimeOut,SiteDomain,Channel,TOK); 
		##url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s/800021294/swf/VaughnSoftPlayer.swf live=%s timeout=%s pageUrl=http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true %s" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,LiveStatus,TimeOut,SiteDomain,Channel,TOK); 
		##url="rtmp://%s/%s/_definst_/%s.> live=%s timeout=%s" % (vidServer,LiveTag,Channel,LiveStatus,TimeOut); 
		##url="rtmp://%s/%s/_definst_/%s live=%s timeout=%s %s Conn=S:OK --live" % (vidServer,LiveTag,Channel,LiveStatus,TimeOut,TOK); 
		##url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s/800021294/swf/VaughnSoftPlayer.swf live=%s timeout=%s pageUrl=http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true %s %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,LiveStatus,TimeOut,SiteDomain,Channel,TOK,'fps=25'); 
		##url="rtmp://%s/live?%s Playpath=%s_%s swfUrl=http://%s/800021294/swf/VaughnSoftPlayer.swf live=%s timeout=%s app=%s pageUrl=http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,LiveStatus,TimeOut,AppStatus,SiteDomain,Channel,TOK); 
		##url="rtmp://%s/live?%s playpath=%s_%s swfUrl=http://%s/800021294/swf/VaughnSoftPlayer.swf live=1 timeout=30 pageUrl=http://%s/embed/video/%s?viewers=true&watermark=left&autoplay=true %s Conn=S:OK --live" % (vidServer,HaSH,LiveTag,Channel,SiteDomain,SiteDomain,Channel,TOK); 
		## ### ## 
		try:    Name=re.compile('<span id="videoTitle">(.+?)</span>').findall(html)[0]
		except: Name='Unknown'
		if len(Thumb)==0: 
			if len(roomId)==0: Thumb=iconSite
			else: Thumb=getThumb(roomId,FetchLoc=LiveTag,TimeStamp=TimeStampA)
		if len(fimg)==0: 
			if len(roomId)==0: 
				try: 		fimg='http://'+re.compile('div.theMain { background-image:url\(//(cdn.vaughnsoft.com/vaughnsoft/vaughnlive/background/[0-9A-Za-z]+_[0-9A-Za-z]+_[0-9A-Za-z]+.jpg)\);').findall(html)[0]
				except: fimg=fanartSite
			else: 
				fimg=getBg(roomId)
				#try: 		
				#	fimg='http://'+re.compile('div.theMain { background-image:url\(//(cdn.vaughnsoft.com/vaughnsoft/vaughnlive/background/[0-9A-Za-z]+_[0-9A-Za-z]+_[0-9A-Za-z]+.jpg)\);').findall(html)[0]
				#	fimg=getBg(roomId)
				#except: fimg=fanartSite
		## ### ## 
	## ### ## 
	debob(",['pars', {'streamurl': '%s', 'roomslug': '%s', 'fimg': '%s', 'img': '%s', 'title': '%s', 'url': '%s', 'type': '%s', 'live': '%s', 'mode': 'PlayStreamUP', 'roomid': '%s', 'sourcetype': '%s'}, " % (str(url),str(roomSlug),str(fimg),str(Thumb),str(Name).replace('[COLOR FFAAAAAA] [[COLOR FF777777]Live[/COLOR]][/COLOR]',''),str(pageUrl),str(addpr('type','')),str(liVe),str(roomId),str(sourcetype))); 
	infoLabels={"Studio":liVe,"Title":'%s [%s]: %s'%(Channel,liVe,Name),"cover_url":Thumb,"background_url":fimg,'plot':plot}; 
	li=xbmcgui.ListItem(Name,iconImage=iconSite,thumbnailImage=Thumb); li.setInfo(type="Video",infoLabels=infoLabels); li.setProperty('IsPlayable','true'); li.setProperty('fanart_image',fimg); 
	if tfalse(addst("playback_eod"))==True: eod()
	if tfalse(addst("playback_urlresolve"))==True:
		try: _addon.resolve_url(url)
		except: pass
	if tfalse(addst("playback_urlonly"))==True:
		try: play.play(url)
		except: pass
	else:
		try: play.play(url,li,False,0)
		except:
			try: play.play(url)
			except: pass
	### ### ## 

def MenuHistory101():
	tab1rows=ps('db channels tags0c'); 
	try:
		r=get_database_all('SELECT %s FROM channels' % (tab1rows)); 
	except: pass
	if r:
		if len(r) > 0:
			iC=len(r); i=0; 
			HistoryCountLimit="20"; #HistoryCountLimit=addst("history101-count"); 
			for k in r[::-1]:
				try:
					debob(['k',k]); 
					cMI=[]; pars={}; labs={}; pageurl=''; url=''; title=''; liVe=''; plot=''; streamtype=''; roomslug=''; roomid=''; img=iconSite; fanart=fanartSite; 
					try: pageurl=urllib.unquote_plus(str(k[0])); 
					except: pass
					try: title=urllib.unquote_plus(str(k[1])); 
					except: pass
					try: streamtype=urllib.unquote_plus(str(k[2])); 
					except: pass
					try: img=urllib.unquote_plus(str(k[4])); 
					except: pass
					try: fanart=urllib.unquote_plus(str(k[5])); 
					except: pass
					try: roomid=urllib.unquote_plus(str(k[6])); 
					except: pass
					try: roomslug=urllib.unquote_plus(str(k[7])); 
					except: pass
					try: url=urllib.unquote_plus(str(k[9])); debob(['url',url]); 
					except: pass
					try: labs[u'plot']=urllib.unquote_plus(str(k[17])); 
					except: labs[u'plot']=''
					labs[u'title']=cFL(title,colorA); 
					if (len(liVe) > 0) and (not str(liVe).lower()=='none'): labs[u'title']=cFL(title+cFL(" ["+cFL(liVe,colorC)+"]",colorB),colorA); 
					pars={'streamurl':str(url),'roomslug':str(roomslug),'fimg':str(fanart),'img':str(img),'title':str(title),'url':str(pageurl),'type':'','live':'History','mode':'PlayStreamUP','roomid':str(roomid),'sourcetype':''}; 
					if (len(url) > 0) and (not str(url).lower()=='none'):
						try: _addon.add_directory(pars,labs,is_folder=False,fanart=fanart,img=img,contextmenu_items=cMI,total_items=iC,context_replace=False); i+=1; 
						except: pass
					if not (HistoryCountLimit=="ALL") and (len(HistoryCountLimit) > 0):
						if i > (int(HistoryCountLimit)-1): break
				except: pass
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()

def MenuListChannels(Url,Page='',TyPE='js',idList='[]',csrfToken='',MeTHoD='re.compile'):
	debob(['Url',Url,'TyPE',TyPE])
	if len(Url)==0: debob("No url found."); eod(); return
	if (not mainSite in Url) and (not mainSite2 in Url) and (not mainSite3 in Url) and (not mainSite4 in Url): Url=mainSite+Url
	deb('Url',Url); html=messupText(nolines(nURL(Url,headers={'Referer':mainSite},cookie_file=CookFile,load_cookie=True)),True,True); deb('length of html',str(len(html))); #debob(html); 
	if len(html)==0: debob("No html found."); eod(); return
	## ### ## 
	if   (mainSite+"/app/topbar.php?s=") in Url: s='<div\s+class="topbar_img">\s*<a\s+href="(\D+://(?:www.)?(?:/|vapers.tv/|breakers.tv/|vaughnlive.tv/|instagib.tv/)?)(.*?)"\s*>(())\s*<img\s+name="mvnPicTopBar_.*?"\s+width="\d*"\s+height="\d*" border="\d*"\s+onerror="mvnImages.profileError\(\'mvnPicTopBar_[0-9A-Za-z_\-]+\',\'[0-9A-Za-z_\-]+\'\);"\s+class="[0-9A-Za-z_\-]*"\s+alt="[0-9A-Za-z_\-]+(?: - \D+.)?"\s+title="[0-9A-Za-z_\-]+(?: - \D+.)?"\s*/>\s*</a>\s*</div'; #MeTHoD='split'
	elif (mainSite+"/browse/") in Url: 
		s='<a href="((?:http://)?(?:/|vapers.tv/|breakers.tv/|vaughnlive.tv/|instagib.tv/)?)(.+?)" target="_top"><img src="//(thumbnails.vaughnsoft.com/(\d+)/fetch/\D+/.+?.png)" class"browseThumb" width="\d*" height="\d*"\s*/></a>'; 
		
	else: return
	html=html.replace('</div>','</div\n\r\a>'); #debob(html); 
	if (MeTHoD=='split') and ('</MVN>' in html):
		debob(['MeTHoD',MeTHoD,'"</MVN>" is in HTML.']); 
		matches=html.split('</MVN>')[-1].split(',')
	elif (MeTHoD=='re.compile') or (not '</MVN>' in html): #MeTHoD=='re.compile':
		debob(['MeTHoD',MeTHoD,'"</MVN>" is not in HTML.']); 
		try: matches=re.compile(s).findall(html); deb('# of matches found',str(len(matches))); #debob(matches); 
		except: matches=[]; debob('No matches were found.'); 
	else: matches=[]; debob('No matching method was found.'); 
	## ### ## 
	if len(matches) > 0:
		iC=len(matches); 
		if MeTHoD=='re.compile':
			if tfalse(addst('sort-by-name'))==True: matches=sorted(matches,key=lambda i: i[1],reverse=False)
			try:
			#	os.remove(_thumbArtPath)
				if isPath(_thumbArtPath)==True:
					shutil.rmtree(_thumbArtPath)
			except: pass
			for (PrefixD,match,img,iTS) in matches: #(img,url,name,genres)
				labs={}; cMI=[]; is_folder=False; plot=''; name=match.replace('_',' '); labs[u'plot']=plot; LocImgName=''; 
				img=getThumb(match,FetchLoc='live',TimeStamp=iTS)
				fimg=getBg(match)
				#debob({'img':img,'fimg':fimg})
				if tfalse(addst('thumbnail-type'))==True:
						ThumbFile=match+'.png'
						DownloadThisSilently(img,ThumbFile,_thumbArtPath,useResolver=False)
						ThumbFileWithPath=thumbart(ThumbFile)
						if os.path.isfile(ThumbFileWithPath)==True:
							img=''+ThumbFileWithPath
							unCacheAnImage(img)
				#unCacheAnImage(img)
				if '://' in PrefixD:url=PrefixD+"%s"%match; urlPage=PrefixD+"%s" % match; urlEmbedVideo=PrefixD+"embed/video/%s"%match; urlEmbedChat=PrefixD+"embed/chat/%s"%match; 
				else: url=mainSite+"/%s"%match; urlPage=mainSite+"/%s" % match; urlEmbedVideo=mainSite+"/embed/video/%s"%match; urlEmbedChat=mainSite+"/embed/chat/%s"%match; 
				labs[u'title']=cFL(name,colorA); #labs[u'title']=cFL(name+cFL(" ["+cFL(liVe,colorC)+"]",colorB),colorA); 
				pars={'url':url,'title':name,'fimg':fimg,'img':img,'mode':'PlayLiveStream','channel':match,'site':site,'section':section,'sourcetype':'auto'}; 
				Clabs={'title':name,'year':'','url':url,'commonid':'','img':img,'fanart':fimg,'plot':labs[u'plot'],'todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}; 
				try: cMI=ContextMenu_LiveStreams(Clabs); 
				except: pass
				try: debob(['pars',pars,'labs',labs]); 
				except: pass
				cMI.append(('Visit Page', 'XBMC.RunPlugin(%s)'%_addon.build_plugin_url({'mode':'BrowseUrl','url':urlPage})))
				cMI.append(('Visit Video','XBMC.RunPlugin(%s)'%_addon.build_plugin_url({'mode':'BrowseUrl','url':urlEmbedVideo})))
				cMI.append(('Visit Chat', 'XBMC.RunPlugin(%s)'%_addon.build_plugin_url({'mode':'BrowseUrl','url':urlEmbedChat})))
				try: _addon.add_directory(pars,labs,is_folder=is_folder,fanart=fimg,img=img,contextmenu_items=cMI,total_items=iC,context_replace=False)
				except: pass
		elif MeTHoD=='split':
			if tfalse(addst('sort-by-name'))==True: matches=matches.sort() #matches=sorted(matches,key=lambda i: i[1],reverse=False)
			for (match) in matches: #(img,url,name,genres)
				if len(match.strip()) > 0:
					PrefixD=''; img=''; iTS=''
					labs={}; cMI=[]; is_folder=False; plot=''; name=match.replace('_',' '); labs[u'plot']=plot; LocImgName=''; 
					img=getThumb(match,FetchLoc='live',TimeStamp='0')
					fimg=getBg(match)
					if '://' in PrefixD:url=PrefixD+"%s" % match; urlPage=PrefixD+"%s" % match; urlEmbedVideo=PrefixD+"embed/video/%s" % match; urlEmbedChat=PrefixD+"embed/chat/%s" % match; 
					else: url=mainSite+"/%s" % match; urlPage=mainSite+"/%s" % match; urlEmbedVideo=mainSite+"/embed/video/%s" % match; urlEmbedChat=mainSite+"/embed/chat/%s" % match; 
					labs[u'title']=cFL(name,colorA); #labs[u'title']=cFL(name+cFL(" ["+cFL(liVe,colorC)+"]",colorB),colorA); 
					pars={'url':url,'title':name,'fimg':fimg,'img':img,'mode':'PlayLiveStream','channel':match,'site':site,'section':section,'sourcetype':'auto'}; 
					Clabs={'title':name,'year':'','url':url,'commonid':'','img':img,'fanart':fimg,'plot':labs[u'plot'],'todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}; 
					try: cMI=ContextMenu_LiveStreams(Clabs); 
					except: pass
					try: debob(['pars',pars,'labs',labs]); 
					except: pass
					cMI.append(('Visit Page', 'XBMC.RunPlugin(%s)'%_addon.build_plugin_url({'mode':'BrowseUrl','url':urlPage})))
					cMI.append(('Visit Video','XBMC.RunPlugin(%s)'%_addon.build_plugin_url({'mode':'BrowseUrl','url':urlEmbedVideo})))
					cMI.append(('Visit Chat', 'XBMC.RunPlugin(%s)'%_addon.build_plugin_url({'mode':'BrowseUrl','url':urlEmbedChat})))
					try: _addon.add_directory(pars,labs,is_folder=is_folder,fanart=fimg,img=img,contextmenu_items=cMI,total_items=iC,context_replace=False)
					except: pass
	#		## ### ## 
	#		#if is_folder==False:
	#		#	sDB=[]; 
	#		#	#'pageurl, title, streamtype, live, thumb, fanart, roomid, roomslug, sourcetype, streamurl, streamkey, 
	#		#	#youtubeposition, youtubecurrentindex, youtubeduration, youtubeplaylistcount, youtubevideoid, youtubeuuid, 
	#		#	#plot, timestampyear, timestampmonth, timestampday'
	#		#	#'"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"'
	#		#	if url.startswith('/'): url=mainSite2+url
	#		#	GroupB=(  urllib.quote_plus(str(url)),urllib.quote_plus(str(name)),urllib.quote_plus(str(liVe)),urllib.quote_plus(str(img)),urllib.quote_plus(str(roomId)),urllib.quote_plus(str(roomSlug)),urllib.quote_plus(str(plot)),str(datetime.date.today().year),str(datetime.date.today().month),str(datetime.date.today().day)  )
	#		#	#sDB.append( 'INSERT OR REPLACE INTO channels ('+ps('db channels tags1a')+') VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % GroupB )
	#		#	sDB.append( 'INSERT INTO channels ('+ps('db channels tags1a')+') VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % GroupB )
	#		#	debob(sDB); 
	#		#	do_database(sDB); 
	#		#	#do_database_test(sDB); 
	#		## ### ## 
	#NextPage=str(int(page)+1); 
	#if (("page="+NextPage) in html) and (not TyPE=='js|featured'):
	#	_addon.add_directory({'mode':'ListShows','site':site,'url':Url,'page':NextPage,'type':str(TyPE),'idlist':str(ListOfIds),'csrfToken':csrfToken},{'title':cFL('>> Next %s' % cFL(NextPage,colorA),colorB)},is_folder=True,fanart=fanartSite,img=psgn('next'))
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()
def Fav_List(site='',section='',subfav=''):
	debob(['test1',site,section,subfav]); 
	favs=fav__COMMON__list_fetcher(site=site,section=section,subfav=subfav); 
	ItemCount=len(favs); 
	debob('test2 - '+str(ItemCount)); 
	if len(favs)==0: myNote('Favorites','None Found'); eod(); return
	debob(favs); 
	favs=sorted(favs,key=lambda item: (item[0],item[1]),reverse=False); 
	for (_name,_year,_img,_fanart,_Country,_Url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2) in favs:
		if _img > 0: img=_img
		else: img=iconSite
		if _fanart > 0: fimg=_fanart
		else: fimg=fanartSite
		debob('_ToDoParams'); debob(_ToDoParams)
		pars=_addon.parse_query(_ToDoParams)
		pars[u'fimg']=_fanart; pars[u'img']=_img; 
		#if len(_commonID) > 0: pars['imdb_id']=_commonID
		debob('pars'); debob(pars)
		_title=AFColoring(_name)
		if (len(_year) > 0) and (not _year=='0000'): _title+=cFL('  ('+cFL(_year,'mediumpurple')+')',colorA)
		if len(_Country) > 0: _title+=cFL('  ['+cFL(_Country,'mediumpurple')+']',colorA)
		wwT=_name+" ~~ "; 
		try:
			if visited_check2(wwT)==True: ww=7
			else: ww=6
		except: ww=6
		#try:
		if ww > 1:
			contextLabs={'title':_name,'year':_year,'img':_img,'fanart':_fanart,'country':_Country,'url':_Url,'plot':_plot,'genres':_Genres,'site':_site,'subfav':_subfav,'section':_section,'todoparams':_ToDoParams,'commonid':_commonID,'commonid2':_commonID2}
			##contextLabs={'title':_name,'year':'0000','url':_url,'img':img,'fanart':fimg,'DateAdded':'','todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}
			contextMenuItems=ContextMenu_Favorites(contextLabs)
			contextMenuItems.append( ('Empty List','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'cFavoritesEmpty','site':site,'section':section,'subfav':subfav}) ) )
			#contextMenuItems=[]
			_title=wwA(_title,ww); 
			_addon.add_directory(pars,{'title':_title,'plot':_plot},is_folder=True,fanart=fimg,img=img,total_items=ItemCount,contextmenu_items=contextMenuItems)
		#except: pass
		#
	#
	if 'movie' in section.lower(): content='movies'
	else: content='tvshows'
	set_view(content,view_mode=int(addst('tvshows-view'))); eod()
### ############################################################################################################
### ############################################################################################################
def DoSearch_Post(title='',Url='/search/results.php'):
	if len(Url)==0: return
	if mainSite not in Url: Url=mainSite+Url; 
	if len(title)==0: title=showkeyboard(txtMessage=title,txtHeader="Search:  ("+site+")")
	if (title=='') or (title=='none') or (title==None) or (title==False): return
	#deb('Searching for',title); title=title.replace('+','%2B').replace('&','%26').replace('?','%3F').replace(':','%3A').replace(',','%2C').replace('/','%2F').replace('=','%3D').replace('@','%40').replace(' ','+'); 
	deb('Searching for',title); #MenuListChannels( Url+( title.replace(' ','+') ) ); 
	deb('Url',Url); html=messupText(nolines(nURL(Url,method='post',form_data={'search':title,'page':'','hidden_page':'','valider':'GO'})),True,True); deb('length of html',str(len(html))); #debob(html); 
	if len(html)==0: return
	ListShowsH(Url,html)
	##
def DoSearch(title='',Url='/search/'):
	if len(Url)==0: return
	if mainSite not in Url: Url=mainSite+Url; 
	if len(title)==0: title=showkeyboard(txtMessage=title,txtHeader="Search:  ("+site+")")
	if (title=='') or (title=='none') or (title==None) or (title==False): return
	deb('Searching for',title); title=title.replace('+','%2B').replace('&','%26').replace('?','%3F').replace(':','%3A').replace(',','%2C').replace('/','%2F').replace('=','%3D').replace('@','%40').replace(' ','%20'); 
	deb('Searching for',title); 
	##
	if ('_s_' in Url) or ('%s' in Url): Url=Url.replace('_s_','%s'); doUrl=Url % ( title.replace(' ','%20') )
	else: doUrl=Url + ( title.replace(' ','%20') )
	MenuListChannels( doUrl ,'','html'  ); 
	##
def MenuSpecial(url):
	try: 
		if not '://' in url: html=common._OpenFile(TPapp(url))
		else: html=nURL(url)
		html=html.replace('\n','').replace('\r','').replace('\a','').replace('\t',''); data=eval(html); 
	except: data=[]
	iC=len(data); 
	if iC > 0:
		for (tag1,pars,tag2,labs) in data:
			try: img=pars['img'].replace('https://','http://'); 
			except: 
				try: img=labs['img'].replace('https://','http://'); 
				except: img=iconSite
			try: fimg=pars['fimg'].replace('https://','http://'); 
			except: 
				try: fimg=labs['fimg']; 
				except: fimg=fanartSite
			img=img.replace('https://','http://'); fimg=fimg.replace('https://','http://'); debob([tag1,pars,tag2,labs]); 
			if  img.lower()=='[icon]':    img=  iconSite
			if fimg.lower()=='[fanart]': fimg=fanartSite
			try: _addon.add_directory(pars,labs,is_folder=False,fanart=fimg,img=img,total_items=iC,context_replace=False)
			except: pass
	#set_view('list',view_mode=addst('default-view')); eod()
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()
	##
def MenuDevFeatured(data=[]):
	#data.append(['pars',{},'labs',{u'plot':'',u'title':''}])
	#data.append()
	iC=len(data)
	for (tag1,pars,tag2,labs) in data:
		img=pars['img']; fimg=pars['fimg']; #debob(['pars',pars,'labs',labs]); 
		try: _addon.add_directory(pars,labs,is_folder=False,fanart=fimg,img=img,total_items=iC,context_replace=False)
		except: pass
	#set_view('list',view_mode=addst('default-view')); eod()
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()
	##
def MenuBrowse_FetchCats(Url='/browse',zz=[],d=[]):
	if (not '//' in Url) and (not '://' in Url) and (not mainSite in Url) and (not mainSite2 in Url) and (not mainSite3 in Url) and (not mainSite4 in Url): Url=mainSite+Url
	if ('//' in Url) and (not '://' in Url): Url='http:'+Url
	html=messupText(nolines(nURL(Url,headers={'Referer':mainSite})),True,True); deb('length of html',str(len(html))); #debob(html); 
	if len(html)==0: debob("No html found."); return d
	zz=rcPile('<div class="browseTab browseTabAccent(?:Selected)?" id="browseBtn[0-9A-Za-z]+" onclick="Browse\.[0-9A-Za-z]+\(\);"><img src="(/img/cat_.+?_white.png)" class="cat_img"/>\s*(.+?)\s*</div',html.replace('</div>','</div\n\r\a>'),'',[])
	return zz
def MenusBrowser(Url='/browse',zz=[],NewMode='BrowseCat3'):
	#zz=MenuBrowse_FetchCats(Url)
	zz.append("Misc"); zz.append("People"); zz.append("Nature"); zz.append("Creative"); zz.append("Music Cafe"); zz.append("News & Tech"); zz.append("Lifestyles"); zz.append("Espanol"); 
	zz.append("Vapers"); zz.append("Breakers"); zz.append("Gamers"); 
	#_addon.add_directory({'mode':NewMode,'site':site,'cat':'','type':'php'},{'title':AFColoring('All')},is_folder=True,fanart=fanartSite,img=(mainSite+'/img/cat_all_white.png'))
	_addon.add_directory({'mode':NewMode,'site':site,'cat':'','type':'php'},{'title':AFColoring('All')},is_folder=True,fanart=fanartSite,img=artj('All'))
	for z in zz: 
		nonTitle=z.lower().replace(' ','').replace('&',''); 
		catName=nonTitle.replace('musiccafe3','music_cafe').replace('newstech','news_tech'); 
		pars={'mode':'BrowseCat3','site':site,'cat':catName,'type':'php'}; 
		img=(mainSite+'/img/cat_%s_white.png'%nonTitle.replace('musiccafe','music')); #img=(mainSite+'/img/cat_%s.png' % nonTitle)
		img=artj(nonTitle)
		_addon.add_directory(pars,{'title':AFColoring(z)},is_folder=True,fanart=fanartSite,img=img); #img=psgn('cat '+z.lower())); 
	set_view('list',view_mode=addst('default-view')); eod()
def MenuBrowse(Url='/browse',zz=[],NewMode='BrowseCat3'): MenusBrowser(Url,zz,NewMode)
def MenuTopBar(Url='/app/topbar.php?s=vl',zz=[],NewMode='BrowseCat'): MenusBrowser(Url,zz,NewMode)

def MenuSection():
	#common.check_database() #Checks rather the Database needs initialized or updated.
	##import splash_highway as splash; #splash.do_My_Splash(_addon.get_fanart(),2,False); 
	##splash.do_My_Splash(HowLong=5,resize=False); 
	SpecialCODE=addst('special-code',''); LocalLists=[]; 
	
	try: nURL(mainSite,cookie_file=CookFile,save_cookie=True)
	except: deb("Error","Couldn't save cookie file."); pass
	
	_addon.add_directory({'mode':'MenuTopBar','site':site},{'title':AFColoring('Top Bar')},is_folder=True,fanart=fanartSite,img=psgn('topbar'))
	_addon.add_directory({'mode':'MenuBrowse','site':site},{'title':AFColoring('Browse')},is_folder=True,fanart=fanartSite,img=psgn('browse'))
	
	#_addon.add_directory({'mode':'BrowseCat2','site':site,'cat':'rooms','type':'js|featured'},{'title':AFColoring('Featured')},is_folder=True,fanart=fanartSite,img=psgn('browse featured'))
	#_addon.add_directory({'mode':'MenuSpecial','url':'http://raw.github.com/HIGHWAY99/plugin.stream.vaughnlive.tv/master/lists/DevsFeaturedList.txt','site':site},{'title':AFColoring("Dev's Featured List")},is_folder=True,fanart=fanartSite,img=psgn('browse devs featured'))
	
	LocalLists.append(['MyPicksList.txt','My Picks List','browse my picks list'])
	LocalLists.append(['LocalList.txt','Local List','browse local list'])
	##LocalLists.append(['','','browse'])
	for (urlA,TiTLE,iMg) in LocalLists:
		urlB=TPapp(urlA)
		if isFile(urlB)==True:
			html=common._OpenFile(urlB)
			if len(html) > 10:
				_addon.add_directory({'mode':'MenuSpecial','url':urlA,'site':site},{'title':AFColoring(TiTLE)},is_folder=True,fanart=fanartSite,img=psgn(iconSite)) #iMg
	
	#if SpecialCODE==ps('special-code'):
	#	_addon.add_directory({'mode':'MenuDevFeatured','site':site},{'title':AFColoring("Dev's Featured List[CR][Hard Coded]")},is_folder=True,fanart=fanartSite,img=psgn('browse devs featured'))
	
	#_addon.add_directory({'mode':'Search','site':site,'url':'/search/'},{'title':AFColoring('Search')+cFL(' Channels',colorB)},is_folder=True,fanart=fanartSite,img=psgn('search'))
	#_addon.add_directory({'mode':'Search','site':site,'url':'/search/_s_/users.js'},{'title':AFColoring('Search')+cFL(' People',colorB)},is_folder=True,fanart=fanartSite,img=psgn('search user'))
	#_addon.add_directory({'mode':'History101','site':site,'url':''},{'title':AFColoring('History')+cFL(' 101',colorB)},is_folder=True,fanart=fanartSite,img=psgn('history 101'))
	
	#
	#if SpecialCODE==ps('special-code'):
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section             },{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.1.name'),colorB)},fanart=fanartSite,img=psgn('favorites 1'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'2'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.2.name'),colorB)},fanart=fanartSite,img=psgn('favorites 2'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'3'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.3.name'),colorB)},fanart=fanartSite,img=psgn('favorites 3'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'4'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.4.name'),colorB)},fanart=fanartSite,img=psgn('favorites 4'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'5'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.5.name'),colorB)},fanart=fanartSite,img=psgn('favorites 5'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'6'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.6.name'),colorB)},fanart=fanartSite,img=psgn('favorites 6'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'7'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.7.name'),colorB)},fanart=fanartSite,img=psgn('favorites 7'))
	###
	#if (len(addst("LastShowListedURL")) > 0): 
	#	pars={'site':site,'section':section,'mode':'ListEpisodes','url':addst("LastShowListedURL"),'title':addst("LastShowListedNAME"),'imdb_id':addst("LastShowListedIMDBID"),'img':addst("LastShowListedIMG"),'fimg':addst("LastShowListedFANART")}; 
	#	title=AFColoring(addst("LastShowListedNAME"))+CR+cFL('[Last Show]',colorA); 
	#	_addon.add_directory(pars,{'title':title},fanart=addst("LastShowListedFANART"),img=addst("LastShowListedIMG"),is_folder=True); 
	#if (len(addst("LastEpisodeListedURL")) > 0): 
	#	pars={'site':site,'section':section,'mode':'GetMedia','url':addst("LastEpisodeListedURL"),'title':addst("LastEpisodeListedNAME"),'imdb_id':addst("LastEpisodeListedIMDBID"),'img':addst("LastEpisodeListedIMG"),'fimg':addst("LastEpisodeListedFANART"),'stitle':addst("LastEpisodeListedSTITLE"),'etitle':addst("LastEpisodeListedETITLE"),'e':addst("LastEpisodeListedEpNo"),'s':addst("LastEpisodeListedSNo"),'e2':addst("LastEpisodeListedEpNo2")}; 
	#	title=AFColoring(addst("LastEpisodeListedNAME"))+CR+cFL('[Last Episode]',colorA); 
	#	_addon.add_directory(pars,{'title':title},fanart=addst("LastEpisodeListedFANART"),img=addst("LastEpisodeListedIMG"),is_folder=True); 
	###
	_addon.add_directory({'mode':'About','site':site,'section':section},{'title':AFColoring('About')},is_folder=True,fanart=fanartSite,img=artj('About')) # 'http://i.imgur.com/0h78x5V.png' # iconSite
	###
	_addon.add_directory({'mode':'BrowseUrl','url':'http://tinyurl.com/o52ar6c'},{'title':'#The_Projects @ irc.snoonet.org:6667'},fanart=psgn('irc','.jpg'),img=psgn('irc','.jpg'),is_folder=True)
	
	_addon.add_directory({'mode':'BrowseUrl','url':'http://forums.addons.center/thread/7-release-and-bug-reports-vaughnlive/'},{'title':'Forum'},fanart=psgn('forum','.png'),img=psgn('forum','.png'),is_folder=True)
	#_addon.add_directory({'mode':'BrowseUrl','url':'http://forums.addons.center/thread/7-release-and-bug-reports-vaughnlive/'},{'title':'Note: Rtmplib is currently preventing stream from using the redirected url with a wowz:// protocol.'},fanart=fanartSite,img=psgn('forum','.png'),is_folder=True)
	#_addon.add_directory({'mode':'BrowseUrl','url':'http://forums.addons.center/thread/7-release-and-bug-reports-vaughnlive/'},{'title':'Note: The wowz:// protocol accurs ~7seconds in, resetting the stream url used.'},fanart=fanartSite,img=psgn('forum','.png'),is_folder=True)
	
	_addon.add_directory({'mode':'BrowseUrl','url':'http://www.reddit.com/r/The_Projects/'},{'title':'/r/TheProjects'},fanart=psgn('redditfa','.jpg'),img=psgn('reddit','.png'),is_folder=True)
	
	###
	set_view('list',view_mode=addst('default-view')); eod()
### ############################################################################################################
### ############################################################################################################
def mode_subcheck(mode='',site='',section='',url=''):
	try: debob({'mode':mode,'url':url,'title':addpr('title','')})
	except: pass
	if (mode=='SectionMenu'): 					MenuSection()
	elif (mode=='') or (mode=='main') or (mode=='MainMenu'): MenuSection()
	elif (mode=='SubMenu'): 						MenuSub()
	elif (mode=='MenuSpecial'): 				MenuSpecial(url)
	elif (mode=='MenuDevFeatured'): 		MenuDevFeatured()
	elif (mode=='MenuBrowse'): 					MenuBrowse()
	elif (mode=='MenuTopBar'): 					MenuTopBar()
	##																 #MenuListChannels(Url,Page='',TyPE='js',idList='[]', csrfToken='')
	elif (mode=='ListShows'): 					MenuListChannels(url,addpr('page',''),addpr('type',''),addpr('idlist',''),addpr('csrfToken',''))
	elif (mode=='BrowseCat'): 					MenuListChannels(mainSite+"/app/topbar.php?s=vl%s" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='BrowseCat2'): 					MenuListChannels(mainSite+"/app/topbar.php?s=%s" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='BrowseCat3'): 					MenuListChannels(mainSite+"/browse/%s?a=mvn" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='BrowseCat4'): 					MenuListChannels(mainSite+"/browse/%s" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='Search'):							DoSearch(addpr('title',''),url)
	elif (mode=='History101'):					MenuHistory101()
	elif (mode=='PlayLiveStream'): 			PlayLiveStream(url,addpr('title',''),addpr('img',''),addpr('channel',''),addpr('roomid',''),addpr('roomslug',''),addpr('plot',''),addpr('live',''),addpr('streamurl',''),addpr('streamkey',''),addpr('youtubeid',''),addpr('sourcetype','show'))
	#
	elif (mode=='BrowseUrl'): 					XBMC_System_Exec('"%s"' % url)
	elif (mode=='FavoritesList'): 			Fav_List(site=site,section=section,subfav=addpr('subfav',''))
	elif (mode=='About'): 							eod(); DoA('Back'); About(); 
	elif (mode=='PlayPICTURES'): 				PlayPictures(url)
	elif (mode=='PlayURL'): 						PlayURL(url)
	elif (mode=='PlayURLs'): 						PlayURLs(url)
	elif (mode=='PlayURLstrm'): 				PlayURLstrm(url)
	elif (mode=='PlayFromHost'): 				PlayFromHost(url)
	elif (mode=='PlayVideo'): 					PlayVideo(url)
	elif (mode=='PlayItCustom'): 				PlayItCustom(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='PlayItCustomL2A'): 		PlayItCustomL2A(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='Settings'): 						_addon.addon.openSettings() # Another method: _plugin.openSettings() ## Settings for this addon.
	elif (mode=='ResolverSettings'): 		import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='ResolverUpdateHostFiles'):	import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='TextBoxFile'): 				TextBox2().load_file(url,addpr('title','')); #eod()
	elif (mode=='TextBoxUrl'):  				TextBox2().load_url(url,addpr('title','')); #eod()
	elif (mode=='Download'): 						
		try: _addon.resolve_url(url)
		except: pass
		debob([url,addpr('destfile',''),addpr('destpath',''),str(tfalse(addpr('useResolver','true')))])
		DownloadThis(url,addpr('destfile',''),addpr('destpath',''),tfalse(addpr('useResolver','true')))
	elif (mode=='toJDownloader'): 			SendTo_JDownloader(url,tfalse(addpr('useResolver','true')))
	elif (mode=='cFavoritesEmpty'):  		fav__COMMON__empty( site=site,section=section,subfav=addpr('subfav','') ); xbmc.executebuiltin("XBMC.Container.Refresh"); 
	elif (mode=='cFavoritesRemove'):  	fav__COMMON__remove( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year','') )
	elif (mode=='cFavoritesAdd'):  			fav__COMMON__add( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year',''),img=addpr('img',''),fanart=addpr('fanart',''),plot=addpr('plot',''),commonID=addpr('commonID',''),commonID2=addpr('commonID2',''),ToDoParams=addpr('todoparams',''),Country=addpr('country',''),Genres=addpr('genres',''),Url=url ) #,=addpr('',''),=addpr('','')
	elif (mode=='AddVisit'):							
		try: visited_add(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='RemoveVisit'):							
		try: visited_remove(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='EmptyVisit'):						
		try: visited_empty(); RefreshList(); 
		except: pass
	elif (mode=='refresh_meta'):				refresh_meta(addpr('video_type',''),addpr('title',''),addpr('imdb_id',''),addpr('alt_id',''),addpr('year',''))
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); #MenuSection()
mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
