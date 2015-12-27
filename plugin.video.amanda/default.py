# -*- coding: utf-8 -*-
# Code by h@k@M@c
aaastreamversion = "Halow"
aaastreamdate = "23/03/2015 13:00hrs GMT"

import urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, time, base64
import re,urllib2, datetime
import xbmcplugin,random,urlparse,urlresolver
from t0mm0.common.addon import Addon
from metahandler import metahandlers
from addon.common.net import Net

PlaylistUrl = "http://aaastream.com"
AddonID = 'plugin.video.amanda'
Addon = xbmcaddon.Addon(AddonID)
localizedString = Addon.getLocalizedString
localisedTranslate = 'aHR0cDovL3Bhc3RlYmluLmNvbS9yYXcucGhwP2k9MUZrWjlhTUQ='
localisedMoLink = 'aHR0cDovL2tvZGkueHl6L21vdmllcy5waHA='
localisedCatLink = 'aHR0cDovL21vdmllc2hkLmNvL2dlbnJl'
LocalisedLa = 'aHR0cDovL3d3dy5tb3ZpZTI1LmFnLw=='
LocalisedReplay = 'aHR0cDovL2xpdmVmb290YmFsbHZpZGVvLmNvbS8='
Raw = base64.decodestring('aHR0cDovL3Bhc3RlYmluLmNvbS9yYXcucGhwP2k9')
LibDBLink = base64.decodestring('aHR0cDovL2ltdmRiLmNvbS8=')
DirectoryMSG = ""
net = Net(user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36')
headers = {
    'Accept'    :   'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
AddonName = Addon.getAddonInfo("name")
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.aaastream/fanart.jpg'))
artpath = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.aaastream/resources/art/'))
icon = Addon.getAddonInfo('icon')
addonDir = Addon.getAddonInfo('path').decode("utf-8")
LibCommon = len(PlaylistUrl)
libDir = os.path.join(addonDir, 'resources', 'lib')
sys.path.insert(0, libDir)
custurltv = str(base64.decodestring('aHR0cDovL3d3dy50dm9ubGluZS50dy8='))

datapath = xbmc.translatePath(Addon.getAddonInfo('profile'))
cookie_path = os.path.join(datapath, 'cookies')
cookie_jar = os.path.join(cookie_path, "football.lwp")
if os.path.exists(cookie_path) == False:
        os.makedirs(cookie_path)
        net.save_cookies(cookie_jar)
		
import common

metaget = metahandlers.MetaData(preparezip=False)
metaset = 'true'
custurl1 = str(base64.decodestring(LocalisedLa))

 
addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), AddonID)
if not os.path.exists(addon_data_dir):
	os.makedirs(addon_data_dir)

	
# remove this after a couple of weeks
DecrypterFile = os.path.join(libDir,"decrypter.py")
if not (os.path.isfile(DecrypterFile)):
       url = "http://kodi.xyz/updatedecrypter.php"
       urllib.urlretrieve(url,DecrypterFile)
	   
ResolverFile = os.path.join(libDir,"commonresolvers.py")
if not (os.path.isfile(ResolverFile)):
       url = "http://kodi.xyz/updateresolvers.php"
       urllib.urlretrieve(url,ResolverFile)
	   
tmpListFile = os.path.join(addonDir, 'tempList.txt')
favoritesFile = os.path.join(addonDir, 'favorites.txt')
if  not (os.path.isfile(favoritesFile)):
	f = open(favoritesFile, 'w') 
	f.write('[]') 
	f.close()  
