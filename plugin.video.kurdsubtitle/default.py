import xbmcaddon, xbmc, xbmcgui, xbmcplugin
import requests, urllib, urllib2, re, urlparse
from os import path, system
from urllib2 import Request, URLError, urlopen
import sys, json, os
import unicodedata
import googledocs as gDocs
import commonresolvers as resolve
import urlresolver
from BeautifulSoup import BeautifulSoup


thisPlugin = int(sys.argv[1])
addonId = "plugin.video.cinama"
dataPath = xbmc.translatePath('special://profile/addon_data/%s' % (addonId))
addon = xbmcaddon.Addon()
addonInfo = xbmcaddon.Addon().getAddonInfo
progress = xbmcgui.DialogProgress()
path = addon.getAddonInfo('path')


###----Playing the stupid video---##
def playVideo(url):
    resolved = urlresolver.resolve(url)
    xbmc.log("resolved: " + repr(resolved))
    if resolved:
        url = resolved
    player = xbmc.Player()
    player.play(url)



# for get content for website
def getUrl(url, post='', referer=''):
    if post: req = urllib2.Request(url, post)
    else: req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    if referer:
      req.add_header('Referer', referer)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link







baseurl = 'http://www.kurdsubtitle.net/'
#Main menu#
def home():
    addDir3("Genres", "foo", 5, "", "","")
    addDir3("Years", "foo", 6, "", "","")
    addDir3("Search", "foo", 9, "", "", "")

def categories():
    r = requests.get(baseurl)
    html = BeautifulSoup(r.content)
    genres_ul = html.findAll("ul", attrs={'class':'genres scrolling'})[0]
    genres_lis = genres_ul.findAll('li')
    for genre in genres_lis:
        link = genre.findAll("a")[0]
        href = link["href"]
        name = link.text
        name = name.encode("utf-8")
        number_of_items = genre.findAll("i")[-1].text
        name = "({0}) {1}".format(number_of_items, name)
        if "tvshows" in str(url):
            addDir3(name,href,7,'','','')
        else:
            addDir3(name,href,2,'','','')

def years():
    r = requests.get(baseurl)
    html = BeautifulSoup(r.content)
    years_ul = html.findAll("ul", attrs={'class': 'year scrolling'})[0]
    years_lis = years_ul.findAll('li')
    for year in years_lis:
        link = year.findAll("a")[0]
        href = link["href"]
        name = link.text
        name = name.encode("utf-8")
        if "tvshows" in str(url):
            addDir3(name,href,7,'','','')
        else:
            addDir3(name, href, 2, '', '', '')

#Fix this nigguh <-- start here
def menu2(url):
    r = requests.get(url)
    html = BeautifulSoup(r.content)
    try:
        items_div = html.findAll("div", attrs={"class": "items"})[0]
    except:
        items_div = html.findAll("div", attrs={"class": "search"})[-1]
        xbmc.log("items_div: " + repr(items_div))
    movies = items_div.findAll("article")
    for movie in movies:
        poster = movie.findAll("div", attrs={"class": "poster"})[0]
        link = poster.findAll("a")[0]
        href = link["href"]
        image = link.findAll("img")[0]
        image_src = image["src"].split("?resize")[0]
        try:
            image_src.decode(encoding='UTF-8', errors='strict')
        except:
            image_src = iriToUri(image_src)
        xbmc.log("img_src: " + repr(image_src))
        try:
            name = image["alt"].encode("utf-8")
        except:
            name = movie.findAll("h3")[0].findAll("a")[0].text
        try:
            texto = movie.findAll("div", attrs={"class": "texto"})[0].contents[0].encode("utf-8")
        except:
            texto = ""
        if "/tvshows" in href:
            addDir3(name, href + '?tab=episodes',7,image_src,'',texto)
        else:
            addDir2(name, href + '?tab=video&player=option-1',  4, image_src,texto)
    try:
        pagination = html.findAll("div", attrs={"class": "pagination"})[0]
        yearstext = pagination.findAll("span")[0].text
        pages_info = re.findall("Page (\d+) of (\d+).*", yearstext)[0]
        current_page = int(pages_info[0])
        max_page = int(pages_info[1])
        if current_page < max_page:
            if "/page" in url:
                url = url.split("/page")[0]
            href = url + "/page/%s" % str(current_page + 1)
            addDir3("Next Page", href, 2, '','','')
    except:
        pass

