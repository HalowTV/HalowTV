import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os
import datetime
from datetime import date
import time
from addon import Addon
from threading import Timer

addon_id='plugin.video.iptvmania.tv'
ADDON = xbmcaddon.Addon(id=addon_id)
ADDON_HELPER = Addon(addon_id, sys.argv)

base_url = 'http://iptvmania.tv'
api_url = 'http://api.iptvapi.com/api/v1/'
site_id = '27'
api_key = '562b2a59-64de-4416-bdff-e71d3e53787d'

# get parameters
mode = ADDON_HELPER.queries['mode']
play = ADDON_HELPER.queries.get('play', None)
image = ADDON_HELPER.queries.get('img', '')
title = ADDON_HELPER.queries.get('title', None)
dir_end = ADDON_HELPER.queries.get('dir_end', 'true')
dir_update = ADDON_HELPER.queries.get('dir_update', 'false')
url = ADDON_HELPER.queries.get('url', '')
referer = ADDON_HELPER.queries.get('referer', base_url)
channel_id = ADDON_HELPER.queries.get('channel_id', 0)
date = ADDON_HELPER.queries.get('date', None)
date_title = ADDON_HELPER.queries.get('date_title', '')

def Exit():
    xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
    xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
    
def APICALL(route, params={}):
    
    import time
    timestamp = int(time.time())
    
    params.update({'sid':site_id, 'language':'46', 'route':route, 'time':timestamp})
    #print params
    import urllib
    import hashlib
    params.update( {'hash':hashlib.sha1( hashlib.md5(urllib.urlencode(params)).hexdigest() + api_key).hexdigest()} )
    
    from urllib2 import Request, urlopen
    request = Request(api_url + route,urllib.urlencode(params))    
    api_return = urlopen(request).read()
    print api_return
    import json
    json_return = json.loads(api_return)
    
    if json_return['status'] != 'ok':
        raise Exception('api error')
    
    return json_return['params']

if ADDON.getSetting('user')=='':
    dialog = xbmcgui.Dialog()
    if dialog.yesno("IPTVMANIA", "If you dont already have an account, please sign up at:", "[COLOR royalblue]http://iptvmania.tv/en[/COLOR]", "", "Exit", "Continue"):
        
        dialog.ok("IPTVMANIA", "Please provide your email")
        keyboard = xbmc.Keyboard("", "IPTVMANIA - Please provide your email")
        keyboard.doModal()
        if keyboard.isConfirmed():
            user_input = keyboard.getText() 
        ADDON.setSetting('user',user_input)
        
        dialog.ok("IPTVMANIA", "Please provide your password")
        keyboard = xbmc.Keyboard("", "IPTVMANIA - Please provide your password")
        keyboard.doModal()
        if keyboard.isConfirmed():
            pwd_input = keyboard.getText() 
        ADDON.setSetting('pass',pwd_input)
    else:
        Exit()

user = ADDON.getSetting('user')
pwd = ADDON.getSetting('pass')        

datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
cookie_jar = os.path.join(datapath, "iptvmaniatv.lwp")


def get_user_id_and_token():
    params = {'email':user, 'password':pwd}
    json_return = APICALL('user/login', params)    
    return json_return['id'], json_return['session_token']

def get_channels_list():
    user_id, session_token = get_user_id_and_token()
    ADDON.setSetting('session_token',session_token)
    params = {'user_id':user_id, 'for_player':'1', 'for_orders':'0', 'include_favorites':'0','session_token':session_token}
    json_return = APICALL('user/ordered_channels', params)
    return json_return['items']


def get_stream_token():
    user_id, session_token = get_user_id_and_token()
    params = {'user_id':user_id, 'session_token':session_token}
    stream_token = APICALL('user/channel_token', params)
    return stream_token['stream_token']


def get_record_token():
    user_id, session_token = get_user_id_and_token()
    params = {'user_id':user_id, 'session_token':session_token}
    stream_token = APICALL('user/channel_token', params)
    return stream_token['stream_token'].split('token=')[1]


# TIMEZONE OFFSET
def get_gmt_offset():
    import time
    t = time.time()
    
    gmt_offset = 0
    
    if time.localtime(t).tm_isdst and time.daylight:
        gmt_offset = time.altzone
    else:
        gmt_offset = time.timezone
        
    gmt_offset = gmt_offset / 60 / 60 * -1
    
    return gmt_offset

def get_current_utc_date():
    time_zone_src = ADDON.getSetting('timezonesource')
    import time
    timestamp = int(time.time())
    time_zone = get_gmt_offset() if time_zone_src == '0' else int(ADDON.getSetting('timezone'))
    
    import datetime
    return (datetime.datetime.fromtimestamp(timestamp) + datetime.timedelta( hours= -1 * time_zone))

