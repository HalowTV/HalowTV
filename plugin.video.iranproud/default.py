import xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin
from BeautifulSoup import BeautifulSoup
def CATEGORIES():
    addDir('list','lisst',4,'')




movlink = "http://www.iranproud2.net/irani-best-movies"




def menu1():
    r = requests.get('http://www.iranproud2.net/index.html')
    urlshit = ''
    #regex = r'<div id=".*?" class="fluid"><a href=".+?80(.*?)">.+?<div id="divTitrSS2" class="TitrSS">(.*?)</div></a>'
    regex = 'class="fluidButton"><a href.+?"(.*?)".+?(.*?)</a></div>'
    match = re.compile(regex,re.DOTALL).findall(r.content)
    for link,name in match:
        xbmc.log("LINK HERE --->>> %s "% link)
        addDir3(name.replace('target="_parent">',''),link.replace('http://www.iranproud2.net:80','').replace('/','http://www.iranproud2.net/'),3,'','','')

def lifetvmenu(url):
    r = requests.get(url)
    #regex = r'<div id="divTitrGrid2" class="titrGrid2">(.*?)</div>.+?<ul id="gridMason" class="gridMason effect-1">.+?<li><a href=".+?" target="_parent"><img src=".+?" alt="" width="100" height="160"></a></li>.+?</ul>'
    regex = r'<div id="divTitrGrid2" class="titrGrid2">(.*?)</div>'
    match = re.compile(regex,re.DOTALL).findall(r.content)
    for name2 in match:
        addDir3(name2.replace('&amp;','&'),'http://www.iranproud2.net/livetv',11,'','','')

def recrel(url):
    r = requests.get(url)
    regex = r'<div id="divTitrSS1" class="TitrSS">(.*?)</div>'
    match = re.compile(regex,re.DOTALL).findall(r.content)
    for name2 in match:
        if "musicvideo" in str(url):
            addDir3(name2.replace('&amp;','&'),'http://www.iranproud2.net/musicvideo',9,'','','')
def menu2(url):
    r = requests.get(url)
    regex = r'<div id="divTitrSS2" class="TitrSS">(.*?)</div>.+?<div id="divSutitrSS2" class="sutitrSS"><a href=".+?80(.*?)">VIEW ALL</a></div>'
    match = re.compile(regex,re.DOTALL).findall(r.content)
    for name2,link in match:
        if "musicvideo" in str(url):
            addDir3(name2.replace('&amp;','&'),"http://www.iranproud2.net%s"%link.replace('&amp;','&'),9,'','','')
        elif "iran-best-movies" in str(url):
            addDir3(name2.replace('&amp;','&'),"http://www.iranproud2.net%s"%link.replace('&amp;','&'),10,'','','')
        else:
            addDir3(name2.replace('&amp;','&'),"http://www.iranproud2.net%s"%link.replace('&amp;','&'),4,'','','')
def tsc(url):
    r = requests.get(url)
    regex = r'<div class="divBorder.*?"><a href=".+?80(.*?)"><img src="(.*?)" alt=""></a></div>.+?">.+?<div class="SSh.*?">(.*?)</div>.+?<'
    match = re.compile(regex,re.DOTALL).findall(r.content)
    for link,image,name3 in match:
        xbmc.log("3rd menu links --->>> %s "% match)
        addDir3(name3.replace('&amp;','&'),"http://www.iranproud2.net%s"%link.replace('" target="_parent','').replace('&amp;','&'),5,image,'','')
   
def musicvideo(url):
    r = requests.get(url)
     #<div class="divBorder?"><a href=".+?80(.*?)"><img src="(.*?)" alt=""></a></div>.+?">.+?<div class="SSh?">(.*?)</div>.+?<
    regex = r'<div class="divBorder"><a href="(.*?)" target="_parent"><img src="(.*?)" alt=""></a></div>.+?<div class="mask1M">.+?<div class="SSh1">(.*?)</div>'
    match = re.compile(regex,re.DOTALL).findall(r.content)
    for link,image,name3 in match:
        xbmc.log("3rd menu links --->>> %s "% match)
        addDir2(name3.replace('&amp;','&'),"http://www.iranproud2.net%s"%link.replace('" target="_parent','').replace('&amp;','&'),6,image)