#aaastream New security key U1R1A6P4R9I3C1K 
def Categories():
    Version = '[COLOR yellow][B]*FAILED TO CONNECT*[/B][/COLOR]'
    try: Version = net.http_GET(Raw+'1FkZ9aMD').content
    except: AddDir("[COLOR red][B]@HalowTV  twitter[/B][/COLOR]", "Update" ,98, "http://www.selfpublishingadvice.org/wp-content/uploads/2013/10/twitter-1024x1024.png")

    if Version != aaastreamdate and Version != '[COLOR yellow][B]*FAILED TO CONNECT*[/B][/COLOR]':
           UpdateMe()
           xbmc.executebuiltin("UpdateLocalAddons")

           
    AddDir("[COLOR green][B]KURDISH LIVE TV[/B][/COLOR]", Raw+"aUP8WWAd" ,4 ,"https://lh3.googleusercontent.com/-Frj2oKQyGVk/AAAAAAAAAAI/AAAAAAAAABI/A4ILF4cV2x0/photo.jpg")
    AddDir("[COLOR green][B]Arabic LIVE TV[/B][/COLOR]", Raw+"AH2EUHYY" ,4 ,"http://www.tamddon.com/wp-content/uploads/2014/02/%D8%AA%D9%84%D9%81%D8%B2%D9%8A%D9%88%D9%86.jpg")
    AddDir("[COLOR green][B]TURKISH LIVE TV[/B][/COLOR]", Raw+"8skLzEsU" ,4 ,"http://img.freeflagicons.com/thumb/football_icon/turkey/turkey_640.png")
    AddDir("[COLOR green][B]IRAN LIVE TV[/B][/COLOR]", Raw+"53bw3hGb" ,4 ,"http://forumbilder.se/EBJ4Q/kmfuhn2a.png")
    AddDir("[COLOR green][B]Afghanistan LIVE TV[/B][/COLOR]", Raw+"P9HK1Ynp" ,4 ,"http://icons.iconarchive.com/icons/hopstarter/flag-borderless/256/Afghanistan-icon.png")
    AddDir("[COLOR green][B]SWEDISH LIVE TV[/B][/COLOR]", Raw+"kbxNEVpZ" ,4 ,"http://www.iconarchive.com/download/i65935/hopstarter/flag-borderless/Sweden.ico")
    AddDir("[COLOR green][B]Norway LIVE TV[/B][/COLOR]", Raw+"LHbyudcT" ,4 ,"http://icons.iconarchive.com/icons/custom-icon-design/flag/256/Norway-Flag-icon.png")
    AddDir("[COLOR green][B]Finland LIVE TV[/B][/COLOR]", Raw+"j9bLghZ1" ,4 ,"http://img.freeflagicons.com/thumb/glossy_square_icon/finland/finland_640.png")
    AddDir("[COLOR green][B]Denmark LIVE TV[/B][/COLOR]", Raw+"5G8C6thz" ,4 ,"http://www.iconarchive.com/download/i65855/hopstarter/flag-borderless/Denmark.ico")
    AddDir("[COLOR green][B]UK LIVE TV[/B][/COLOR]", Raw+"Nny5ifgH" ,4 ,"http://files.softicons.com/download/internet-icons/glossy-flag-icons-by-nordic-factory/ico/uk.ico")
    AddDir("[COLOR green][B]ISRAEL LIVE TV[/B][/COLOR]", Raw+"yMFRKMMT" ,4 ,"http://icons.iconarchive.com/icons/iconscity/flags/256/israel-icon.png")
    AddDir("[COLOR green][B]GREECE LIVE TV[/B][/COLOR]", Raw+"96mMhK4s" ,4 ,"http://www.iconarchive.com/download/i65868/hopstarter/flag-borderless/Greece.ico")
    AddDir("[COLOR green][B]Italia LIVE TV[/B][/COLOR]", Raw+"zyF70nW2" ,4 ,"http://www.iconarchive.com/download/i65883/hopstarter/flag-borderless/Italy.ico")
    AddDir("[COLOR green]Espana LIVE TV[B][/B][/COLOR]", Raw+"bz1aT8vi" ,4 ,"http://www.iconarchive.com/download/i65933/hopstarter/flag-borderless/Spain.ico")
    AddDir("[COLOR green][B]Serbian LIVE TV[/B][/COLOR]", Raw+"GzdWMNgg" ,4 ,"http://www.fancyicons.com/free-icons/103/flags/png/256/serbia_flag_256.png")
    AddDir("[COLOR green][B]Albanian LIVE TV[/B][/COLOR]", Raw+"UHLrrvuE" ,4 ,"http://static1.worldcrunch.com/images/flags/Albania.png")
    AddDir("[COLOR green][B]Bosnien LIVE TV[/B][/COLOR]", Raw+"h7Vs46Qi" ,4 ,"http://static1.menstream.pl/i/mundial2014/flagi/bosnia-i-hercegowina.png")
    AddDir("[COLOR green][B]Russia LIVE TV[/B][/COLOR]", Raw+"hVGLQv0m" ,4 ,"http://www.iconarchive.com/download/i65923/hopstarter/flag-borderless/Russia.ico")
    AddDir("[COLOR green][B]Latino America LIVE TV[/B][/COLOR]", Raw+"7eqeuVkJ" ,4 ,"http://www.allpago.com/wp-content/uploads/2014/10/Brazil-icon1.png")
    AddDir("[COLOR green][B]French LIVE TV[/B][/COLOR]", Raw+"bc4QF6en" ,4 ,"http://www.iconarchive.com/download/i65864/hopstarter/flag-borderless/France.ico")
    AddDir("[COLOR green][B]Ukraine LIVE TV[/B][/COLOR]", Raw+"RT9XrXys" ,4 ,"http://icons.iconarchive.com/icons/iconscity/flags/256/ukraine-icon.png")
    AddDir("[COLOR green][B]Pakistan LIVE TV[/B][/COLOR]", Raw+"08q2MN09" ,4 ,"http://img.freeflagicons.com/thumb/round_icon/pakistan/pakistan_640.png")
    AddDir("[COLOR green][B]Germany LIVE TV[/B][/COLOR]", Raw+"DsBmxZhK" ,4 ,"http://icons.iconarchive.com/icons/iconscity/flags/256/germany-icon.png")
    AddDir("[COLOR green][B]Inden LIVE TV[/B][/COLOR]", Raw+"b5MQRZAg" ,4 ,"http://www.iconarchive.com/download/i65877/hopstarter/flag-borderless/India.ico")
    AddDir("[COLOR green][B]USA LIVE TV[/B][/COLOR]", Raw+"hNZ6kjp4" ,4 ,"http://www.icon2s.com/wp-content/uploads/2012/12/US-United-States-flag-icon.png")
    AddDir("[COLOR green][B]portugal LIVE TV[/B][/COLOR]", Raw+"8jtfy7W0" ,4 ,"http://www.iconarchive.com/download/i65919/hopstarter/flag-borderless/Portugal.ico")
    AddDir("[COLOR green][B]Thailand LIVE TV[/B][/COLOR]", Raw+"p2ZsH6FT" ,4 ,"http://www.iconarchive.com/download/i65937/hopstarter/flag-borderless/Thailand.ico")
    AddDir("[COLOR green][B]Croatia LIVE TV[/B][/COLOR]", Raw+"zjtnZQjF" ,4 ,"http://www.icon2s.com/wp-content/uploads/2012/12/Croatia-flag-icon.png")
    AddDir("[COLOR green][B]Brazil LIVE TV[/B][/COLOR]", Raw+"sJf3nxRf" ,4 ,"https://cdn2.iconfinder.com/data/icons/world-flag-icons/256/Flag_of_Brazil.png")
    AddDir("[COLOR green][B]Korea LIVE TV[/B][/COLOR]", Raw+"YM5dK6GX" ,4 ,"http://comps.canstockphoto.com/can-stock-photo_csp13904483.jpg")
    AddDir("[COLOR green][B]Austria LIVE TV[/B][/COLOR]", Raw+"CQfMR62W" ,4 ,"http://www.iconarchive.com/download/i65836/hopstarter/flag-borderless/Austria.ico")
    AddDir("[COLOR green][B]Holland LIVE TV[/B][/COLOR]", Raw+"NPen5ZCV" ,4 ,"http://images.mystockphoto.com/files/premium/thumbs/150/netherlands-3d-button-on-white-background_150145484.jpg")
    AddDir("[COLOR green][B]Poland LIVE TV[/B][/COLOR]", Raw+"PwGujQHR" ,4 ,"http://www.country-dialing-codes.net/img/png-country-4x2-fancy-res-1280x960/pl.png")
    AddDir("[COLOR green][B]SOMALI LIVE TV[/B][/COLOR]", Raw+"Z6NpggZ0" ,4 ,"http://icons.iconarchive.com/icons/custom-icon-design/all-country-flag/256/Somalia-Flag-icon.png")
    AddDir("[COLOR green][B]Bulgarian LIVE TV[/B][/COLOR]", Raw+"JZEWDxHh" ,4 ,"http://www.veryicon.com/icon/png/Flag/Rounded%20World%20Flags/Bulgaria%20Flag.png")
    AddDir("[COLOR green][B]world LIVE TV[/B][/COLOR]", Raw+"y8iNNZJS" ,4 ,"http://findicons.com/files/icons/662/preview/world_flag_full.png")
    AddDir("[COLOR green][B]Poland LIVE TV[/B][/COLOR]", Raw+"xeyTWEjc" ,4 ,"https://cdn2.iconfinder.com/data/icons/world-flag-icons/256/Flag_of_Poland.png")
    AddDir("[COLOR green][B]CHILE LIVE TV[/B][/COLOR]", Raw+"heRxPkem" ,4 ,"http://icons.iconarchive.com/icons/iconscity/flags/256/chile-icon.png")
    AddDir("[COLOR green][B]COSTA RICA LIVE TV[/B][/COLOR]", Raw+"fnnC6LWW" ,4 ,"http://img.freeflagicons.com/thumb/round_icon/costa_rica/costa_rica_640.png")
    AddDir("[COLOR green][B]MEXICO LIVE TV[/B][/COLOR]", Raw+"WNty2W1s" ,4 ,"http://icons.iconarchive.com/icons/hopstarter/flag/256/Mexico-icon.png")
    AddDir("[COLOR green][B]COLOMBIA LIVE TV[/B][/COLOR]", Raw+"8wqHrZEV" ,4 ,"http://img.freeflagicons.com/thumb/glossy_square_icon/colombia/colombia_640.png")
    AddDir("[COLOR green][B]ARGENTINA LIVE TV[/B][/COLOR]", Raw+"SfJupvk8" ,4 ,"http://img.freeflagicons.com/thumb/glossy_square_icon/argentina/argentina_640.png")
    AddDir("[COLOR green][B]Trinidad LIVE TV[/B][/COLOR]", Raw+"tSR1LCKA" ,4 ,"http://icons.iconseeker.com/png/fullsize/rounded-world-flags/trinidad-and-tobago-flag.png")
    AddDir("[COLOR green][B]GHANA LIVE TV[/B][/COLOR]", Raw+"37qch7SJ" ,4 ,"http://www.fancyicons.com/free-icons/103/flags/png/256/ghana_flag_256.png")
    AddDir("[COLOR green][B]Ireland LIVE TV[/B][/COLOR]", Raw+"Er6tEtp9" ,4 ,"http://icons.iconarchive.com/icons/hopstarter/flag/256/Ireland-icon.png")
    AddDir("[COLOR green][B]Canada LIVE TV[/B][/COLOR]", Raw+"H48aVN7Z" ,4 ,"http://icons.iconarchive.com/icons/custom-icon-design/flag-2/256/Canada-Flag-icon.png")
    AddDir("[COLOR green][B]Chinia LIVE TV[/B][/COLOR]", Raw+"yw4yLJMm" ,4 ,"http://icons.iconarchive.com/icons/custom-icon-design/flag-2/256/China-Flag-icon.png")
    AddDir("[COLOR green][B]Webcams  LIVE TV[/B][/COLOR]", Raw+"3QsyXVHa" ,4 ,"http://www.mhub.tv/wp-content/uploads/2013/12/webcam.png")
    AddDir("[COLOR green][B]Africa LIVE TV[/B][/COLOR]", Raw+"2aYeNhfC" ,4 ,"http://www.freeiptvlinks.com/wp-content/uploads/2015/04/Flag_of_South_Africa.svg_-304x200.png")
    AddDir("[COLOR green][B]Macedonia LIVE TV[/B][/COLOR]", Raw+"v1mxrzHF" ,4 ,"http://img.freeflagicons.com/thumb/glossy_square_icon/macedonia/macedonia_640.png")
    AddDir("[COLOR green][B]Bangladesh LIVE TV[/B][/COLOR]", Raw+"dH2PZY5B" ,4 ,"http://www.fancyicons.com/free-icons/103/flags/png/256/bangladesh_flag_256.png")
    AddDir("[COLOR green][B]Czech LIVE TV[/B][/COLOR]", Raw+"M84yYRHe" ,4 ,"http://img.freeflagicons.com/thumb/square_icon/czech_republic/czech_republic_640.png")
    AddDir("[COLOR green][B]Slovakien LIVE TV[/B][/COLOR]", Raw+"Mnhiv1Tf" ,4 ,"http://static4.depositphotos.com/1003329/334/i/950/depositphotos_3349502-Icon-with-flag-of-Slovakia-isolated.jpg")
    AddDir("[COLOR green][B]Indonesian LIVE TV[/B][/COLOR]", Raw+"H2tigGCQ" ,4 ,"http://www.country-dialing-codes.net/img/png-country-4x2-fancy-res-1280x960/id.png")
    AddDir("[COLOR green][B]Philippine LIVE TV[/B][/COLOR]", Raw+"gqd5pSZM" ,4 ,"http://png-5.findicons.com/files/icons/656/rounded_world_flags/256/philippines.png")
    AddDir("[COLOR green][B]Romania  LIVE TV[/B][/COLOR]", Raw+"x5NqzmwS" ,4 ,"https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/1280px-Flag_of_Romania.svg.png")


    xbmc.executebuiltin('Container.SetViewMode(25)') 
   

def MOVIES():
        AddDir('[COLOR white][B]Featured[/B][/COLOR]',custurl1+'featured-movies/',52,"http://www.mrcolionnoir.com/wp-content/uploads/2013/08/Featured.png")
        AddDir('[COLOR white][B]New Releases[/B][/COLOR]',custurl1+'new-releases/',52,"http://www.presentation-process.com/images/New-icon.gif")
        AddDir('[COLOR white][B]Latest Added[/B][/COLOR]',custurl1+'latest-added/',52,"http://comps.canstockphoto.com/can-stock-photo_csp16348546.jpg")
        AddDir('[COLOR white][B]HD[/B][/COLOR]',custurl1+'latest-hd-movies/',52,"http://s5.postimg.org/pwa1iwsiv/image.png")
        AddDir('[COLOR white][B]Most Viewed[/B][/COLOR]',custurl1+'most-viewed/',52,"https://www.colourbox.com/preview/10743341-most-viewed-sign-icon-most-watched-symbol.jpg")
        AddDir('[COLOR white][B]Search[/B][/COLOR]',custurl1+'most-viewed/',79,"http://c.dryicons.com/images/icon_sets/shine_icon_set/png/256x256/movie_search.png")
        AddDir('[COLOR white][B]TRAILERS[/B][/COLOR]','movieclipsTRAILERS',11,"http://i292.photobucket.com/albums/mm16/kiwijunglist/category/th_Trailers.png")
        xbmc.executebuiltin("Container.SetViewMode(500)") 
        