def get_recording(programme_id,date_title,date):
    items = []        
    session_token = ADDON.getSetting('session_token')

    params = {'time':date_title, 'programme':programme_id, 'date':str(date),'session_token':session_token}
    link  = APICALL('record/info', params)
    
    link = link['info'].items()
    for k , v in link:
        if k == 'url':
           return v



    #return json_return

def get_schedule_for_channel(channel_id, utc_date, beforeafter=False):
    items = []    
    import datetime
    session_token = ADDON.getSetting('session_token')
    if beforeafter == True:
        params = { 'channel':channel_id, 'date':(utc_date + datetime.timedelta(days=-1)).strftime("%Y-%m-%d"),'session_token':session_token}
        #print params
        json_return = APICALL('programme', params)
        if len(json_return['items']) > 0:
            items.extend( sorted(json_return['items'].items(), key=lambda(key,value): value['time_start']) )
        
    params = { 'channel':channel_id, 'date':utc_date.strftime("%Y-%m-%d"),'session_token':session_token}
    json_return = APICALL('programme', params)
    if len(json_return['items']) > 0:
        items.extend( sorted(json_return['items'].items(), key=lambda(key,value): value['time_start']) )
    
    if beforeafter == True:
        params = { 'channel':channel_id, 'date':(utc_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d"),'session_token':session_token}
        
        json_return = APICALL('programme', params)
        if len(json_return['items']) > 0:
            items.extend( sorted(json_return['items'].items(), key=lambda(key,value): value['time_start']) )
       
   
    return items

    
def date_str_to_datetime(utc_str_date):
    import datetime
    import time
    
    try:
        utc_date = datetime.datetime.strptime(utc_str_date, "%Y-%m-%d")
    except:
        utc_date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(utc_str_date, "%Y-%m-%d")))
        
    return utc_date

def GetSchedule(channel_id, schedule_utc_date=None, diff=0):
    
    import xbmc
    xbmc.executebuiltin( "ActivateWindow(busydialog)" )
    
    try:
        import datetime
        time_format = ADDON.getSetting('timeformat')
        time_zone_src = ADDON.getSetting('timezonesource')
        time_zone = get_gmt_offset() if time_zone_src == '0' else int(ADDON.getSetting('timezone'))
        str_time_format = '%I:%M %p' if time_format == '0' else '%H:%M'
        current_utc_datetime = get_current_utc_date() if not schedule_utc_date else date_str_to_datetime(schedule_utc_date)
        #########################################################################
        items = get_schedule_for_channel(channel_id, current_utc_datetime, True)
        #########################################################################
        current_tz_datetime = get_current_utc_date() + datetime.timedelta(hours=time_zone) 
        current_sch_tz_datetime = current_utc_datetime + datetime.timedelta(hours=time_zone)
        current_sch_tz_date = current_sch_tz_datetime.strftime('%Y-%m-%d')
        current_tz_date = current_tz_datetime.strftime('%Y-%m-%d')
        current_tz_datetime_minus_diff = current_tz_datetime  + datetime.timedelta(hours=(-1*diff)) 
        current_tz_datetime_plus_diff = current_tz_datetime  + datetime.timedelta(hours=diff) 

        next = False
        upcoming = False
        later = False
        time_zoned_list = []
        recordings = []

        import htmlcleaner
        for item in items:
            #print item
            sch = item[1]
            sch_utc_datetime = (datetime.datetime.utcfromtimestamp(sch['time_start']))            
            sch_utc_datetime_end = (datetime.datetime.utcfromtimestamp(sch['time_end']))
            sch_tz_datetime = sch_utc_datetime + datetime.timedelta(hours=time_zone) 
            sch_tz_datetime_end = sch_utc_datetime_end + datetime.timedelta(hours=time_zone) 
            sch_tz_date = sch_tz_datetime.strftime('%Y-%m-%d')
            if (diff == 0 and sch_tz_date == current_sch_tz_date) or ( diff != 0 and (sch_tz_datetime<=current_tz_datetime and sch_tz_datetime_end >= current_tz_datetime) or ( sch_tz_datetime >= current_tz_datetime and sch_tz_datetime_end <= current_tz_datetime_plus_diff)):

                item_text = sch_tz_datetime.strftime(str_time_format)  
                if current_tz_datetime > sch_tz_datetime_end:
                    item_text += ' - [COLOR white][REC][/COLOR]'
                elif sch_tz_datetime <= current_tz_datetime and current_tz_datetime <= sch_tz_datetime_end and next == False:
                    item_text += ' - [COLOR red][NOW][/COLOR]'
                    next = True
                elif next == True and upcoming==False:
                    item_text += ' - [COLOR gold][NXT][/COLOR]'
                    next = False
                    upcoming = True
                elif upcoming == True and later==False:
                    item_text += ' - [COLOR white][LTR][/COLOR]'
                    later = True
                #print sch['name']
                
                NAME = htmlcleaner.cleanUnicode(sch['name']).encode('utf8')
                recordings.append( ('', '', NAME,sch['id'],sch['time_start'],sch_tz_date)) 
                time_zoned_list.append( item_text + ' - ' + NAME) 
        
        xbmc.executebuiltin( "Dialog.Close(busydialog)" )
    except:
        xbmc.executebuiltin( "Dialog.Close(busydialog)" )
        raise
    
    return time_zoned_list, recordings 

