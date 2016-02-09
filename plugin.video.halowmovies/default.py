import sys,urllib,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,json
import requests
from addon.common.addon import Addon
from addon.common.net import Net
from metahandler import metahandlers


User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.halowmovies'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
metaset = selfAddon.getSetting('enable_meta')
con_trailer = selfAddon.getSetting('enable_trailers')
metaget = metahandlers.MetaData()
baseurl = 'http://hdmovie14.net'
net = Net()




def Halow():
        addDir('[B][COLOR white]Most Views[/COLOR][/B]',baseurl+'/list/most-view',1,icon,fanart,'')
        addDir('[B][COLOR white]Last Movies[/COLOR][/B]',baseurl+'/list/movie',1,icon,fanart,'')
        addDir('[B][COLOR white]TV SHOWS[/COLOR][/B]',baseurl+'/list/series',1,icon,fanart,'')
        addDir('[B][COLOR white]Category[/COLOR][/B]',baseurl,5,icon,fanart,'')
        addDir('[B][COLOR white]Countrys[/COLOR][/B]',baseurl,7,icon,fanart,'')
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',4,icon,fanart,'')




def INDEX(url):
        link = OPEN_URL(url)
        all_videos = regex_get_all(link, '<div data-content=', '</div></div></div>')
        items = len(all_videos)
        for a in all_videos:
                name = regex_from_to(a, '<h3>', '<').replace("&amp;","&").replace('&#39;',"'").replace('&quot;','"').replace('&#039;',"'")
                url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
                thumb = regex_from_to(a, 'src="', '"')
                seas = regex_from_to(a, '<p>', '<')
                if 'Season'not in seas:
                        if metaset=='true':
                                addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,baseurl+url,3,thumb,items)
                        else:
                                addDir('[B][COLOR red]%s[/COLOR][/B]' %name,baseurl+url,3,thumb,fanart,'')
                else:
                        addDir('[B][COLOR yellow]%s[/COLOR] : [I][COLOR blue]%s[/COLOR][/I][/B]' %(name,seas),baseurl+url,2,thumb,fanart,'') 
        try:
                np = re.compile('<a href="(.*?)".*?</a>').findall(link)[-2]
                addDir('[B][COLOR yellow]Next >[/COLOR][/B]',baseurl+np,1,icon,fanart,'')
        except: pass
        setView('movies', 'movie-view')




def Episode(url):
        link = OPEN_URL(url)
        addDir('[I][B][COLOR yellow]Episode[/COLOR][COLOR red] 1[/COLOR][/B][/I]' ,url,3,iconimage,fanart,'')
        all_links = regex_get_all(link, 'Select Episode		</div>', '</div>')
        all_videos = regex_get_all(str(all_links), 'button', 'button')
        try:
                for a in all_videos:
                        name = regex_from_to(a, 'episode">', '<')
                        url = regex_from_to(a, '\&quot;', '\&')
                        if name > '':
                                addDir('[I][B][COLOR blue]Episode[/COLOR][COLOR red] %s[/COLOR][/B][/I]' %name,baseurl+url,3,iconimage,fanart,'')
        except: pass
        try:
                all_links = regex_get_all(link, 'Select Season		</div>', '</div>')
                all_videos = regex_get_all(str(all_links), 'button', 'button')
                for a in all_videos:
                        name = regex_from_to(a, 'episode">', '<')
                        url = regex_from_to(a, '\&quot;', '\&')
                        if name > '':
                                addDir('[I][B][COLOR blue]Season[/COLOR][COLOR red] %s[/COLOR][/B][/I]' %name,baseurl+url,2,iconimage,fanart,'')
        except: pass
        setView('movies', 'movie-view')




def LINK(url):
        link = OPEN_URL(url)
        print url
        RequestURL = baseurl+re.findall(r'<ifram.*?rc="(.*?)".*?>', str(link), re.I|re.DOTALL)[-1]
        headers = {'host': 'hdmovie14.net', 'referer': url, 'user-agent': User_Agent}
        r = requests.get(RequestURL, headers=headers)
        r = requests.get(RequestURL, headers=headers, cookies=r.cookies)
        try:
                url = re.compile('"url":"(.*?)"').findall(str(r.text))[-1]
        except:
                url = re.compile('"url":"(.*?)"').findall(str(r.text))[0]
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setInfo(type='Video', infoLabels={'Title':description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(str(url))
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)




def SEARCH():
        keyb = xbmc.Keyboard('', 'Search')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','+')
                url = baseurl+'/search?key='+search
                INDEX(url)



def Category(url):
        link = OPEN_URL(url)
        match=re.compile('<a title="(.*?)" href="(.*?)">').findall(link) 
        for name,url in match:
                if '/category/' in url:
                        addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,baseurl+url,1,icon,fanart,'')