def musicvideo2(url):
    r = requests.get(url)
    regex = r'<div class="divPicMask1 divPicMask1_musicvideos"><a href="#" target="_blank"><img src="(.*?)" alt="" width="210" height="160"></a>.+?<div class="SSh1">(.*?)</div>.+?<a href="(.*?)" target="_parent" class="infinA1">Watch Now</a>'
    match = re.compile(regex,re.DOTALL).findall(r.content)
    for image,name3,link in match:
        xbmc.log("3rd menu links --->>> %s "% match)
        addDir2(name3.replace('&amp;','&'),"http://www.iranproud2.net%s"%link.replace('" target="_parent','').replace('&amp;','&'),6,image)


def livetv(url):
   r = requests.get(url)
   regex = r'<li><a href="(.*?)" target="_parent"><img src="(.*?)" alt="" width="100" height="160"></a></li>'
   match = re.compile(regex,re.DOTALL).findall(r.content)
   for link,image in match:
    xbmc.log('LIVETV NOTICE:%s'%match)
    addDir2('test',"http://www.iranproud2.net%s"%link,6,image) 

#needs fixing nigguh
def movies(url):
    #html = '<html><div class="divBorder3"><a href="(.*?)" target="_parent"><img src="(.*?)" alt="" width="172" height="240"></a></div><div class="mask3M"><div class="SSh3">(.*?)</div>'
    html = BeautifulSoup(requests.get(url).text) # get the html
    grid = html.findAll("ul", attrs={'class': 'gridMasonMO'})[0] #find the ul with id gridMason4
    items = grid.findAll("li") # find all li items in the ul
    for item in items:  # for each item
        divborder = item.findAll("div", attrs={'class': 'divBorder3'})[0] #find the first div with class divborder 3
        href = divborder.findAll('a')[0]['href'] # find the link href in the div
        image = divborder.findAll('img')[0]['src'] #find the image src in the div
        ssh3 = item.findAll('div', attrs={'class': 'SSh3'})[0].text #get the text of the first div with class SSh3 in the li item
        xbmc.log('item:' + repr(item))
        addDir2(ssh3.replace('&amp;','&'),"http://www.iranproud2.net%s"%href.replace('" target="_parent','').replace('&amp;','&'),12,image)
 
def menu4(url):
    r = requests.get(url)
    regex = r'class="divBorder.*?"><a href="(.*?)".*?<img src="(.*?)" alt=.+?<div id="divEpiNo1" class="fluid">(.*?)</div>'
    match = re.compile(regex,re.DOTALL).findall(r.content)
    for link,image,name4 in match:
        xbmc.log("4th menu links --->>> %s "% match)
        addDir2(name4.replace('&amp;','&'),"http://www.iranproud2.net%s"%link.replace('" target="_parent','').replace('&amp;','&'),6,image)

def menu5(url):
    r = requests.get(url)
    regex = r'videosrc="(.*?)"'
    match = re.compile(regex).findall(r.content)
    for link in match:
        xbmc.log("link play this %s"%link)
        playVideo(link)

def menu6(url):
    r = requests.get(url)
    regex = r'video_url="(.*?)";'
    match = re.compile(regex).findall(r.content)
    for link in match:
        xbmc.log("link play this %s"%link)
        playVideo(link)    

###----Playing the stupid video---##
def playVideo(url):
    player = xbmc.Player()
    player.play(url)


#--------------Params---------#
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
     
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
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

def addLink(name,url,image,urltype,fanart):
  ok=True
  liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable','true')
  liz.setProperty('fanart_image', fanart)
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
  return ok

def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % viewType )
 


              
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
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        menu1()
       
elif mode==3:
        menu2(url)
        recrel(url)
        lifetvmenu(url)
elif mode==4:
        tsc(url)
        #tsc2(url)
elif mode==5:
        menu4(url)
elif mode==6:
        menu5(url)
elif mode==7:        
        playVideo(url)
elif mode==8:
        checkmenu(url)
elif mode==9:
        musicvideo(url)
        musicvideo2(url)
elif mode==10:
        movies(url)
elif mode==11:
        livetv(url)
elif mode==12:
        menu6(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