def PopulateChannels():
    
    favs = ADDON.getSetting('favs')
    favs = favs.split(",")
    
    channels= get_channels_list()
    
    favoritesList = []
    channelList = []
    
    for cg_id, cg in channels.items():
        
        channelList.append ( ( {'mode':'dummy', 'title':cg['name']}, {'title' : "[COLOR yellow][B]" + cg['name'] + "[/COLOR][/B]"}, '', []) )
        for c_id, c in cg['channels'].items():
            #print c
            favMarker = ""
            
            if ADDON.getSetting('hls')=='true':                
                STREAM=c['link_m3u8'].replace('\/','/')+'?'#+stream_token                
            else:                
                STREAM=c['link_rtp'].replace('\/','/')+'?'#+stream_token

                
            contextMenuItems = []
            if c['name'] not in favs:
                contextMenuItems.append( ('[B][COLOR green]Add to addon favorites[/COLOR][/B]', 'RunPlugin(%s)' % ADDON_HELPER.build_plugin_url( {'mode':'add_fav', 'channel_id':c['id'], 'title': c['name'], 'url':c['url']}) ) )
            else:
                contextMenuItems.append( ('[B][COLOR red]Remove from addon favorites[/COLOR][/B]', 'RunPlugin(%s)' % ADDON_HELPER.build_plugin_url( {'mode':'remove_fav', 'channel_id':c['id'], 'title': c['name'], 'url':c['url']}) ) )
            contextMenuItems.append( ('[B][COLOR gold]Upcoming[/COLOR][/B]', 'RunPlugin(%s)' % ADDON_HELPER.build_plugin_url( {'mode':'upcoming', 'channel_id':c['id'], 'title': c['name']}) ) )
            contextMenuItems.append( ('[B][COLOR gold]Schedule[/COLOR][/B]', 'Container.Update(%s, True)' % ADDON_HELPER.build_plugin_url( {'mode':'schedule', 'channel_id':c['id'], 'title': c['name']}) ) )
            contextMenuItems.append( ('[B][COLOR gold]Recordings[/COLOR][/B]', 'Container.Update(%s, True)' % ADDON_HELPER.build_plugin_url( {'mode':'recordings', 'channel_id':c['id'], 'title': c['name']}) ) )
            
            if c['name'] in favs:
                favMarker = " [COLOR green][B]|*|[/B][/COLOR] "
                favoritesList.append ( ( {'mode':'live', 'play':'true', 'url':STREAM, 'title':c['name'], 'channel_id':c['id'] }, {'title': '.....' + c['name'] }, c['image'].replace('\/', '/'), contextMenuItems) )
            
            channelList.append ( ( {'mode':'live', 'play':'true', 'url':STREAM, 'title':c['name'], 'channel_id':c['id'] }, {'title': '.....' + favMarker + c['name'] }, c['image'].replace('\/', '/'), contextMenuItems) )
    
    ADDON_HELPER.add_directory( {'mode':'dummy'}, {'title':'[COLOR green][B]***** Favorite Channels *****[/B][/COLOR]'} )
    uniques= []
    if len(favoritesList) <= 0:
        ADDON_HELPER.add_directory( {'mode':'dummy'}, {'title':'[I]You have no favorites.[/I]'} )
    for params, title, img, cmi in  favoritesList:
        if title not in uniques:
            uniques.append(title)
            ADDON_HELPER.add_video_item( params, title, img=img, contextmenu_items=cmi )
    ADDON_HELPER.add_directory( {'mode':'dummy'}, {'title':' '} )
    ADDON_HELPER.add_directory( {'mode':'dummy'}, {'title':'[COLOR white][B]***** All Channels *****[/B][/COLOR]'} )
    for params, title, img, cmi in  channelList:
        ADDON_HELPER.add_video_item( params, title, img=img, contextmenu_items=cmi )

def ShowSchedule():
    import xbmcgui
    dialog = xbmcgui.Dialog()
    time_zoned_list, recordings = GetSchedule(channel_id, None, 20)       
    dialog.select(title, time_zoned_list)
    
