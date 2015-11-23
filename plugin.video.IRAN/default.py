# -*- coding: utf-8 -*-
# please visit Halow TV

import xbmc,xbmcgui,xbmcplugin,sys,urllib2
from resources.lib.BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
icons = xbmc.translatePath("special://home/addons/plugin.video.Halow/resources/icons/")
icon = xbmc.translatePath("special://home/addons/plugin.video.Halow/icon.png")
plugin_handle = int(sys.argv[1])
mode = sys.argv[2]

	
def ginico(url):
    import resources.lib.requests as requests

    if 'xxx&User' in url:
        x = url.partition('xxx&User')
        url = x[0] + 'xxx'
    x = url.partition('---')
    url = x[0]
    id = x[2].replace('xxx','')

    r = requests.get("http://giniko.com/watch.php?id=" + id)
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    r = requests.get("http://giniko.com/watch.php?id=37")
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    r = requests.get("http://giniko.com/watch.php?id=220")
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    else: return url
	
def canlitvlive(url):
    import resources.lib.requests as requests
    r = requests.get(url)
    r = r.text.replace(' ','').strip()
    r = find_between(r,'file:"http','"')
    #r = 'http'+r+'|referer=http://www.canlitvlive.com/tvplayer.swf'
    r = 'http'+r+'|referer=http://www.canlitvlive.com/jwplayer.flash.swf'
    return r

def find_between(s,first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
	
def add_video_item(title,url,img):
    url = 'plugin://plugin.video.IRAN/?playtrk=' + url + '***' + title + '***' + img
    listitem = xbmcgui.ListItem(title, iconImage=img, thumbnailImage=img)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return

def addDir(name,url,iconimage):
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "Fanart_Image", icon )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def categorie():
    addDir('[COLOR red]ALL [COLOR yellow]IRAN CHANNELS [/COLOR]', 'plugin://plugin.video.IRAN/?xcat1x', "http://ittsgh.com/iptv/wp-content/uploads/sites/2/2014/11/channels_iran.jpg")
    addDir('[COLOR red]News[/COLOR]', 'plugin://plugin.video.IRAN/?xcat2x', "http://www.rokhshad.com/wp-content/uploads/2012/08/KhabarFarsi.jpg")
    addDir('[COLOR yellow]Entertainment[/COLOR]', 'plugin://plugin.video.IRAN/?xcat3x', "https://i1.ytimg.com/sh/GF4U1eOGV4s/showposter.jpg?v=50222cb1")
    addDir('[COLOR yellow]Political[/COLOR]', 'plugin://plugin.video.IRAN/?xcat4x', "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/State_flag_of_Iran_1964-1980.svg/120px-State_flag_of_Iran_1964-1980.svg.png")
    addDir('[COLOR yellow]IRIB[/COLOR]', 'plugin://plugin.video.IRAN/?xcat5x', "http://pounezar.ir/uploads/2015/02/IRIB-_-4.jpg")
    addDir('[COLOR yellow]GEM TVS[/COLOR]', 'plugin://plugin.video.IRAN/?xcat6x', "http://gemgroup.tv/wordpress/wp-content/uploads/2012/06/GEM-TV.png")
    addDir('[COLOR blue]www.streamaxit.tv[/COLOR]', 'plugin://plugin.video.IRAN/?xcat7x', "http://streamaxit.tv/portals/1/images/slider15.jpg")

    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
def playginico():
    xbmcPlayer = xbmc.Player()
    idx = mode.replace("?playtrk=", "").replace("###", "|").replace("#x#", "?").replace("#h#", "http://").split('***')
    xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , HalowTV ,5000,'+idx[2]+')')
    listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    if 'giniko' in idx[0]: url = ginico(idx[0])
    elif 'www.canlitvlive.com' in idx[0]: url = canlitvlive(idx[0])
    else: url = idx[0]
    playlist.add( url, listitem )
    xbmcPlayer.play(playlist,None,False)
    sys.exit(0)

def get_url(url):
        response = urllib2.urlopen(url)
        link=response.read()
        response.close()
        return link

def main():	
    xcat = 0
    if 'xcat1' in mode: 
        url = "http://pastebin.com/raw.php?i=S0dhY72L"
    elif 'xcat2' in mode: 
        url = "http://pastebin.com/raw.php?i=tqDBrFQb"
    elif 'xcat3' in mode: 
        url = "http://pastebin.com/raw.php?i=pmjj1sBX"
    elif 'xcat4' in mode: 
        url = "http://pastebin.com/raw.php?i=r3cjchek"
    elif 'xcat5' in mode: 
        url = "http://pastebin.com/raw.php?i=muKxz417"
    elif 'xcat6' in mode: 
        url = "http://pastebin.com/raw.php?i=9zxGjSDH"
    elif 'xcat7' in mode: 
        url = "http://pastebin.com/raw.php?i=wDphWaFz"
    else:
        categorie()
        sys.exit(0)


    link = get_url(url)
    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)

    items = soup.findAll("item")
    for item in items:
            try:
                videoTitle=item.title.string
            except: pass
            try:
                if item.thumbnail.string == 'none': thumbnail = icon	
                elif 'http://' in item.thumbnail.string: thumbnail = item.thumbnail.string 
                else: thumbnail = icons + item.thumbnail.string   
            except:
                thumbnail = icon
            try:
                url= item.link.string
            except: pass

            add_video_item(videoTitle,url,thumbnail)
    xbmcplugin.endOfDirectory(plugin_handle)
    sys.exit(0)


if 'playtrk' in mode:
    playginico()
else:
    main()