def TV():
        AddDir('[COLOR white]Newest Episodes [/COLOR]',custurltv+'new-episodes/',77,'http://s5.postimg.org/xsuir53zb/new.png')
        AddDir('[COLOR white]Latest Added[/COLOR]',custurltv+'latest-added/',75,'http://s5.postimg.org/5rghdfyp3/latest_added.png')
        AddDir('[COLOR white]Search[/COLOR]',custurltv,78,'http://s5.postimg.org/rhpbaq2qv/search.png')
        AddDir('[COLOR white]A-Z[/COLOR]',custurltv+'tv-listings/0-9',82,'http://s5.postimg.org/t19z1a4x3/tvshows.jpg')
  		
        GenresPage = net.http_GET(custurltv+'genres/action').content
        GenresPage = GenresPage.encode('ascii', 'ignore').decode('ascii')
        GenresPage = regex_from_to(GenresPage, '<div class="tv_letter">', '</ul></div>')
        GenresPage = GenresPage.replace('\"','').replace(')','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')

        match=re.compile("<a href=/(.+?)>(.+?)</a>",re.DOTALL).findall(str(GenresPage))
		
        for url,name in match:
                name = CLEAN(name)
                AddDir('[COLOR white]'+name+'[/COLOR]',custurltv+url,83,"http://www.iconarchive.com/download/i14263/hydrattz/multipurpose-alphabet/Letter-"+name[:1]+"-black.ico")

        xbmc.executebuiltin("Container.SetViewMode(500)")
		
def REPLAYS():
        custurlreplay = str(base64.decodestring(LocalisedReplay))
        AddDir("[COLOR Pink][B]Full Matches[/B][/COLOR]",custurlreplay+'fullmatch',151 ,"http://livefootballvideo.com/images/xlivefootballvideologo.png.pagespeed.ic.3kxaAupa3O.png")
        AddDir("[COLOR Pink][B]Highlights[/B][/COLOR]", Raw+"2BnErJa1",155 ,"http://livefootballvideo.com/images/xlivefootballvideologo.png.pagespeed.ic.3kxaAupa3O.png")
        AddDir('[COLOR Pink][B]Search[/B][/COLOR]','search',154,"http://thumbs.dreamstime.com/x/green-3d-search-icon-7724318.jpg")
        AddDir("[COLOR Pink][B]FOOTBALL TEAMS[/B][/COLOR]", "7FpJGU86", 7 ,"http://forzafutbol.com/wp-content/uploads/2011/08/Primera-La-Liga-clubs-logos-fixtures-El-classico-2011-2012.jpeg")
        AddDir("[COLOR Pink][B]UFC HD[/B][/COLOR]", "http://watchwrestling.ch/category/ufc/", 9 ,"http://fc04.deviantart.net/fs71/f/2011/287/2/b/icon_ufc__by_evgeniysi-d4csp8a.png")
        AddDir("[COLOR Pink][B]WWE HD[/B][/COLOR]", "http://watchwrestling.ch/category/wwe/ppv/", 9 ,"http://media.wrestlenewz.com/wp-content/uploads/2014/09/wwe-logo1-750x340-1412163784.jpg")
		
        xbmc.executebuiltin("Container.SetViewMode(500)")


def UFCSection(url):
    link = net.http_GET(url).content
    link = link.encode('ascii', 'ignore').decode('ascii')
	
    nextpage = ''
    if link.find('rel="next') > 0:
       nextpage = regex_from_to(link, '<link rel="next" href="//', '"/>')
	   
    link = regex_from_to(link, '<div class="nag cf">', '<div class="loop-nav pag-nav">') 
    all_videos = regex_get_all(link, '<div id="post', '<span class="overlay"></span>')
    for a in all_videos:
        title = regex_from_to(a, ' title="', '"')
        vurl = regex_from_to(a, ' href="', '"')
        iconimage = "http://" + regex_from_to(a, '<img src="//', '" alt=')
        AddDir(title,vurl,15,iconimage)

    if len(nextpage) > 0:
       nextpage = 'http://' + nextpage
#       xbmcgui.Dialog().ok('msg', nextpage)
       AddDir('[B][COLOR Red]Next.....[/COLOR][/B]',nextpage,9,"http://s5.postimg.org/rmlrly3jb/next.png")

    xbmc.executebuiltin("Container.SetViewMode(500)")
	
def UFCScrape(url):
    link = net.http_GET(url).content
    link = link.encode('ascii', 'ignore').decode('ascii')
    iconimage = regex_from_to(link, '<meta name="twitter:image:src" content="', '"/>') 
    link = regex_from_to(link, '<div class="entry-content rich-content">', '<div id="extras">') 
    all_videos = regex_get_all(link, '<a class="small cool-blue vision-button"', '</a>')
    c=0
    for a in all_videos:
        vurl = regex_from_to(a, ' href="', '" target=')
        c=c+1
        title = "[COLOR gold] Source ["+str(c)+"] [/COLOR]" + regex_from_to(a, 'blank">', '</a>')
        AddDir(title,vurl,16,iconimage)

def StreamUFC(name,url,thumb):
    name2 = name
    url2 = url
              
    print url
    if re.search('http://pwtalk.net', url):
       headers['Referer'] = "http://watchwrestling.ch/"
       url_content = net.http_GET(url, headers=headers).content        
       url_content = re.sub("<!--.+?-->", " ", url_content)
       link2 = regex_from_to(url_content, '<iframe ', '<') 
       url = regex_from_to(link2, 'src="', '">')
       print url   
			
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        streamlink = urlresolver.resolve(urllib2.urlopen(req).url)
        addLinkMovies(name2,streamlink,thumb)
    except:
        Notify('small','AAA Sorry Link Removed:', 'Please try another one.',9000)
		   
def PlayYoutubeUser(url):
    GetDataValue = "http://gdata.youtube.com/feeds/api/users/"
    GetDataValueB = "/uploads?start-index=1&max-results=10"
    YouTube_List(GetDataValue+url+GetDataValueB)

	
def KidzCorner(url):
    GetDataValue = "http://gdata.youtube.com/feeds/api/users/"
    GetDataValueB = "/uploads?start-index=1&max-results=10"
    links = net.http_GET(Raw+url).content
    match=re.compile('I:"(.+?)" A:"(.+?)" B:"(.+?)" C:"(.+?)"').findall(str(links))
    
    all_videos = regex_get_all(links, 'I:', '"#')
    for a in all_videos:
        mode = regex_from_to(a, 'I:"', '"')
        url = regex_from_to(a, 'A:"', '"')
        name = regex_from_to(a, 'B:"', '"')
        icon = regex_from_to(a, 'C:"', '"')
        AddDir('[COLOR lime]'+name+'[/COLOR]',GetDataValue+url+GetDataValueB, mode, icon)
		
	xbmc.executebuiltin("Container.SetViewMode(50)")
	
def FootballTeams(url):
    GetDataValue = "http://gdata.youtube.com/feeds/api/users/"
    GetDataValueB = "/uploads?start-index=1&max-results=10"
    links = net.http_GET(Raw+url).content
    match=re.compile('I:"(.+?)" A:"(.+?)" B:"(.+?)" C:"(.+?)"').findall(str(links))
    
    all_videos = regex_get_all(links, 'I:', '"#')
    for a in all_videos:
        mode = regex_from_to(a, 'I:"', '"')
        url = regex_from_to(a, 'A:"', '"')
        name = regex_from_to(a, 'B:"', '"')
        icon = regex_from_to(a, 'C:"', '"')
        AddDir('[COLOR lime]'+name+'[/COLOR]',GetDataValue+url+GetDataValueB, mode, icon)
		
	xbmc.executebuiltin("Container.SetViewMode(500)")

def StreamsList(url):
    links = net.http_GET(Raw+url).content
    match=re.compile('I:"(.+?)" A:"(.+?)" B:"(.+?)" C:"(.+?)"').findall(str(links))
    AddDir("[COLOR white][B] BONUS PACK [/B][/COLOR]", "Bqdg4C4g" ,10 ,"http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg")
    AddDir("[COLOR white][B] COUNTRY [/B][/COLOR]", "Bqdg4C4g" ,5 ,"http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg")
    
    all_videos = regex_get_all(links, 'I:', '"#')
    for a in all_videos:
        mode = regex_from_to(a, 'I:"', '"')
        url = regex_from_to(a, 'A:"', '"')
        name = regex_from_to(a, 'B:"', '"')
        icon = regex_from_to(a, 'C:"', '"')
        AddDir('[COLOR lime]'+name+'[/COLOR]',Raw+url, mode, icon)

		
	xbmc.executebuiltin("Container.SetViewMode(500)")
		
		
