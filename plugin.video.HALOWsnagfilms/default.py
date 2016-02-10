#!/usr/bin/python

import xbmc,xbmcplugin
import xbmcgui
import sys
import urllib, urllib2
import re
import httplib
import urlparse
from os import path, system
from urllib2 import Request, URLError, urlopen
import xbmcaddon
import unicodedata
import json
import os
# from resources.lib import xmltodict

host = "http://www.snagfilms.com/movies/kids_and_family"

thisPlugin = int(sys.argv[1])
addonId = "plugin.video.HALOWsnagfilms"
dataPath = xbmc.translatePath('special://profile/addon_data/%s' % (addonId))
addon = xbmcaddon.Addon()
addonInfo = xbmcaddon.Addon().getAddonInfo
path = addon.getAddonInfo('path')
pic = path+"/icon.png"
picNext = path+"/resources/media/next.jpg"
picSearch = path+"/resources/media/search.jpg"
picNo = path+"/resources/media/null.jpg"
picFanart = path+"/fanart.jpg"
progress = xbmcgui.DialogProgress()

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
    
def playVideo(url, title, pic):
    xlistitem = xbmcgui.ListItem( title, iconImage=pic, thumbnailImage=pic, path=url)
    xlistitem.setInfo( "video", { "Title": title } )
    player = xbmc.Player()
    player.play(url, xlistitem)

def gedebug(strTxt):
    print '######################################################'
    print '### GEDEBUG: ' + str(strTxt)
    print '######################################################'
    return

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
    except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))


def showMainMenu():
    addDirectoryItem("Popular", {"name":"Popular", "url":host, "mode":1}, pic)
    addDirectoryItem("Recent", {"name":"Recent", "url":host, "mode":1}, pic)

    xbmcplugin.endOfDirectory(thisPlugin)

def showFilmList(category):
    content = getUrl(host)
    regex = 'Snag.page.data.=.(.+)\;\n<\/script'
    match = re.compile(regex).findall(content)[0]
    jsonData = json.loads(match)

    for x in xrange(1,3):
        if category in jsonData[x]['title']:
            try:
                items = jsonData[x]['data']['items']
                # gedebug(items[0]['title'])
                for i in range(len(items)):
                    gedebug(items[i]['title'])
                    title = items[i]['title']
                    title = cleanHex(title)
                    url = items[i]['permalink']
                    thumbnail = items[i]['image']
                    addDirectoryItem(title, {"name":title, "url":url, "mode":2, "thumbnail":thumbnail}, thumbnail)
            except: pass
        pass
    xbmcplugin.endOfDirectory(thisPlugin)

def getStream(url, title, thumbnail):
    content = getUrl('http://www.snagfilms.com'+url)
    regex = 'iframe.*?src="(\/embed\/player?.+?)"'
    match = re.compile(regex).findall(content)[0]

    content = getUrl('http://www.snagfilms.com'+match)

    regex = 'file:."(.+?)",\n\s*label:.*?"(.+?)",'
    match = re.compile(regex).findall(content)

    for url, label in match:
        addDirectoryItem(label, {"name":title, "url":url, "mode":3, "thumbnail":thumbnail}, thumbnail)

    xbmcplugin.endOfDirectory(thisPlugin)



std_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100627 Firefox/3.6.6',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
}

def addDirectoryItem(name, parameters={},pic=""):
    li = xbmcgui.ListItem(name,iconImage="", thumbnailImage=pic)
    li.setInfo( "video", { "Title" : name, "FileName" : name} )
    li.setProperty('Fanart_Image', picFanart)
    url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)


def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

params = parameters_string_to_dict(sys.argv[2])
name =  str(params.get("name", ""))
name = urllib.unquote(name)
url =  str(params.get("url", ""))
url = urllib.unquote(url)
mode =  str(params.get("mode", ""))
postData =  str(params.get("postData", ""))
page =  str(params.get("page", 1))
thumbnail = str(params.get("thumbnail", ""))
thumbnail = urllib.unquote(thumbnail)

#### ACTIONS ####
if not sys.argv[2]:
    pass#print  "Here in default-py going in showContent"
    ok = showMainMenu()
else:
    if mode == str(1):
        ok = showFilmList(name)
    if mode == str(2):
        ok = getStream(url, name, thumbnail)
    if mode == str(3):
        ok = playVideo(url, name, thumbnail)