def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)

def iriToUri(iri):
    parts= urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )

def tvseastit(url):
    r = requests.get(url)
    html = BeautifulSoup(r.content)
    seasons = html.findAll("div",attrs={"class":"se-c"})
    for season in seasons:
        seastitle = season.findAll("span",attrs={"class":"title"})[0].contents[0]
        addDir3(seastitle,url,8,'','','')
def tvep(url, season_name):
    r = requests.get(url)
    html = BeautifulSoup(r.content)
    seasons = html.findAll("div", attrs={"class": "se-c"})
    for season in seasons:
        seastitle = season.findAll("span",attrs={"class":"title"})[0].contents[0]
        if seastitle != season_name:
            continue
        episodes = season.findAll("ul", attrs={"class":"episodios"})
        episodes_list = episodes[0].findAll('li')
        for episode in episodes_list:
            eplink = episode.findAll("div",attrs={"class":"imagen"})[0]
            link = eplink.findAll("a")[0]
            href = link['href']
            image = link.findAll("img")[0]
            image_src = image['src']
            ep_number = episode.findAll("div",attrs=({"class":"numerando"}))[0].text.encode('utf-8')
            ep_title_div = episode.findAll("div",attrs=({"class":"episodiotitle"}))[0]
            ep_title = ep_title_div.findAll("a")[0].text.encode("utf-8")
            ep_date = ep_title_div.findAll("span", attrs={"class": "date"})[0].text
            name = "{0} - {1} ({2})".format(ep_number, ep_title, ep_date)
            addDir2(name,href,4,image_src,'')
def menu3(url):
    r = requests.get(url)
    regex = r'<iframe src="(.*?)"'
    match = re.compile(regex,re.DOTALL).findall(r.content)
    for link2 in match:
        addDir2('',link2,4,'')
def getResolve(url):
    regex = '\/\/(.+?)\/'
    match = re.compile(regex).findall(url)[0]

    regex = '(?:www.|)(.+?)\.'

    

    site = re.compile(regex).findall(match)[0]
    if site == 'drive': site = 'googledocs'
    urls = __import__('%s' % site, globals(), locals(), ['resolve'], -1)
    link = urls.resolve(url)
    return link




#-------------------test-------------------#
#####---GET STREAM URL and play that mofo---####

def getStream(url):
    content = getUrl(url)
    regex = '<iframe src="(.*?)"'
    link = re.compile(regex, re.DOTALL).findall(content)[0]
    xbmc.log("LIIIIINK %s "% link)
    if link.endswith("/preview"):
        link = link[:-8]
    try:
        #data = getResolve(link)
        
        #try:
        #    vLink = data[0]['url']
        #except:
        #    vLink = urls
        #playVideo(vLink)
        playVideo(link)
    except:
        pass




#----------------------------------Param BS----------------------#

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param       
#################################################################################################################

#                               NEED BELOW CHANGED

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
     
def addDir2(name,url,mode,iconimage,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description  } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def setView():
        xbmc.executebuiltin("Container.SetViewMode(500)")
 


              
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
xbmc.log("Mode: "+str(mode))
xbmc.log("URL: "+str(url))
xbmc.log("Name: "+str(name))

if mode==None or url==None or len(url)<1:
        print ""
        home()
elif mode==1:
        Open_URL()
elif mode==2:
        menu2(url)
elif mode==3:
        menu3(url)
elif mode==4:
        getStream(url)
elif mode==5:
        categories()
elif mode==6:
        years()
elif mode==7:
        tvseastit(url)
elif mode==8:
        tvep(url, name)
elif mode==9:
        search_title = xbmcgui.Dialog().input("Search")
        search_url = "http://www.kurdsubtitle.net/?s=%s" % urllib.quote_plus(search_title)
        menu2(search_url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))