def YouTube_List(url):
    aaalink = regex_from_to(url, 'http://gdata.youtube.com/feeds/api/users/', '/uploads?')
    link = net.http_GET(url).content
    link = link.encode('ascii', 'ignore').decode('ascii')
    link = link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','')
 
    all_videos = regex_get_all(link, '<entry>', '</entry>')
    for a in all_videos:
        title = regex_from_to(a, '<title type=text>', '</title>')
        thumbnail = regex_from_to(a, '<media:thumbnail url=', ' height=')
        video_id = FindFirstPattern(a,"http\://www.youtube.com/watch\?v\=([^\&]+)\&").replace("&amp;","&")
        url = "PlayMedia(plugin://plugin.video.youtube/?action=play_video&videoid="+video_id+")"
        AddDir(title ,url, 46, thumbnail, isFolder=False)
		
    start_index = int( FindFirstPattern( link ,"start-index=(\d+)") )
    max_results = int( FindFirstPattern( link ,"max-results=(\d+)") )
    next_page_url = "http://gdata.youtube.com/feeds/api/users/"+aaalink+"/uploads?start-index=%d&max-results=%d" % ( start_index+max_results , max_results)

    AddDir("[COLOR red][B]Next.....[/B][/COLOR]", next_page_url ,200 ,"http://s5.postimg.org/rmlrly3jb/next.png")


def FindFirstPattern(text,pattern):
    result = ""
    try:    
        matches = re.findall(pattern,text, flags=re.DOTALL)
        result = matches[0]
    except:
        result = ""

    return result
	
def Highlights():
        link = net.http_GET('http://doctortips.net/wss/footballhighlights.html').content
        link = link.encode('ascii', 'ignore').decode('ascii')
        match=re.compile('<a href="(.+?)">(.+?)</a></div>').findall(link)
        for url, name in match:
                AddDir(name,url,156,"http://s5.postimg.org/vr0ijo3mv/fullmatches.png")


def PlayHighlights(name,url):
    ok=True
    try:
      liz=xbmcgui.ListItem(name, "http://s5.postimg.org/vr0ijo3mv/fullmatches.png","http://s5.postimg.org/vr0ijo3mv/fullmatches.png"); liz.setInfo( type="Video", infoLabels={ "Title": name } )
      ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
      xbmc.Player ().play(url, liz, False)
    except:pass

    return ok
				
def FullMatches(url):
    link = net.http_GET(url).content
    link = link.encode('ascii', 'ignore').decode('ascii')

    r='<div class="cover"><a href="(.+?)" rel="bookmark" title="(.+?)">.+?<img src="(.+?)".+?<p class="postmetadata longdate" rel=".+?">(.+?)/(.+?)/(.+?)</p>'
    match=re.compile(r,re.DOTALL).findall(link)
    for vurl,name,iconimage,month,day,year in match:
        _date='%s/%s/%s'%(day,month,year)  
        name='%s-[COLOR gold][%s][/COLOR]'%(name,_date)    
        AddDir(name,vurl,152,iconimage)
    
    nextpage=re.compile('</span><a class="page larger" href="(.+?)">').findall(link)
    if nextpage:
       vurl = str(nextpage)
       vurl = vurl.replace('[u\'','')
       vurl = vurl.replace(']','')
       vurl = vurl.replace('\'','')
       AddDir('[B][COLOR red]Next......[/COLOR][/B]',vurl,151,"http://s5.postimg.org/rmlrly3jb/next.png")

    xbmc.executebuiltin("Container.SetViewMode(500)")	

def SearchReplays():
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Search Halow Replays')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() .replace(' ','+')
            if search_entered == None:
                return False
        link=OPEN_MAGIC('http://www.google.com/cse?cx=partner-pub-9069051203647610:8413886168&ie=UTF-8&q=%s&sa=Search&ref=livefootballvideo.com/highlights'%search_entered)
        match=re.compile('" href="(.+?)" onmousedown=".+?">(.+?)</a>').findall(link)
        for url,dirtyname in match: 
            import HTMLParser
            cleanname= HTMLParser.HTMLParser().unescape(dirtyname)
            name= cleanname.replace('<b>','').replace('</b>','')
            AddDir(name,url,152,'')
        xbmc.executebuiltin("Container.SetViewMode(50)")	 
		
def REPLAYSGETLINKS(name,url):#  cause mode is empty in this one it will go back to first directory
    link = net.http_GET(url).content
    link = link.encode('ascii', 'ignore').decode('ascii')
    if "proxy.link=lfv*" in link :
        import decrypter
        match = re.compile('proxy\.link=lfv\*(.+?)&').findall(link)
        match = uniqueList(match)
        match = [decrypter.decrypter(198,128).decrypt(i,base64.urlsafe_b64decode('Y0ZNSENPOUhQeHdXbkR4cWJQVlU='),'ECB').split('\0')[0] for i in match]
        print match
        for url in match:

            url = replaceHTMLCodes(url)
            if url.startswith('//') : url = 'http:' + url
            url = url.encode('utf-8')  
            _name=url.split('://')[1] 
            _name=_name.split('/')[0].upper()
            ReplaysAddDir( name+' - [COLOR red]%s[/COLOR]'%_name , url , 120 , 'http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg' , '' )
    if "www.youtube.com/embed/" in link :
        r = 'youtube.com/embed/(.+?)"'
        match = re.compile(r,re.DOTALL).findall(link)
        yt= match[0]
        iconimage = 'http://i.ytimg.com/vi/%s/0.jpg' % yt.replace('?rel=0','')
        url = 'plugin://plugin.video.youtube/?path=root/video&action=play_video&videoid=%s' % yt.replace('?rel=0','')
        ReplaysAddDir( name+' - [COLOR red]YOUTUBE[/COLOR]' , url , 120 , iconimage , '' )
    if "dailymotion.com" in link :
        r = 'src="http://www.dailymotion.com/embed/video/(.+?)\?.+?"></iframe>'
        match = re.compile(r,re.DOTALL).findall(link)
        for url in match :
            ReplaysAddDir ( name+' - [COLOR red]DAILYMOTION[/COLOR]' , url , 120 , 'http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg', '' )
    if "http://videa" in link :
        r = 'http://videa.+?v=(.+?)"'
        match = re.compile(r,re.DOTALL).findall(link)
        for url in match :
            ReplaysAddDir (name+' - [COLOR red]VIDEA[/COLOR]',url,120,'', '' )
            
    if "rutube.ru" in link :
        r = 'ttp://rutube.ru/video/embed/(.+?)\?'
        match = re.compile(r,re.DOTALL).findall(link)
        print match
        for url in match :
            ReplaysAddDir (name+' - [COLOR red]RUTUBE[/COLOR]',url,120,'http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg', '' )
    if 'cdn.playwire.com' in link :
        r = 'cdn.playwire.com/bolt/js/embed.min.js.+?data-publisher-id="(.+?)".+?data-config="(.+?)">'
        match = re.compile(r,re.DOTALL).findall(link)
        for id ,vid in match :
            
            url=vid.replace('player.json','manifest.f4m')
            ReplaysAddDir (name+' - [COLOR red]PLAYWIRE[/COLOR]',url,120,'http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg', '' )
    if "vk.com" in link :
        r = '<iframe src="http://vk.com/(.+?)"'
        match = re.compile(r,re.DOTALL).findall(link)
        for url in match :
            ReplaysAddDir (name+' - [COLOR red]VK.COM[/COLOR]','http://vk.com/'+url,120,'http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg', '' )
    if "mail.ru" in link :
        r = 'http://videoapi.my.mail.ru/videos/embed/(.+?)\.html'
        match = re.compile(r,re.DOTALL).findall(link)
        for url in match :
            ReplaysAddDir (name+' - [COLOR red]MAIL.RU[/COLOR]','http://videoapi.my.mail.ru/videos/%s.json'%url,120,'http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg', '' )            
          

def PLAYSTREAM(name,url,iconimage):
 #       xbmcgui.Dialog().ok(str(name), url)
        if 'YOUTUBE' in name:
            link = str(url)
        elif 'VIDEA' in name:
            try:
                url=url.split('-')[1]
            except:
                url=url
            link = GrabVidea(url)
        elif 'VK.COM' in name:
            link = GrabVK(url)

        elif 'MAIL.RU' in name:
            link = GrabMailRu(url)

            
        elif 'RUTUBE' in name:
            try:
                html = 'http://rutube.ru/api/play/trackinfo/%s/?format=xml'% url.replace('_ru','')
                print html