if play:
    url=url+get_stream_token()
    listitem = xbmcgui.ListItem(path=url, iconImage=image, thumbnailImage=image)
    if title:
        listitem.setInfo("Video", {'title':title})
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)    
elif mode == 'main':
    PopulateChannels()
elif mode == 'DIALOG':
    dialog = xbmcgui.Dialog()
    dialog.ok( ADDON_HELPER.queries.get('dlg_title', "IPTVMANIA"), ADDON_HELPER.queries.get('dlg_line1', ''), 
        ADDON_HELPER.queries.get('dlg_line2', ''), ADDON_HELPER.queries.get('dlg_line3', '') )
elif mode == 'upcoming':
    ShowSchedule()
elif mode in ('schedule', 'recordings'):
    ADDON_HELPER.add_directory( {'mode':'dummy', 'title':title}, {'title':'[COLOR gold][B]***** ' + title + (' Recordings ' if mode=='recordings' else ' Schedule ') + '*****[/B][/COLOR]'} )
    if date:
        ADDON_HELPER.add_directory( {'mode':'dummy'}, {'title':'[COLOR royalblue][B] ' + date_title + '[/B][/COLOR]'} )    
    ADDON_HELPER.add_directory( {'mode':'dummy'}, {'title':' '} )
        
    if not date:        
        time_zone_src = ADDON.getSetting('timezonesource')
        time_zone = get_gmt_offset() if time_zone_src == '0' else int(ADDON.getSetting('timezone'))
        
        import datetime
        
        utc_datetime = get_current_utc_date()
        tz_datetime = utc_datetime + datetime.timedelta(hours=time_zone) 
        
        for i in range(0,20):
            utc_datetime_plus_i = utc_datetime + datetime.timedelta(days=( (-1 if mode=='recordings' else 1) *i))
            tz_datetime_plus_i = utc_datetime_plus_i + datetime.timedelta(hours=time_zone) 
            ADDON_HELPER.add_directory( {'mode':mode, 'channel_id':channel_id, 'title':title, 'date':utc_datetime_plus_i.strftime('%Y-%m-%d'), 'date_title':tz_datetime_plus_i.strftime('%A, %B %d')}, {'title':tz_datetime_plus_i.strftime('%A, %B %d')} )
            if mode == 'schedule' and i >=2: break
    else:
        time_zoned_list, recordings = GetSchedule(channel_id, date, 0)

        for idx,item in enumerate(time_zoned_list):
            recording = recordings[idx]

            #ADDON_HELPER.add_item( {'mode':'getrecording'}, {'title':item} , {'channel_id':str(recording[3])},{'date_title':str(recording[4])})
            u=sys.argv[0]+"?url="+urllib.quote_plus(str(recording[3]))+"&mode=getrecording&title="+urllib.quote_plus(item)+"&iconimage=None&date_title="+str(recording[4])+"&date="+str(recording[5])
            liz=xbmcgui.ListItem(item, iconImage="DefaultFolder.png", thumbnailImage='')
            liz.setInfo( type="Video", infoLabels={ "Title": item} )       
            liz.setProperty("IsPlayable","true")
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
      

elif mode == 'getrecording':
    
    stream_url = get_recording(url,date_title,date)
    liz = xbmcgui.ListItem(title, iconImage='DefaultVideo.png', thumbnailImage='')
    liz.setInfo(type='Video', infoLabels={'Title':title})
    liz.setProperty("IsPlayable","true")
    liz.setPath(stream_url+get_record_token())
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz) 
    
elif mode == "add_fav":
    favs = ADDON.getSetting('favs').split(",")
    if title in favs:
        ADDON_HELPER.show_small_popup("[COLOR white][B]iptvmania.tv[/B][/COLOR]", "Channel already in favorites.", image=".")
    else:
        favs.append(title)
        ADDON.setSetting('favs', ",".join(favs))
        ADDON_HELPER.show_small_popup("[COLOR white][B]iptvmania.tv[/B][/COLOR]", "Channel added to favorites.", image=".")
    xbmc.executebuiltin('Container.Refresh')
elif mode == "remove_fav":
    favs = ADDON.getSetting('favs').split(",")
    if title not in favs:
        ADDON_HELPER.show_small_popup("[COLOR white][B]iptvmania.tv[/B][/COLOR]", "Channel not in favorites.", image=".")
    else:
        favs.remove(title)
        ADDON.setSetting('favs', ",".join(favs))
        ADDON_HELPER.show_small_popup("[COLOR white][B]iptvmania.tv[/B][/COLOR]", "Channel removed from favorites.", image=".")
    xbmc.executebuiltin('Container.Refresh')
        
if mode != 'dummy' and dir_end == 'true':
    try: xbmcplugin.endOfDirectory(int(sys.argv[1]), updateListing=(dir_update=='true'))
    except: pass
