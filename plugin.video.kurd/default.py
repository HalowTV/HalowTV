# -*- coding: utf-8 -*-
# please visit 
import xbmc,xbmcgui,xbmcplugin,sys
icons = "http://karwan.tv/images/tvlogo/"
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
    xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , KURDISH.TV ,5000,'+idx[2]+')')
    listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add(idx[0], listitem )
    xbmcPlayer.play(playlist,None,False)
    sys.exit(0)

def main():

    add_video_item('http://wpc.C1A9.edgecastcdn.net/hls-live/20C1A9/kurdsat/ls_satlink/b_528.m3u8'				,{ 'title': 'KurdSat TV'}, icons + 'kurdsat-tv.png')
    add_video_item('rtmp://68.168.105.117/live//livestream'	,{ 'title': 'KurdSat News'}, icons + 'kurdsat-news-tv.png')
    add_video_item('rtmp://84.244.187.12/live/livestream'			,{ 'title': 'Kurdistan TV'}, icons + 'kurdistan-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal10/_definst_/livestream/playlist.m3u8'				,{ 'title': 'Zagros TV'}, icons + 'zagros-tv.png')
    add_video_item('rtmp://prxy-wza-02.iptv-playoutcenter.de/nrt1/_definst_/mp4:nrt1.stream_1'					,{ 'title': 'NRT TV HD'}, icons + 'nalia-tv.png')
    add_video_item('rtmp://prxy-wza-02.iptv-playoutcenter.de/nrt2/_definst_/mp4:nrt2.stream_1'				,{ 'title': 'Nalia 2 TV HD'}, icons + 'nalia-2-tv.png')
    add_video_item('rtsp://livestreaming.itworkscdn.net/rudawlive/rudawtv'					,{ 'title': 'Rudaw TV'}, icons + 'rudaw.png')
    add_video_item('rtmp://51.254.209.160/live/livestream'						,{ 'title': 'KNN TV'}, icons + 'knn-tv.png')
    add_video_item('rtmp://64.150.177.45/live//mp4:myStream',{ 'title': 'Geli Kurdistan'}, icons + 'geli-kurdistan-tv.png')
    add_video_item('http://38.99.146.181:7777/KorekTV.m3u8'					,{ 'title': 'Korek TV'}, icons + 'korek-tv.png')
    add_video_item('http://live.kurdstream.net:1935/liveTrans//myStream_360p/playlist.m3u8'				,{ 'title': 'Kurd MAX TV'}, icons + 'kurdmax-tv.png')
    add_video_item('http://38.99.146.181:7777/Kanal4.m3u8'						,{ 'title': 'Kanal 4'}, icons + 'kanal4.png')
    add_video_item('rtmp://51.254.210.165/live/livestream'			,{ 'title': 'Amozhgary TV'}, icons + 'amozhgary-tv.png')
    add_video_item('http://63.237.48.23/ios/GEM_KURD/GEM_KURD.m3u8'			,{ 'title': 'GEM Kurd TV'}, icons + 'gem-kurd-tv.png')
    add_video_item('http://162.244.81.103:1935/RegaTV/myStream/playlist.m3u8'					,{ 'title': 'REGA TV'}, icons + 'rega-tv.png')
    add_video_item('http://38.99.146.181:7777/VINTV.m3u8'						,{ 'title': 'Vin TV'}, icons + 'vin-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal3/_definst_/livestream/playlist.m3u8'				,{ 'title': 'Newroz TV'}, icons + 'newroz-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal2/_definst_/livestream/playlist.m3u8'					,{ 'title': 'WAAR TV'}, icons + 'waar-tv.png')
    add_video_item(''		,{ 'title': 'WAAR Sport TV'}, icons + 'waar-sport-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal16/_definst_/livestream/playlist.m3u8'				,{ 'title': 'Ronahi TV'}, icons + 'ronahi-tv.png')
    add_video_item('http://kurd-live.com:1935/live/speda/chunklist_w557275510.m3u8'					,{ 'title': 'Speda TV'}, icons + 'speda-tv.png')
    add_video_item('http://cofafrw181.glwiz.com:7777/Cira.m3u8'					,{ 'title': 'Cira TV'}, icons + 'cira-tv.png')
    add_video_item('rtmp://payamlive.nanocdn.com/live/payam256'					,{ 'title': 'Payam TV'}, icons + 'payam-tv.png')
    add_video_item('http://cofafrw181.glwiz.com:7777/KurdChannel.m3u8'						,{ 'title': 'KM TV'}, icons + 'kmtv.png')
    add_video_item('http://cofafrw181.glwiz.com:7777/Pelistank.m3u8'			,{ 'title': 'PELISTANK TV'}, icons + 'pelistank-tv.png')
    add_video_item('http://live.kurdstream.net:1935/liveTrans/Pepule_360p/playlist.m3u8'					,{ 'title': 'KurdMax Pepule TV'}, icons + 'kurdmax-tv.png')
    add_video_item('http://balgurup.garantisistem.com:1935/Super_Tv/Super_Tv/playlist.m3u8'							,{ 'title': 'Super TV'}, icons + 'super-tv.png')
    add_video_item('rtmp://37.77.2.236/liveedge/live'							,{ 'title': 'Halk TV'}, icons + 'halk-tv.png')
    add_video_item('rtmp://gemtv.fms.visionip.tv/live/gemtv-gemtv-kurd-live-25f-4x3-SD'				,{ 'title': 'ABN Sat TV'}, icons + 'abn-sat-tv.PNG')
    add_video_item('http://origin.live.web.tv.streamprovider.net/streams/e3490d55c5dfc38e758ade69815cd9ef_live_0_0/index.m3u8'						,{ 'title': 'JIYAN TV'}, icons + 'Jiyan-T.png')
    add_video_item(''					,{ 'title': 'Tishk TV'}, icons + 'tishk-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal16/_definst_/livestream/playlist.m3u8'			,{ 'title': 'Rojhelat TV'}, icons + 'rojhelat.png')
    add_video_item('http://198.100.158.231:1935/kanal8/_definst_/livestream/playlist.m3u8'				,{ 'title': 'Komala TV'}, icons + 'komala-tv.png')
    add_video_item('rtmp://50.7.129.202:1935/batmantv<playpath>batmantv'					,{ 'title': 'Batman TV Express offlien now'}, icons + 'batman-tv-express.png')
    add_video_item('http://198.100.158.231:1935/kanal17/_definst_/livestream/playlist.m3u8'						,{ 'title': 'IMC TV'}, icons + 'imc-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal11/_definst_/livestream/playlist.m3u8'			,{ 'title': 'MED Nuce TV'}, icons + 'med-nuce-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal6/_definst_/livestream/playlist.m3u8'					,{ 'title': 'Sterk TV'}, icons + 'sterk-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal14/_definst_/livestream/playlist.m3u8'			,{ 'title': 'MED Muzik TV'}, icons + 'med-muzik-tv.png')
    add_video_item('rtmp://balgurup.garantisistem.com/Damla_Tv/Damla_Tv'					,{ 'title': 'Damla TV'}, icons + 'damla-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal1/_definst_/livestream/playlist.m3u8'						,{ 'title': 'TV 10'}, icons + 'tv-10.png')
    add_video_item('rtmp://178.254.20.205:2100/yol//yolstream'						,{ 'title': 'Yol TV'}, icons + 'yol-tv.png')
    add_video_item('rtmp://yayin3.canlitv.com/live/dengetv'					,{ 'title': 'Denge TV'}, icons + 'denge-tv.png')
    add_video_item('http://guntv.mediatriple.net/guntv/guntv2/Playlist.m3u8'								,{ 'title': 'Özgür Gün Tv'}, icons + 'ozgur-gun-tv-canli.png')
    add_video_item('rtmp://live1.karwan.tv/falcon-eye-tv1//falcon-eye-tv1.stream'				,{ 'title': 'Falcon Eye TV offlien now'}, icons + 'falcon-eye-tv.png')
    add_video_item('rtmp://kurd-live.com/live/cihan'                                                    ,{ 'title': 'Cihan TV'}, icons + 'cihan-tv')
    add_video_item('http://38.99.146.181:7777/AzadiTV.m3u8'                                                    ,{ 'title': 'Azadi TV TV'}, icons + 'azadi-tv')
    add_video_item('http://cofafrw181.glwiz.com:7777/Badinan.m3u8'                                                    ,{ 'title': 'Badinan Sat TV'}, icons + 'badinan-sat-tv')
    add_video_item('http://cofafrw181.glwiz.com:7777/Jamawar.m3u8'                                                    ,{ 'title': 'Jamawar TV '}, icons + 'jamawar-tv')
    add_video_item('http://origin2.live.web.tv.streamprovider.net/streams/894b55a9a7fa8f9b20da735e2112b034/index.m3u8'                                                    ,{ 'title': 'Havin TV '}, icons + 'havin-tv')
    add_video_item('http://origin.live.web.tv.streamprovider.net//streams//d9d7ee96913217bbc757f40d4de65c29_live_0_0//index.m3u8'                                                    ,{ 'title': 'Van TV'}, icons + 'van-tv')
    add_video_item('http://origin.live.web.tv.streamprovider.net//streams//8afa5b0b23429365abd7dbbb4ba22326_live_0_0//index.m3u8'                                                    ,{ 'title': 'HAYAT TV  '}, icons + 'hayat-tv')
    add_video_item('http://origin2.live.web.tv.streamprovider.net//streams//894b55a9a7fa8f9b20da735e2112b034//index.m3u8'                                                    ,{ 'title': 'Havin TV'}, icons + 'havin-tv')
    add_video_item('http://origin.live.web.tv.streamprovider.net//streams//04c042818579efb61acf6a75e6a02774//index.m3u8'                                                    ,{ 'title': 'Govend TV '}, icons + 'govend-tv')
    add_video_item('http://live.kurdstream.net:1935/liveTrans/Pepule_360p/playlist.m3u8'                                                    ,{ 'title': 'KurdMax Pepûle TV '}, icons + 'kurdmax-pepule-tv')
    add_video_item('http://38.99.146.181:7777/KirkukTV.m3u8'                                                    ,{ 'title': 'KIRKÛK TV ZINDÎ'}, icons + 'kirkuk-tv')
    add_video_item('rtmp://si.trtcdn.com/tv/trt6/mp4:trt6_3'                                                    ,{ 'title': 'TRT 6'}, icons + 'trt6-tv')
    
    # add_video_item(''				,{ 'title': ''}, icons + '')
    # add_video_item(''				,{ 'title': ''}, icons + '')
    # add_video_item(''				,{ 'title': ''}, icons + '')
    # add_video_item(''				,{ 'title': ''}, icons + '')

    xbmcplugin.endOfDirectory(plugin_handle)

if 'playkurd' in mode:
    iptvxtra_play()
else:
    main()