#                link = OPEN_URL(html)
                link = net.http_GET(html).content
                r = '<m3u8>(.+?)</m3u8>'
                match = re.compile(r,re.DOTALL).findall(link)
                if match:
                    link=match[0]
                else:
                    dialog = xbmcgui.Dialog()
                    dialog.ok("Football Replays", '','Sorry Video Is Private', '')
                    return
            except:
                dialog = xbmcgui.Dialog()
                dialog.ok("Football Replays", '','Sorry Video Is Private', '')
                return
        elif 'PLAYWIRE' in name:
            link = net.http_GET(url).content
 #           link = OPEN_URL(url)
            r = '<baseURL>(.+?)</baseURL>.+?media url="(.+?)"'
            match = re.compile(r,re.DOTALL).findall(link)
            if match:
                link=match[0][0]+'/'+match[0][1]
                
                
        elif 'DAILYMOTION' in name:
            try:
                url = url.split('video/')[1]
            except:
                url = url
            link = getStreamUrl(url)
        try:
            liz=xbmcgui.ListItem(name, iconImage="http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={ "Title": name} )
            liz.setProperty("IsPlayable","true")
            liz.setPath(link)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
        except:pass
        
 
def GrabMailRu(url):
    print 'RESOLVING VIDEO.MAIL.RU VIDEO API LINK'
      
    items = []
    quality = "???"
    data = getData(url)
    cookie = net.get_cookies()
    for x in cookie:

         for y in cookie[x]:

              for z in cookie[x][y]:
                   
                   l= (cookie[x][y][z])
    name=[]
    url=[]
    r = '"key":"(.+?)","url":"(.+?)"'
    match = re.compile(r,re.DOTALL).findall(data)
    for quality,stream in match:
        name.append(quality.title())
        

  
        test = str(l)
        test = test.replace('<Cookie ','')
        test = test.replace(' for .my.mail.ru/>','')
        url.append(stream +'|Cookie='+test)

    return url[xbmcgui.Dialog().select('Please Select Resolution', name)]

def getData(url,headers={}):
    net.save_cookies(cookie_jar)
    req = urllib2.Request(url)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    data=response.read()
    response.close()
    return data
	
def ReplaysAddDir(name,url,mode,iconimage,page):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&page="+str(page)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name} )
        if mode == 120:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def uniqueList(name):
    uniques = []
    for n in name:
        if n not in uniques:
            uniques.append(n)
    return uniques  

def replaceHTMLCodes(txt):
    import HTMLParser

    # Fix missing ; in &#<number>;
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", makeUTF8(txt))

    txt = HTMLParser.HTMLParser().unescape(txt)
    txt = txt.replace("&amp;", "&")
    return txt  

def makeUTF8(data):
    return data
    try:
        return data.decode('utf8', 'xmlcharrefreplace') # was 'ignore'
    except:
        s = u""
        for i in data:
            try:
                i.decode("utf8", "xmlcharrefreplace") 
            except:
                log("Can't convert character", 4)
                continue
            else:
                s += i
        return s  

def getStreamUrl(id):
    maxVideoQuality = "1080p"
    content = net.http_GET("http://www.dailymotion.com/embed/video/"+id).content

    if content.find('"statusCode":410') > 0 or content.find('"statusCode":403') > 0:
        xbmc.executebuiltin('XBMC.Notification(Info:,Not Found (DailyMotion)!,5000)')
        return ""
    else:
        matchFullHD = re.compile('"stream_h264_hd1080_url":"(.+?)"', re.DOTALL).findall(content)
        matchHD = re.compile('"stream_h264_hd_url":"(.+?)"', re.DOTALL).findall(content)
        matchHQ = re.compile('"stream_h264_hq_url":"(.+?)"', re.DOTALL).findall(content)
        matchSD = re.compile('"stream_h264_url":"(.+?)"', re.DOTALL).findall(content)
        matchLD = re.compile('"stream_h264_ld_url":"(.+?)"', re.DOTALL).findall(content)
        url = ""
        if matchFullHD and maxVideoQuality == "1080p":
            url = urllib.unquote_plus(matchFullHD[0]).replace("\\", "")
        elif matchHD and (maxVideoQuality == "720p" or maxVideoQuality == "1080p"):
            url = urllib.unquote_plus(matchHD[0]).replace("\\", "")
        elif matchHQ:
            url = urllib.unquote_plus(matchHQ[0]).replace("\\", "")
        elif matchSD:
            url = urllib.unquote_plus(matchSD[0]).replace("\\", "")
        elif matchLD:
            url = urllib.unquote_plus(matchLD[0]).replace("\\", "")
        return url



def video_artists(name,url):
    alphabet =  ['0-9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
    for a in alphabet:
        MusicAddDir(a,url+a.lower(),106,"http://www.iconarchive.com/download/i14263/hydrattz/multipurpose-alphabet/Letter-"+a.upper()+"-black.ico",'1')
    
    xbmc.executebuiltin("Container.SetViewMode(500)")
	
def Get_video_artists_AZ(name,url):
    link = net.http_GET(url).content
    link = link.encode('ascii', 'ignore').decode('ascii')
	
	
    all_artists = regex_from_to(link, 'ul class="nameList">', '<div id="footer">')
    match = re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(all_artists)
    for url, title in match:
        MusicAddDir(title,url,107,'','n')
		
    xbmc.executebuiltin("Container.SetViewMode(50)")	


def SEARCHTV(url):
        EnableMeta = metaset
        keyb = xbmc.Keyboard('', 'Halow TvSearch TV Shows')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                print encode
                url = custurltv+'search.php?key='+encode
                print url
                links = net.http_GET(url).content
                links = regex_from_to(links, '<div class="found">', '</div>')
                links=links.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
                
#				match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>   </li>',re.DOTALL).findall(links) 

                all_genres = regex_get_all(links, '<ul><li>', '</li></ul>')
                for a in all_genres:
                        url = regex_from_to(a, '<a href="', '"')
                        name = regex_from_to(a, '">', '<').lstrip()
                        name = CLEAN(name)
                        AddDir(name,custurltv+url,80,'')

def LATESTADDED(url):
        links = net.http_GET(url).content
        links = links.encode('ascii', 'ignore').decode('ascii')
        links = regex_from_to(links, '<div class="home">', '</div>')
        links=links.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
		
        match=re.compile('<li><a href="/(.+?)">(.+?)</a></li>',re.DOTALL).findall(str(links))
        for url,name in match:
                name = CLEAN(name)
                searcher = url.replace('/','')
                AddDir(name,custurltv+url,80,'')
				
        xbmc.executebuiltin("Container.SetViewMode(50)") 
				
def NEWLINKS(url):
        EnableMeta = metaset
        links = net.http_GET(url).content
		
        links=links.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
        NotNeeded, SelectOut = links.split('<div class="leftpage_frame">')
        SelectOut , NotNeeded = SelectOut.split('<div class="foot"')
		
        match=re.compile('<li><a href="/(.+?)" >(.+?)</a></li><li>',re.DOTALL).findall(str(SelectOut))
        for url,name in match:
                name = CLEAN(name)
                searcher = url.replace('/','')
                AddDir(name,custurltv+url,80,'')
				
        xbmc.executebuiltin("Container.SetViewMode(50)") 
		
def GETLINKS(url):
        links = net.http_GET(Raw+url).content
        match=re.compile('I:"(.+?)" A:"(.+?)" B:"(.+?)"',re.DOTALL).findall(str(links))
        for mode,url,name in match:
                name = CLEAN(name)
                AddDir('[COLOR lime]'+name+'[/COLOR]',Raw+url, mode, "http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg")  
				
        xbmc.executebuiltin("Container.SetViewMode(50)")
			
def ADINDEX(url):
        links = net.http_GET(Raw+url).content
        match=re.compile('I:"(.+?)" A:"(.+?)" B:"(.+?)" C:"(.+?)"',re.DOTALL).findall(str(links))
        for mode,url,name,icon in match:
                name = CLEAN(name)
                AddDir('[COLOR lime]'+name+'[/COLOR]',Raw+url, mode, icon)  
        
        xbmc.executebuiltin("Container.SetViewMode(500)")


def NEWEPISODESTV(url):
        links = net.http_GET(url).content 
        links = links.encode('ascii', 'ignore').decode('ascii')
        links = regex_from_to(links, '<div class="home">', '</div>')
        links=links.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')

      
        match=re.compile('<li><a href="/(.+?)">(.+?)</a></li>',re.DOTALL).findall(links)
        for url,name in match:
                name = CLEAN(name)
                url = url+'/'
                AddDir(name,custurltv+url,81,'')
	
        xbmc.executebuiltin("Container.SetViewMode(50)")
			 
def GETSEASONSTV(name,url):

        SeasonPage = net.http_GET(url).content
        NotNeeded, SelectOut = SeasonPage.split("IMDB</a><br/>")
        SelectOut , NotNeeded = SelectOut.split('class="foot"')
        match=re.compile("<a href='/(.+?)'><strong>Episode</strong> (.+?)</a>").findall(str(SelectOut))
        for url,name in match:
             AddDir(name,custurltv+url,81,'')
	
        xbmc.executebuiltin("Container.SetViewMode(50)")

def GETTVSOURCES(name,url):
        SelectOut = net.http_GET(url).content
        SelectOut = regex_from_to(SelectOut, '<div id="linkname">', '</table>')
        SelectOut = SelectOut.replace(')','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
        all_genres = regex_get_all(SelectOut, '<ul id="linkname_nav">', '</a></li>')

        List=[]; ListU=[]; c=0
    	for a in all_genres:
                url = regex_from_to(a, 'http://', ';')
                Source = regex_from_to(a, ';">', '</a></li>').lstrip()
                c=c+1; List.append('Link Halow TV ['+str(c)+'] '+ Source); ListU.append(url)
        
        dialog=xbmcgui.Dialog()
        rNo=dialog.select('Halow Select A Source', List)
        if rNo>=0:
                rName=List[rNo]
                rURL=str("http://"+ListU[rNo])
                STREAMTV(name,rURL,'')
        else:
                pass
				
def STREAMTV(name,url3,thumb):
 #       xbmcgui.Dialog().ok(str(name), url3)
        url = url3
        try:
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                streamlink = urlresolver.resolve(urllib2.urlopen(req).url)
                addLinkMovies(name,streamlink,thumb)
        except:
                Notify('small','Sorry Link Removed:', 'Please try another one.',9000)

				
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("Halow Stream","Downloading")
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()

def TOP9(url):
         EnableMeta = metaset
         links = net.http_GET(url).content
         NotNeeded, links = links.split('<div class="banner_body">')
         links , NotNeeded = links.split('<div class="main">')
         links=links.replace('\r','').replace('\"','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
#        match=re.compile('<div class=pic_top_movie><a href="(.+?)" title=".+?"><img src=".+?" alt="(.+?)\(([\d]{4})\)"',re.DOTALL).findall(links)
       
         match=re.compile('<div class=pic_top_movie><a href=(.+?) title=(.+?)><img src=(.+?) alt=(.+?) width=90 height=130 /></a></div>',re.DOTALL).findall(links)
         for url,blank1,icon,name, in match:
                name = CLEAN(name)
                AddDir(name,custurl1+url,66,icon)

def INDEX(url):
        links = net.http_GET(url).content
        links=links.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
		
        pages=re.compile('found(.+?)/(.+?)Page').findall(links)
        nextpage=re.compile('<font color=#FF3300>.+?</font><a href=(.+?)>.+?</a>').findall(links)
#space here		
        NotNeeded, links = links.split('<li><a href="/western/">Western</a></li>')
        links , NotNeeded = links.split('<div class="count_text">')
        

        match=re.compile('<div class="movie_pic"><a href="(.+?)" target="_self" title="(.+?)"><img src="(.+?)" width="130" height="190" alt=',re.DOTALL).findall(links)

        
        

        for url,name,iconimage2 in match:
                name = CLEAN(name)
                AddDir(name,custurl1+url,66,iconimage2)

 
        if nextpage:
                print nextpage
                url = str(nextpage)
                print url
                url = url.replace('[u\'','')
                url = url.replace(']','')
                url = url.replace('\'','')
                print url
                AddDir('[B][COLOR red]Next...[/COLOR][/B]',custurl1+url,52,"http://s5.postimg.org/rmlrly3jb/next.png")



def VIDEOLINKS(name,url,iconimage):
        EnableMeta = metaset
        name2 = name
        links2 = net.http_GET(url).content
        links2 = links2.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','')
				  
        match2=re.compile('<h1>Links - Quality(.+?)</h1>').findall(links2)
        match=re.compile('<li id="playing_button"><a href="(.+?)" target="_blank"><span').findall(links2)
        if match2:
                quality = str(match2).replace('[','').replace(']','').replace("'",'').replace(' ','').replace('u','')
        else:
                quality = 'Not Specified'
        List=[]; ListU=[]; c=0

        for url in match:
                url = url.replace(')','')
                c=c+1; List.append('Link Halow ['+str(c)+'] '); ListU.append(url)
        dialog=xbmcgui.Dialog()
        rNo=dialog.select('Halow Select A Host Quality = %s'%quality, List)
        if rNo>=0:
                rName=List[rNo]
                rURL=ListU[rNo]
                STREAM(name2,custurl1+rURL,iconimage)
        else:
                pass

def STREAM(name,url,thumb):
        name2 = name
        url2 = url
        link = net.http_GET(url).content
        link = link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','')
#        match=re.compile('onclick="location.href=(.+?)"  value="Click Here to Download"').findall(link)
        match=re.compile('onclick="location.href=(.+?)" value="Click Here to Download"').findall(link)

        if match:
                print match
                url3 = str(match)
                url3 = url3.replace('[u\'','')
                url3 = url3.replace(']','')
                url3 = url3.replace(' ','')
                url3 = url3.replace('\'','')
                
#        xbmcgui.Dialog().ok(str(name), url3)
        print url3
        try:
                req = urllib2.Request(url3)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                url = url3				
                streamlink = urlresolver.resolve(urllib2.urlopen(req).url)
                addLinkMovies(name2,streamlink,thumb)
        except:
                Notify('small','Sorry Link Removed:', 'Please try another one.',9000)


def GETGENRES(url):
        GenresPage = net.http_GET(url).content
        GenresPage = GenresPage.encode('ascii', 'ignore').decode('ascii')
        NotNeeded, GenresPage = GenresPage.split('<div class="tv_letter_nav"><ul>')
        GenresPage , NotNeeded = GenresPage.split('<div class="tv_all">')
        GenresPage = GenresPage.replace('\"','').replace(')','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')

        match=re.compile("<a href=/(.+?)>(.+?)</a>",re.DOTALL).findall(str(GenresPage))
		
        for url,name in match:
                name = CLEAN(name)
                AddDir(name,custurltv+url,83,"http://www.iconarchive.com/download/i14263/hydrattz/multipurpose-alphabet/Letter-"+name[:1]+"-black.ico")

		
def ATOZ(url):
        AtoZPage = net.http_GET(url).content
        AtoZPage = AtoZPage.encode('ascii', 'ignore').decode('ascii') 
        print url
        AtoZPage = regex_from_to(AtoZPage, '<a href="/tv-listings/0-9">0-9</a>', '<div class="home">')
        AtoZPage = AtoZPage.replace('\"','').replace(')','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')

        match=re.compile("<a href=/(.+?)>(.+?)</a>",re.DOTALL).findall(str(AtoZPage))
		
        AddDir("Number 0-9",custurltv+"tv-listings/0-9",83,"http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg")
        for url,name in match:
                name = CLEAN(name)
                AddDir(name,custurltv+url,83,"http://www.iconarchive.com/download/i14263/hydrattz/multipurpose-alphabet/Letter-"+name[:1]+"-black.ico")
        xbmc.executebuiltin("Container.SetViewMode(500)")
		
def GETATOZLIST(name,url):
        ATOZLIST = net.http_GET(url).content
        ATOZLIST = ATOZLIST.encode('ascii', 'ignore').decode('ascii')
        print url
        ATOZLIST = regex_from_to(ATOZLIST, '<div class="home">', '</div>')

        ATOZLIST = ATOZLIST.replace('\"','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
        match=re.compile("<a href=/(.+?)>(.+?)</a>",re.DOTALL).findall(ATOZLIST)
#diaglog
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")
	   
        for url,name in match:
             AddDir(name,custurltv+url,84,'http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg')
             loadedLinks = loadedLinks + 1
             percent = (loadedLinks * 100)/totalLinks
             remaining_display = 'loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
             dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
             if dialogWait.iscanceled(): return False   
        dialogWait.close()
        del dialogWait
			 
def GETATOZSEASON(name,url):
        SeasonPage = net.http_GET(url).content
        NotNeeded, SeasonPage = SeasonPage.split('target="_blank">IMDB</a><br/>')
        SeasonPage , NotNeeded = SeasonPage.split('<div class="addthis">')
        SeasonPage = SeasonPage.replace('\"','').replace(')','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
        match=re.compile("<h3><a href=/(.+?)>(.+?)</a></h3>",re.DOTALL).findall(str(SeasonPage))
        for url,name in match:
             AddDir(name,custurltv+url,85,'http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg')
			 
def GETATOZEPISODE(name,url):
        EpisodePage = net.http_GET(url).content
        EpisodePage = EpisodePage.encode('ascii', 'ignore').decode('ascii')
        NotNeeded, EpisodePage = EpisodePage.split('target="_blank">IMDB</a><br/>')
        EpisodePage , NotNeeded = EpisodePage.split('<div class="addthis">')
        EpisodePage = EpisodePage.replace('\"','').replace(')','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
        match=re.compile("<a href=/(.+?)><strong>(.+?)</strong>(.+?)</a></li><li>",re.DOTALL).findall(str(EpisodePage))
        for url,Blank1,name in match:
             AddDir(name,custurltv+url,81,'')
      
def addLinkMovies(name,url,iconimage):
        download_enabled = 'False'
        print url
        ok=True
        try: addon.resolve_url(streamlink)
        except: pass
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo('Video', infoLabels={ "Title": name } )
        ###Download Context Menu
        contextMenuItems = []
        if download_enabled == 'true':
                contextMenuItems = []
                contextMenuItems.append(('Download', 'XBMC.RunPlugin(%s?mode=9&name=%s&url=%s)' % (sys.argv[0], name, urllib.quote_plus(url))))
                liz.addContextMenuItems(contextMenuItems, replaceItems=True)

        liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok
		
def SEARCHMOVIES():
        EnableMeta = metaset
        keyb = xbmc.Keyboard('', 'Search Halow TV Movies')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                encode = encode.replace('%20', '+')
                print encode
                url = custurl1+'search.php?key='+encode+'&submit='
                print url
                GetPage = net.http_GET(url).content
                NotNeeded, SelectOut = GetPage.split('<div class="left_body">')
                SelectOut , NotNeeded = SelectOut.split('<div class="count">')
				
                SelectOut=SelectOut.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')
                match=re.compile('<div class="movie_pic"><a href="(.+?)" target="_self" title="(.+?)"><img src="(.+?)" width="130" height="190" alt="(.+?)"></a>',re.DOTALL).findall(SelectOut)
                for url,name,iconimage2,iconimage3 in match:
                    name = CLEAN(name)
                    AddDir(name,custurl1+url,66,iconimage2)


							   
def Notify(typeq,title,message,times, line2='', line3=''):
     if typeq == 'small':
            smallicon= ""
            xbmc.executebuiltin("XBMC.Notification("+title+","+message+","''","+smallicon+")")
     elif typeq == 'big':
            dialog = xbmcgui.Dialog()
            dialog.ok(' '+title+' ', ' '+message+' ', line2, line3)
     else:
            dialog = xbmcgui.Dialog()
            dialog.ok(' '+title+' ', ' '+message+' ')

def OPEN_MAGIC(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent' , "Magic Browser")
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
	
def CLEAN(name):
        name = name.replace('&amp;','&')
        name = name.replace('&#x27;',"'")
        urllib.quote(u'\xe9'.encode('UTF-8'))
        name = name.replace(u'\xe9','e')
        urllib.quote(u'\xfa'.encode('UTF-8'))
        name = name.replace(u'\xfa','u')
        urllib.quote(u'\xed'.encode('UTF-8'))
        name = name.replace(u'\xed','i')
        urllib.quote(u'\xe4'.encode('UTF-8'))
        name = name.replace(u'\xe4','a')
        urllib.quote(u'\xf4'.encode('UTF-8'))
        name = name.replace(u'\xf4','o')
        urllib.quote(u'\u2013'.encode('UTF-8'))
        name = name.replace(u'\u2013','-')
        urllib.quote(u'\xe0'.encode('UTF-8'))
        name = name.replace(u'\xe0','a')
        try: name=messupText(name,True,True)
        except: pass
        try:name = name.decode('UTF-8').encode('UTF-8','ignore')
        except: pass
        return name

def PLAYLINK(name,url,iconimage):
        link = common.OpenURL(url)
        match=re.compile('hashkey=(.+?)">').findall(link)
        if len(match) == 0:
                match=re.compile("hashkey=(.+?)'>").findall(link)
        if (len(match) > 0):
                hashurl="http://videomega.tv/validatehash.php?hashkey="+ match[0]
                req = urllib2.Request(hashurl,None)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0')
                req.add_header('Referer', url)
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                match=re.compile('var ref="(.+?)"').findall(link)[0]
                videomega_url = 'http://videomega.tv/?ref='+match 
        else:
                match=re.compile("javascript'\>ref='(.+?)'").findall(link)[0]
                videomega_url = "http://videomega.tv/?ref=" + match
                
##RESOLVE##
        url = urlparse.urlparse(videomega_url).query
        url = urlparse.parse_qs(url)['ref'][0]
        url = 'http://videomega.tv/cdn.php?ref=%s' % url
        referer = videomega_url
        req = urllib2.Request(url,None)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        req.add_header('Referer', referer)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()

#remove
        url = re.compile('<source src="(.+?)" type="').findall(link)[-1]
        url = urllib.unquote_plus(url)
        print url
        stream_url = url
 #       stream_url = re.compile('file *: *"(.+?)"').findall(url)[0]
        playlist = xbmc.PlayList(1)
        playlist.clear()
        listitem = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
        listitem.setInfo("Video", {"Title":name})
        listitem.setProperty('mimetype', 'video/x-msvideo')
        listitem.setProperty('IsPlayable', 'true')
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
        xbmcPlayer.play(playlist)

def x1Channels(url):
    LocalisedLog = "aHR0cDovL2FwcC5kZXNpc3RyZWFtcy50di9EZXNpU3RyZWFtcy9pbmRleDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWw"
    url = str(base64.decodestring(LocalisedLog+"="))

    links = net.http_GET(url).content
    AddDir('[COLOR gold]-- If links stop working. Reload the bonus pack --[/COLOR]','Findus',0,"http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg")
    links = links.replace('\/','/')
    Mainurl = url[:26]
    
    all_videos = regex_get_all(links, '{"id"', '}')
    for a in all_videos:
        mode = 3
        url = regex_from_to(a, '"stream_url":"', '"')
        name = regex_from_to(a, 'name":"', '"')
        icon = regex_from_to(a, '"img":"', '",')
        AddDir('[COLOR blue] 1: '+name+' [/COLOR]' ,url, mode, Mainurl+icon, isFolder=False)
        url = regex_from_to(a, '"stream_url2":"', '"')
        name = regex_from_to(a, 'name":"', '"')
        icon = regex_from_to(a, '"img":"', '",')
        AddDir('[COLOR blue] 2: '+name+'[/COLOR]' ,url, mode, Mainurl+icon, isFolder=False)
        url = regex_from_to(a, '"stream_url3":"', '"')
        name = regex_from_to(a, 'name":"', '"')
        icon = regex_from_to(a, '"img":"', '",')
        AddDir('[COLOR blue] 3: '+name+'[/COLOR]' ,url, mode, Mainurl+icon, isFolder=False)
    
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    xbmc.executebuiltin("Container.SetViewMode(50)")
	
def PlxCategory(url):
	tmpList = []
	list = common.plx2list(url)
	background = list[0]["background"]
	for channel in list[1:]:
		iconimage = "" if not channel.has_key("thumb") else common.GetEncodeString(channel["thumb"])
		name = common.GetEncodeString(channel["name"])
		if channel["type"] == 'playlist':
			AddDir("[COLOR blue][{0}][/COLOR]".format(name) ,channel["url"], 1, iconimage, background=background)
		else:
			AddDir(name, channel["url"], 3, iconimage, isFolder=False, background=background)
			tmpList.append({"url": channel["url"], "image": iconimage, "name": name.decode("utf-8")})
			
	common.SaveList(tmpListFile, tmpList)
			
		
def AddDir(name, url, mode, iconimage, description='', isFolder=True, background=None):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)

	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
	liz.setProperty('fanart_image', iconimage)
	if mode == 1 or mode == 2:
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10008).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=22)'.format(sys.argv[0], urllib.quote_plus(url)))])
	elif mode == 3:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
	elif mode == 32:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10010).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
		
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def GetKeyboardText(title = "", defaultText = ""):
	keyboard = xbmc.Keyboard(defaultText, title)
	keyboard.doModal()
	text =  "" if not keyboard.isConfirmed() else keyboard.getText()
	return text

def GetSourceLocation(title, list):
	dialog = xbmcgui.Dialog()
	answer = dialog.select(title, list)
	return answer
	
def AddFavorites(url, iconimage, name):
	favList = common.ReadList(favoritesFile)
	for item in favList:
		if item["url"].lower() == url.lower():
			xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, name, localizedString(10011).encode('utf-8'), icon))
			return
    
	list = common.ReadList(tmpListFile)	
	for channel in list:
		if channel["name"].lower() == name.lower():
			url = channel["url"]
			iconimage = channel["image"]
			break
			
	if not iconimage:
		iconimage = ""
		
	data = {"url": url, "image": iconimage, "name": name.decode("utf-8")}
	
	favList.append(data)
	common.SaveList(favoritesFile, favList)
	xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, name, localizedString(10012).encode('utf-8'), icon))

