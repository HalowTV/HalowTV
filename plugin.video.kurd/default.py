# -*- coding: utf-8 -*-
# please visit 
import xbmc,xbmcgui,xbmcplugin,sys
icons = ""
icon = xbmc.translatePath("special://home/addons/plugin.video.karwan-kurdtv/icon.png")
plugin_handle = int(sys.argv[1])
mode = sys.argv[2]
	
def add_video_item(url, infolabels, img=''):
    if 'rtmp://' in url:
        url = url.replace('<playpath>',' playpath=')
        #url = url + ' swfUrl=http://onyxvids.stream.onyxservers.com/[[IMPORT]]/karwan.tv/player_file/flowplayer/player.cluster-3.2.9.swf pageUrl=http://karwan.tv/kurdistan-tv.html live=1'
        url = url + ' swfUrl=http://p.jwpcdn.com/6/11/jwplayer.flash.swf pageUrl=http://karwan.tv/sterk-tv.html live=1'
    url = 'plugin://plugin.video.kurd/?playkurd=' + url + '***' + infolabels['title'] + '***' + img
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return
	
def iptvxtra_play():
    xbmcPlayer = xbmc.Player()
    idx = mode.replace("?playkurd=", "").replace("###", "|").replace("#x#", "?").replace("#h#", "http://").split('***')
    xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , [COLOR green][B]HALOW  [COLOR red][B][TV][/B][/COLOR] ,5000,'+idx[2]+')')
    listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add(idx[0], listitem )
    xbmcPlayer.play(playlist,None,False)
    sys.exit(0)