def COUNTRY(url):
        link = OPEN_URL(url)
        match=re.compile('<a title="(.*?)" href="(.*?)">').findall(link) 
        for name,url in match:
                if '/country/' in url:
                        addDir('[B][COLOR pink]%s[/COLOR][/B]' %name,baseurl+url,1,icon,fanart,'')




def YEAR(url):
        link = OPEN_URL(url)
        match=re.compile('<a title="(.*?)" href="(.*?)">').findall(link) 
        for name,url in match:
                if '/year/' in url:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,baseurl+url,1,icon,fanart,'')




def regex_from_to(text, from_string, to_string, excluding=True):
        if excluding:
                try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
                except: r = ''
        else:
                try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
                except: r = ''
        return r




def regex_get_all(text, start_with, end_with):
        r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
        return r




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




def addDir(name,url,mode,iconimage,fanart,description):
        name = name.replace('()','')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot":description} )
        liz.setProperty('fanart_image', fanart)
        if mode==3:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok




def PlayTrailer(url):
        addon.log('Play Trailer %s' % url)
        notification( addon.get_name(), 'fetching trailer', addon.get_icon())
        xbmc.executebuiltin("PlayMedia(%s)"%url)




def notification(title, message, icon):
        addon.show_small_popup( addon.get_name(), message.title(), 5000, icon)
        return




def addDir2(name,url,mode,iconimage,itemcount):
        name = name.replace('[B][COLOR white]','').replace('[/COLOR][/B]','')
        meta = metaget.get_meta('movie',name)
        if meta['cover_url']=='':
            try:
                meta['cover_url']=iconimage
            except:
                meta['cover_url']=icon
        name = '[B][COLOR white]' + name + '[/COLOR][/B]'
        meta['title'] = name
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&site="+str(site)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
        liz.setInfo( type="Video", infoLabels= meta )
        contextMenuItems = []
        if meta['trailer']:
                        contextMenuItems.append(('Play Trailer', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'mode': 8, 'url':meta['trailer']})))
                        #name = name+' '+' [COLOR gold][B][Trailer Available][/B][/COLOR]'
                        #meta['title'] = name 
        contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
        liz.addContextMenuItems(contextMenuItems, replaceItems=False)
        if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
        else: liz.setProperty('fanart_image', fanart)
        if mode==3:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False,totalItems=itemcount)
        else:
             ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True,totalItems=itemcount)
        return ok




def addLink(name,url,mode,iconimage,fanart,description=''):
        #u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        #ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok




def OPEN_URL(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = requests.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore').decode('ascii')
    return link




''' Why recode whats allready written and works well,
    Thanks go to Eldrado for it '''

def setView(content, viewType):
        
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if addon.get_setting('auto-view') == 'true':

        print addon.get_setting(viewType)
        if addon.get_setting(viewType) == 'Info':
            VT = '500'
        elif addon.get_setting(viewType) == 'Info2':
            VT = '500'
        elif addon.get_setting(viewType) == 'Info3':
            VT = '500'
        elif addon.get_setting(viewType) == 'Fanart':
            VT = '500'
        elif addon.get_setting(viewType) == 'Poster Wrap':
            VT = '500'
        elif addon.get_setting(viewType) == 'Big List':
            VT = '500'
        elif viewType == 'default-view':
            VT = addon.get_setting(viewType)

        print viewType
        print VT
        
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ( int(VT) ) )

    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_MPAA_RATING )




params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
site=None




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
        description=urllib.unquote_plus(params["description"])
except:
        pass




if mode==None or url==None or len(url)<1:
        Halow()

elif mode==1:
        INDEX(url)

elif mode==2:
        Episode(url)

elif mode==3:
        LINK(url)

elif mode==4:
        SEARCH()

elif mode==5:
        Category(url)

elif mode==6:
        YEAR(url)

elif mode==7:
        COUNTRY(url)

elif mode == 8:
        PlayTrailer(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