def GETMOVIES(url,name):
        HDMoviePage = net.http_GET(url).content
        HDMoviePage = HDMoviePage.encode('ascii', 'ignore').decode('ascii')
        NotNeeded, HDMoviePage = HDMoviePage.split('<img src="//movieshd.co/file/movieshd.png" alt="MoviesHD"/>')
        HDMoviePage , NotNeeded = HDMoviePage.split('"Loading videos..."')
        HDMoviePage = HDMoviePage.replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','').replace('[','').replace(']','')

        match=re.compile('<img src="//(.+?)" alt="(.+?)" title="(.+?)"/><a href="(.+?)" title=').findall(HDMoviePage)
        items = len(match)

        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        xbmc.executebuiltin("XBMC.Dialog.Close(busydialog,true)")

        for thumb,Blank1,name,url in match:
                name2 = AAASTREAM_CODE(name)
                thumb = "http://"+thumb
                AAASTREAM_ADDCATDir(name2,url,100,thumb,len(match))
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                remaining_display = 'loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                if dialogWait.iscanceled(): return False 
				
        dialogWait.close()
        del dialogWait
				
        try:
                match=re.compile('"nextLink":"(.+?)"').findall(HDMoviePage)
                url= match[0]
                url = url.replace('\/','/')
#                xbmcgui.Dialog().ok('message', url)
                AAASTREAM_ADDCATDir('Next...',url,43,"http://s5.postimg.org/rmlrly3jb/next.png",items,isFolder=True)
        except: pass

        xbmc.executebuiltin("Container.SetViewMode(500)")
		