def main():
    add_video_item('http://wpc.C1A9.edgecastcdn.net/hls-live/20C1A9/kurdsat/ls_satlink/b_528.m3u8'	,{ 'title': '[COLOR yellow][B]KurdSat TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/kurdsat-tv.png')
    add_video_item('rtmp://68.168.105.117/live//livestream'	,{ 'title': '[COLOR yellow][B]KurdSat News [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/kurdsat-news-tv.png')
    add_video_item('rtmp://84.244.187.12/live/livestream'			,{ 'title': '[COLOR yellow][B]Kurdistan TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/kurdistan-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal10/_definst_/livestream/playlist.m3u8' ,{ 'title': '[COLOR yellow][B]Zagros TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/zagros-tv.png')
    add_video_item('rtmp://prxy-wza-02.iptv-playoutcenter.de/nrt1/_definst_/mp4:nrt1.stream_1'	,{ 'title': '[COLOR yellow][B]NRT TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/nalia-tv.png')
    add_video_item('rtmp://prxy-wza-02.iptv-playoutcenter.de/nrt2/_definst_/mp4:nrt2.stream_1'	,{ 'title': '[COLOR yellow][B]NRT 2 [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/nalia-2-tv.png')
    add_video_item('rtsp://livestreaming.itworkscdn.net/rudawlive/rudawtv' ,{ 'title': '[COLOR yellow][B]Rudaw TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/rudaw.png')
    add_video_item('rtmp://51.254.209.160/live/livestream' ,{ 'title': '[COLOR yellow][B]KNN TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/knn-tv.png')
    add_video_item('rtmp://64.150.177.45/live//mp4:myStream',{ 'title': '[COLOR yellow][B]Geli Kurdistan [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/geli-kurdistan-tv.png')
    add_video_item('http://87.81.198.172:80/hls/mystream.m3u8'       ,{ 'title': '[COLOR yellow][B]ROJIKurd [COLOR red][B][HD][/B][/COLOR]'}, icons + 'https://yt3.ggpht.com/-g9prY3S1fks/AAAAAAAAAAI/AAAAAAAAAAA/S-I2bl14JPc/s900-c-k-no/photo.jpg')
    add_video_item('http://62.210.100.139:1935/kurdistan24tv/smil:kurdistan24/chunklist_w888035107_b886000_slen.m3u8'	    ,{ 'title': '[COLOR yellow][B]kurdistan24 TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/kurdistan24-tv.png')
    add_video_item('http://live.kurdstream.net:1935/liveTrans//myStream_360p/playlist.m3u8'				,{ 'title': '[COLOR yellow][B]Kurd MAX TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/kurdmax-tv.png')
    add_video_item('http://63.237.48.23/ios/GEM_KURD/GEM_KURD.m3u8'			,{ 'title': '[COLOR yellow][B]GEM Kurd TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/gem-kurd-tv.png')
    add_video_item('http://cofafrw181.glwiz.com:7777/KorekTV.m3u8?' ,{ 'title': '[COLOR yellow][B]Korek TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/korek-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal12/_definst_/livestream/playlist.m3u8' ,{ 'title': '[COLOR yellow][B]Kanal 4 [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/kanal4.png')
    add_video_item('http://kurd-live.com:1935/live/new/chunklist_w1304379760.m3u8'       ,{ 'title': '[COLOR yellow][B]New HD TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://newlinehd.tv/images/logo.png')
    add_video_item('http://38.99.146.150:7777/Rega.m3u8?' ,{ 'title': '[COLOR yellow][B]REGA TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/rega-tv.png')
    add_video_item('http://95.170.203.140:1213/hls/vinlive.m3u8'	,{ 'title': '[COLOR yellow][B]Vin TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/vin-tv.png')
    add_video_item('http://cofafrw181.glwiz.com:7777/KirkukTV.m3u8?' ,{ 'title': '[COLOR yellow][B]Kirkuk TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/kirkuk-tv.png')
    add_video_item('http://62.210.100.139:1935/newroztv/smil:newroz.smil/playlist.m3u8',{ 'title': '[COLOR yellow][B]Newroz TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/newroz-tv.png')
    add_video_item('rtmp://war471.srfms.com:2253/live//livestream',{ 'title': '[COLOR yellow][B]WAAR TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/waar-tv.png')
    add_video_item('rtmp://51.254.210.165/live/livestream' ,{ 'title': '[COLOR yellow][B]Amozhgary TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/amozhgary-tv.png')
    add_video_item('rtmp://198.143.185.178:1935/live//speda' ,{ 'title': '[COLOR yellow][B]Speda TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/speda-tv.png')
    add_video_item('rtmp://payamlive.nanocdn.com/live/payam256'	,{ 'title': '[COLOR yellow][B]Payam TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/payam-tv.png')
    #add_video_item('http://live4.karwan.tv:8081/karwan.tv/zarok-tv-1/chunks.m3u8?' ,{ 'title': '[COLOR yellow][B]Zarok TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/zarok-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal18/_definst_/livestream/playlist.m3u8' ,{ 'title': '[COLOR yellow][B]PELISTANK TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/pelistank-tv.png')
    add_video_item('http://live.kurdstream.net:1935/liveTrans/Pepule_360p/playlist.m3u8' ,{ 'title': '[COLOR yellow][B]KurdMax Pepûle TV [COLOR red][B][HD][/B][/COLOR] '}, icons + 'http://karwan.tv/images/tvlogo/kurdmax-pepule.png')
    add_video_item('http://62.210.100.139:1935/ciratv/smil:cira.smil/playlist.m3u8'		,{ 'title': '[COLOR yellow][B]Cira TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/cira-tv.png')
    add_video_item('rtmp://kurd-live.com/live/cihan'     ,{ 'title': '[COLOR yellow][B]Cihan TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/cihan-tv.png')
    add_video_item('http://live2.cdn.web.tv/streams/4da1be863730bb975a52b3341be8f037/index.m3u8?ttl=1457380120&sign=Zdl_z0WVpQI_Nw-pQHfDLQ'	,{ 'title': '[COLOR yellow][B]Halk TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/halk-tv.png')
    add_video_item('http://live1.cdn.web.tv/streams/e3490d55c5dfc38e758ade69815cd9ef_live_0_0/index.m3u8?ttl=1457380230&sign=xOULBtYELSj-3JKEsYaSYA' ,{ 'title': '[COLOR yellow][B]JIYAN TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/jiyan-tv.PNG')
    add_video_item(''	,{ 'title': '[COLOR yellow][B]Tishk TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/tishk-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal16/_definst_/livestream/playlist.m3u8'				,{ 'title': '[COLOR yellow][B]Ronahi TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/ronahi-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal16/_definst_/livestream/playlist.m3u8'			,{ 'title': '[COLOR yellow][B]Rojhelat TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/rojhelat.png')
    add_video_item('http://live4.karwan.tv:8081/karwan.tv/komala-tv.stream/chunks.m3u8'				,{ 'title': '[COLOR yellow][B]Komala TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/komala-tv.png')
    add_video_item('http://62.210.100.139:1935/imctv/smil:imc.smil/playlist.m3u8'						,{ 'title': '[COLOR yellow][B]IMC TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/imc-tv.png')
    add_video_item('http://62.210.100.139:1935/mednucetv/smil:mednuce.smil/chunklist_w199550435_b986000_DVR_slen.m3u8'    	,{ 'title': '[COLOR yellow][B]MED Nuce TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/med-nuce-tv.png')
    add_video_item('http://62.210.100.139:1935/sterktv/smil:sterk/playlist.m3u8?'					,{ 'title': '[COLOR yellow][B]Sterk TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/sterk-tv.png')
    add_video_item('http://62.210.100.139:1935/medmuziktv/smil:medmuzik.smil/chunklist_w1912875585_b886000_slen.m3u8'			,{ 'title': '[COLOR yellow][B]MED Muzik TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/med-muzik-tv.png')
    add_video_item('http://origin.live.web.tv.streamprovider.net/streams/8c4a5bd6d3c5d3c21c11deb333bd4b7d/index.m3u8'					,{ 'title': '[COLOR yellow][B]Damla TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/damla-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal1/_definst_/livestream/playlist.m3u8'						,{ 'title': '[COLOR yellow][B]TV 10 [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/tv-10.png')
    add_video_item('http://live4.karwan.tv:8081/karwan.tv/komala-tv.stream/chunks.m3u8'						,{ 'title': '[COLOR yellow][B]KM TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/kmtv.png')
    add_video_item('rtmp://178.254.20.205:2100/yol//yolstream'						,{ 'title': '[COLOR yellow][B]Yol TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/yol-tv.png')
    add_video_item('rtmp://yayin3.canlitv.com/live/dengetv'					,{ 'title': '[COLOR yellow][B]Denge TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/denge-tv.png')
    add_video_item('http://live4.karwan.tv:8081/karwan.tv/ozgur-gun-tv/chunks.m3u8?'	,{ 'title': '[COLOR yellow][B]Özgür Gün Tv [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/oezguer-guen-tv.png')
    add_video_item('http://origin.live.web.tv.streamprovider.net/streams/415b828121291eb48f01cc26b98c14ff/index.m3u8' ,{ 'title': '[COLOR yellow][B]Azadi TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/azadi-tv.PNG')
    add_video_item('http://origin2.live.web.tv.streamprovider.net/streams/894b55a9a7fa8f9b20da735e2112b034/index.m3u8'                      ,{ 'title': '[COLOR yellow][B]Havin TV [COLOR red][B][HD][/B][/COLOR] '}, icons + 'http://karwan.tv/images/tvlogo/havin-tv.png')
    add_video_item('http://origin.live.web.tv.streamprovider.net//streams//d9d7ee96913217bbc757f40d4de65c29_live_0_0//index.m3u8'           ,{ 'title': '[COLOR yellow][B]Van TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/van-tv.PNG')
    add_video_item('http://origin.live.web.tv.streamprovider.net//streams//8afa5b0b23429365abd7dbbb4ba22326_live_0_0//index.m3u8'           ,{ 'title': '[COLOR yellow][B]HAYAT TV [COLOR red][B][HD][/B][/COLOR]  '}, icons + 'http://karwan.tv/images/tvlogo/hayat-tv.png')
    add_video_item('http://origin2.live.web.tv.streamprovider.net//streams//894b55a9a7fa8f9b20da735e2112b034//index.m3u8'                   ,{ 'title': '[COLOR yellow][B]Havin TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/havin-tv.png')
    add_video_item('http://origin.live.web.tv.streamprovider.net//streams//04c042818579efb61acf6a75e6a02774//index.m3u8'                    ,{ 'title': '[COLOR yellow][B]Govend TV [COLOR red][B][HD][/B][/COLOR] '}, icons + 'http://karwan.tv/images/tvlogo/govend-tv.png')
    add_video_item('rtmp://si.trtcdn.com/tv/trt6/mp4:trt6_3'                                                    ,{ 'title': '[COLOR yellow][B]TRT 6 [COLOR red][B][HD][/B][/COLOR]'}, icons + 'https://kurdistancommentary.files.wordpress.com/2010/12/trt6.png')
    add_video_item('rtmp://fms.1830A.phicdn.net/201830A/kurdishInstance/KurdishHLS'                       ,{ 'title': '[COLOR yellow][B]Sahar TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'https://kurdishgallery.files.wordpress.com/2011/02/sahar-tv1.jpg')
    add_video_item('mms://77.36.241.3:1001'       ,{ 'title': '[COLOR yellow][B]Mahabad TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'https://upload.wikimedia.org/wikipedia/fa/c/cb/Mahabad_tv.png')

     #add_video_item('http://live4.karwan.tv:8081/karwan.tv/qellat-tv/chunks.m3u8?'                       ,{ 'title': '[COLOR yellow][B]QELLAT TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/qellat-tv.png')
     #add_video_item('http://live4.karwan.tv:8081/karwan.tv/badinan-sat-tv/chunks.m3u8?'  ,{ 'title': '[COLOR yellow][B]Badinan Sat TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/badinan-sat-tv.png')
     #add_video_item('http://live4.karwan.tv:8081/sardam-tv/sardam-tv/chunks.m3u8?'       ,{ 'title': '[COLOR yellow][B]Sardam TV [COLOR red][B][HD][/B][/COLOR]'}, icons + 'http://karwan.tv/images/tvlogo/sardam-tv.PNG')
     #add_video_item('http://live4.karwan.tv:8081/karwan.tv/mgc-tv/chunks.m3u8?'       ,{ 'title': 'MGC TV'}, icons + 'http://karwan.tv/images/tvlogo/mgc-tv.PNG')
     #add_video_item('http://live4.karwan.tv:8081/karwan.tv/farkli-tv/chunks.m3u8?'       ,{ 'title': 'FARKLI TV'}, icons + 'http://karwan.tv/images/tvlogo/farkli-tv.PNG')
     #add_video_item('http://live4.karwan.tv:8081/karwan.tv/tiviti-tv/chunks.m3u8?'       ,{ 'title': 'TİVİTİ TV'}, icons + 'http://karwan.tv/images/tvlogo/tiviti-tv.PNG')
     #add_video_item('http://live4.karwan.tv:8081/karwan.tv/abn-sat-tv-kurdish/chunks.m3u8?'       ,{ 'title': 'ABN Sat TV '}, icons + 'http://karwan.tv/images/tvlogo/abn-sat-tv.PNG')
     #add_video_item('http://live4.karwan.tv:8081/karwan.tv/super-tv/chunks.m3u8'       ,{ 'title': 'Super TV'}, icons + 'http://karwan.tv/images/tvlogo/super-tv.png')
     #add_video_item('http://live4.karwan.tv:8081/karwan.tv/ishtar-tv/chunks.m3u8?'       ,{ 'title': 'ISHTAR TV'}, icons + 'http://karwan.tv/images/tvlogo/ishtar-tv.png')


    # add_video_item(''				,{ 'title': ''}, icons + '')
    # add_video_item(''				,{ 'title': ''}, icons + '')
    # add_video_item(''				,{ 'title': ''}, icons + '')
    # add_video_item(''				,{ 'title': ''}, icons + '')

    xbmcplugin.endOfDirectory(plugin_handle)

if 'playkurd' in mode:
    iptvxtra_play()
else:
    main()