def GETMOVIESCATEGORIES(url):
#        xbmcgui.Dialog().ok('message', url)
        links = net.http_GET(url).content
        links = links.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\'','')

        match=re.compile('<img src="//(.+?)" alt="(.+?)" title="(.+?)"/><a href="(.+?)" title="(.+?)"><span>').findall(links)
		
        items = len(match)
        for thumb,alt,blank1,url,name in match:
                name2 = AAASTREAM_CODE(name)
                thumb2 = AAASTREAM_CODE(thumb)
                AddDir("[COLOR lime][B]"+ name2 +"[/B][/COLOR]",url,43 ,"http://"+thumb2)
				
        xbmc.executebuiltin("Container.SetViewMode(500)")


def AAASTREAM_CODE(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
	
def AAASTREAM_ADDCATDir(name,url,mode,thumb,itemcount,isFolder=False):
        if  LibCommon == 20:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&site="+str(site)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=thumb, thumbnailImage=thumb)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            liz.setProperty('fanart_image', thumb)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
            return ok
			
		


def RemoveFavorties(url):
	list = common.ReadList(favoritesFile) 
	for channel in list:
		if channel["url"].lower() == url.lower():
			list.remove(channel)
			break
			
	common.SaveList(favoritesFile, list)
	xbmc.executebuiltin("XBMC.Container.Refresh()")

def UpdateMe():
    url = ""

def RemoveFavorties(url):
	list = common.ReadList(favoritesFile) 
	for channel in list:
		if channel["url"].lower() == url.lower():
			list.remove(channel)
			break
			
	common.SaveList(favoritesFile, list)
	xbmc.executebuiltin("XBMC.Container.Refresh()")



def m3uCategory(url):
    tmpList = []
    list = common.m3u2list(url)
    for channel in list:
		name = common.GetEncodeString(channel["display_name"])
		mode = LibCommon + 26 if channel["url"].find("youtube") > 0 else 3
		AddDir(name ,channel["url"], mode, "http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg", isFolder=False)
		tmpList.append({"url": channel["url"], "image": "", "name": name.decode("utf-8")})

    common.SaveList(tmpListFile, tmpList)
    xbmc.executebuiltin("Container.SetViewMode(50)")

def Newsletter(url):
    tmpList = []
    list = common.m3u2list(url)
    for channel in list:
		name = common.GetEncodeString(channel["display_name"])
		mode = LibCommon + 26 if channel["url"].find("youtube") > 0 else 3
		AddDir(name ,channel["url"], mode, "http://i.ytimg.com/vi/yE4Jxq-3SrM/hqdefault.jpg", isFolder=False)
		tmpList.append({"url": channel["url"], "image": "", "name": name.decode("utf-8")})

    common.SaveList(tmpListFile, tmpList)
    xbmc.executebuiltin("Container.SetViewMode(50)")
	
def Suppliers(url):
    tmpList = []
    list = common.m3u2list(url)
    for channel in list:
		name = common.GetEncodeString(channel["display_name"])
		mode = LibCommon + 26 if channel["url"].find("youtube") > 0 else 3
		AddDir(name ,channel["url"], mode, "http://s5.postimg.org/mmv5t2nhj/newsletter.png", isFolder=False)
		tmpList.append({"url": channel["url"], "image": "", "name": name.decode("utf-8")})

    common.SaveList(tmpListFile, tmpList)
	
def ListFavorites():
	AddDir("[COLOR yellow][B]{0}[/B][/COLOR]".format(localizedString(10013).encode('utf-8')), "favorites" ,34 ,os.path.join(addonDir, "resources", "images", "bright_yellow_star.png"), isFolder=False)
	list = common.ReadList(favoritesFile)
	for channel in list:
		name = channel["name"].encode("utf-8")
		iconimage = channel["image"].encode("utf-8")
		AddDir(name, channel["url"], 32, iconimage, isFolder=False) 

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)

    xbmc.executebuiltin("Container.SetViewMode(true)")		
						
def AddNewFavortie():
	chName = GetKeyboardText("{0}".format(localizedString(10014).encode('utf-8'))).strip()
	if len(chName) < 1:
		return
	chUrl = GetKeyboardText("{0}".format(localizedString(10015).encode('utf-8'))).strip()
	if len(chUrl) < 1:
		return
		
	favList = common.ReadList(favoritesFile)
	for item in favList:
		if item["url"].lower() == url.lower():
			xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, chName, localizedString(10011).encode('utf-8'), icon))
			return
			
	data = {"url": chUrl, "image": "", "name": chName.decode("utf-8")}
	
	favList.append(data)
	if common.SaveList(favoritesFile, favList):
		xbmc.executebuiltin("XBMC.Container.Update('plugin://{0}?mode=30&url=favorites')".format(AddonID))

def PlayUrl(name, url, iconimage=None):
	print '--- Playing "{0}". {1}'.format(name, url)
	listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
	listitem.setInfo(type="Video", infoLabels={ "Title": name })
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
	
def PlayURLResolver(name,url,iconimage):
    import commonresolvers
    resolved=commonresolvers.get(url)    
    if resolved:
        if isinstance(resolved,list):
            for k in resolved:
                quality = addon.getSetting('quality')
                if k['quality'] == 'HD'  :
                    resolver = k['url']
                    break
                elif k['quality'] == 'SD' :
                    resolver = k['url']        
                elif k['quality'] == '1080p' and addon.getSetting('1080pquality') == 'true' :
                    resolver = k['url']
                    break
        else:
            resolver = resolved        
        playsetresolved(resolver,name,iconimage)
    else: 
        xbmc.executebuiltin("XBMC.Notification(AAA,Probably,this host is not supported or resolver is broken::,10000)")  

def playsetresolved(url,name,iconimage):
    liz = xbmcgui.ListItem(name, iconImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title':name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	
def regex_from_to(text, from_string, to_string, excluding=True):
    if excluding:
        r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
    else:
        r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
    return r

def regex_get_all(text, start_with, end_with):
    r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
    return r
	
def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring) >= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?','')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0].lower()] = splitparams[1]
	return param

	
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass
try:        
	mode = int(params["mode"])
except:
	pass
try:        
	description = urllib.unquote_plus(params["description"])
except:
	pass

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass

	
if mode == None or url == None or len(url) < 1:
	Categories()
elif mode == 1:
	PlxCategory(url)
elif mode == 2:
	m3uCategory(url)
elif mode == 3 or mode == 32:
#     PlayUrl(name, url, iconimage)
     PlayURLResolver(name,url,iconimage)
elif mode == 4:
    Newsletter(url)
elif mode == 5:
    StreamsList(url)
elif mode == 7:
    FootballTeams(url)
elif mode == 8:
	KidzCorner(url)
elif mode == 9:
	UFCSection(url)
elif mode == 10:
    x1Channels(url)
elif mode == 11:
	PlayYoutubeUser(url)
elif mode == 12:
    PlayURLResolver(name,url,iconimage)
elif mode == 15:
	UFCScrape(url)
elif mode == 16:
	StreamUFC(name,url,iconimage)
elif mode == 50:
    UpdateMe()
    xbmc.executebuiltin("UpdateLocalAddons")
    sys.exit()
elif mode == 31: 
	AddFavorites(url, iconimage, name) 
elif mode == 33:
	RemoveFavorties(url)
elif mode == 34:
	AddNewFavortie()
elif mode == 35:
	ADINDEX(url)	
elif mode == 41:
	common.DelFile(favoritesFile)
elif mode == 43:
    GETMOVIES(url,'Featured')
elif mode == 44:
	MOVIES()
elif mode == 45:	
	TV()
elif mode == 46 and len(url) > 21:
     xbmc.executebuiltin(url)
elif mode == 47 and LibCommon == 20:
	GETMOVIESCATEGORIES(url)
elif mode == 30:
	ListFavorites()
elif mode == 51:	
	TOP9(url)
elif mode == 52:	
	INDEX(url)
elif mode == 59:	
	GETLINKS(url)
elif mode == 66 and LibCommon == 20:	
	VIDEOLINKS(name,url,iconimage)
elif mode == 75 and LibCommon == 20:	
	LATESTADDED(url)
elif mode == 76 and LibCommon == 20:	
	NEWLINKS(url)
elif mode == 77 and LibCommon == 20:	
	NEWEPISODESTV(url)
elif mode == 78 and LibCommon == 20:	
	SEARCHTV(url)
elif mode == 79 and LibCommon == 20:	
	SEARCHMOVIES()
elif mode == 80 and LibCommon == 20:	
	GETSEASONSTV(name,url)
elif mode == 81 and LibCommon == 20:	
	GETTVSOURCES(name,url)
elif mode == 82 and LibCommon == 20:	
	ATOZ(url)
elif mode == 83 and LibCommon == 20:
	GETATOZLIST(name,url)
elif mode == 84 and LibCommon == 20:	
	GETATOZSEASON(name,url)
elif mode == 85 and LibCommon == 20:
	GETATOZEPISODE(name,url)
elif mode == 86 and LibCommon == 20:
	GETGENRES(url)
elif mode == 90 and LibCommon == 20:
	(name,url)
elif mode == 98 and LibCommon == 20:
    sys.exit()
elif mode == 99 and LibCommon == 20:
	Categories()
elif mode == 100 and LibCommon == 20:	
	PLAYLINK(name,url,iconimage)
elif mode == 101 and LibCommon == 20:
    MusicVideos(url)
elif mode == 102 and LibCommon == 20:
	Music_video_list(name,url)
elif mode == 103 and LibCommon == 20:	
	Music_video_genres(name,url)
elif mode == 104 and LibCommon == 20:
	Music_Charts_New(name,url)
elif mode == 105 and LibCommon == 20:
	video_artists(name,url)
elif mode == 106 and LibCommon == 20:
	Get_video_artists_AZ(name,url)
elif mode == 107 and LibCommon == 20:
	Music_artist_videos(name,url)
elif mode == 108 and LibCommon == 20:
	search_music_videos()
elif mode == 110 and LibCommon == 20:
	Music_play_video(name,url,iconimage)
elif mode == 150 and LibCommon == 20:
	REPLAYS()
elif mode == 151 and LibCommon == 20:
	FullMatches(url)
elif mode == 152 and LibCommon == 20:
	REPLAYSGETLINKS(name,url)
elif mode == 153 and LibCommon == 20:
	NEXTPAGE(page)
elif mode == 154 and LibCommon == 20: 
	SearchReplays()
elif mode == 155 and LibCommon == 20: 
	Highlights()
elif mode == 156 and LibCommon == 20: 
	PlayHighlights(name,url)
elif mode == 200 and LibCommon == 20: 	
	YouTube_List(url)
elif mode == 120:
    PLAYSTREAM(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

# h@k@M@c Code
