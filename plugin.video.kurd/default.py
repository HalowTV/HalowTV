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
    xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , KURDISH.TV ,5000,'+idx[2]+')')
    listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add(idx[0], listitem )
    xbmcPlayer.play(playlist,None,False)
    sys.exit(0)

def main():
    add_video_item('http://wpc.c1a9.edgecastcdn.net/hls-live/20C1A9/kurdsat/ls_satlink/b_,264,528,828,.m3u8'	,{ 'title': 'KurdSat TV'}, icons + 'http://karwan.tv/images/tvlogo/kurdsat-tv.png')
    add_video_item('rtmp://68.168.105.117/live//livestream'	,{ 'title': 'KurdSat News'}, icons + 'http://karwan.tv/images/tvlogo/kurdsat-news-tv.png')
    add_video_item('rtmp://84.244.187.12/live/livestream'			,{ 'title': 'Kurdistan TV'}, icons + 'http://karwan.tv/images/tvlogo/kurdistan-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal10/_definst_/livestream/playlist.m3u8'				,{ 'title': 'Zagros TV'}, icons + 'http://karwan.tv/images/tvlogo/zagros-tv.png')
    add_video_item('rtmp://prxy-wza-02.iptv-playoutcenter.de/nrt1/_definst_/mp4:nrt1.stream_1'					,{ 'title': 'NRT TV HD'}, icons + 'http://karwan.tv/images/tvlogo/nalia-tv.png')
    add_video_item('rtmp://prxy-wza-02.iptv-playoutcenter.de/nrt2/_definst_/mp4:nrt2.stream_1'				,{ 'title': 'Nalia 2 TV HD'}, icons + 'http://karwan.tv/images/tvlogo/nalia-2-tv.png')
    add_video_item('rtsp://livestreaming.itworkscdn.net/rudawlive/rudawtv'					,{ 'title': 'Rudaw TV'}, icons + 'http://karwan.tv/images/tvlogo/rudaw.png')
    add_video_item('rtmp://51.254.209.160/live/livestream'						,{ 'title': 'KNN TV'}, icons + 'http://karwan.tv/images/tvlogo/knn-tv.png')
    add_video_item('rtmp://64.150.177.45/live//mp4:myStream',{ 'title': 'Geli Kurdistan'}, icons + 'http://karwan.tv/images/tvlogo/geli-kurdistan-tv.png')
    add_video_item('http://87.81.198.172:80/hls/mystream.m3u8'       ,{ 'title': 'ROJIKurd'}, icons + 'https://yt3.ggpht.com/-g9prY3S1fks/AAAAAAAAAAI/AAAAAAAAAAA/S-I2bl14JPc/s900-c-k-no/photo.jpg')
    add_video_item('http://62.210.100.139:1935/kurdistan24tv/smil:kurdistan24/chunklist_w888035107_b886000_slen.m3u8'	    ,{ 'title': 'kurdistan24 TV'}, icons + 'http://karwan.tv/images/tvlogo/kurdistan24-tv.png')
    add_video_item('http://live.kurdstream.net:1935/liveTrans//myStream_360p/playlist.m3u8'				,{ 'title': 'Kurd MAX TV'}, icons + 'http://karwan.tv/images/tvlogo/kurdmax-tv.png')
    add_video_item('http://63.237.48.23/ios/GEM_KURD/GEM_KURD.m3u8'			,{ 'title': 'GEM Kurd TV'}, icons + 'http://karwan.tv/images/tvlogo/gem-kurd-tv.png')
    add_video_item('http://38.117.88.153:7777/KorekTV/KorekTV_LR.m3u8?user=sgls4ddwrx45qvtqdc55rwvmhtmf&session=daa58d7aab4f4af12c652d17d9387a3a61b6156f4b3233c1a10474d5bdca29a8e30e201482969cf38a65537e32f96ab857442c670f6ece7e&hlsid=HTTP_ID_114417&group_id=-1&starttime=20151225T175450.343750' ,{ 'title': 'Korek TV'}, icons + 'http://karwan.tv/images/tvlogo/korek-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal12/_definst_/livestream/playlist.m3u8'						,{ 'title': 'Kanal 4'}, icons + 'http://karwan.tv/images/tvlogo/kanal4.png')
    add_video_item('http://stream-02.vty.dailymotion.com/31/dm/1/x32d5ky/live.isml/events(live-1454391224)/live-video=700000.m3u8'       ,{ 'title': 'Biaban Family HD'}, icons + 'http://ladda-upp.se/files/2016/b180019.jpg')
    add_video_item('http://kurd-live.com:1935/live/new/chunklist_w1304379760.m3u8'       ,{ 'title': 'New HD TV'}, icons + 'http://newlinehd.tv/images/logo.png')
    add_video_item('http://162.244.81.103:1935/RegaTV/myStream/playlist.m3u8'					,{ 'title': 'REGA TV'}, icons + 'http://karwan.tv/images/tvlogo/rega-tv.png')
    add_video_item('http://38.117.88.84:7777/VINTV/VINTV_LR.m3u8?user=sgls4ddwrx45qvtqdc55rwvmhtmf&session=daa9fe599c49f81d593b85e34a499fd068633648afc627b974679d1f9200a8de31a2d0e595b18b3a0d85789d53eb146633971f5d2e6620c8&hlsid=HLS_171118'	,{ 'title': 'Vin TV'}, icons + 'http://karwan.tv/images/tvlogo/vin-tv.png')
    add_video_item('http://38.117.88.153:7777/KirkukTV/KirkukTV_LR.m3u8?user=sglssap0pyfd4ly4wbbowu5liejb&session=ff42b3e559d5cb21df2fff98a81da21b3ac7c3e2f36c7dc0a875aa5792e84bfcf6496a5bf943e796368f817c85cb5f94d8131bd34a7e67a1de2a9a15d4e21705&hlsid=HTTP_ID_95055&group_id=-1&starttime=20151225T175450.343750' ,{ 'title': 'Kirkuk TV'}, icons + 'http://karwan.tv/images/tvlogo/kirkuk-tv.png')
    add_video_item('http://38.117.88.153:7777/Jamawar/Jamawar_LR.m3u8?user=sglssap0pyfd4ly4wbbowu5liejb&session=4c6efa823699dc0bcc35ef56ce2712ac61b6156f4b3233c1d421a39c32170cac27b3f61158cd7653df6bd10244ef1e26476103c1e3be1df6&hlsid=HTTP_ID_95239&group_id=-1&starttime=20151225T175450.328125'				,{ 'title': 'Jamawar TV'}, icons + 'http://karwan.tv/images/tvlogo/jamawar-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal3/_definst_/livestream/playlist.m3u8'				,{ 'title': 'Newroz TV'}, icons + 'http://karwan.tv/images/tvlogo/newroz-tv.png')
    add_video_item('http://avenuewtv.srfms.com:2219/live/livestream/playist.m3u8'					,{ 'title': 'WAAR TV'}, icons + 'http://karwan.tv/images/tvlogo/waar-tv.png')
    add_video_item('rtmp://51.254.210.165/live/livestream'			,{ 'title': 'Amozhgary TV'}, icons + 'http://karwan.tv/images/tvlogo/amozhgary-tv.png')
    add_video_item('rtmp://198.143.185.178:1935/live//speda'					,{ 'title': 'Speda TV'}, icons + 'http://karwan.tv/images/tvlogo/speda-tv.png')
    add_video_item('rtmp://payamlive.nanocdn.com/live/payam256'					,{ 'title': 'Payam TV'}, icons + 'http://karwan.tv/images/tvlogo/payam-tv.png')
    add_video_item('http://live4.karwan.tv:8081/karwan.tv/zarok-tv-1/chunks.m3u8?'              ,{ 'title': 'Zarok TV'}, icons + 'http://karwan.tv/images/tvlogo/zarok-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal18/_definst_/livestream/playlist.m3u8'			,{ 'title': 'PELISTANK TV'}, icons + 'http://karwan.tv/images/tvlogo/pelistank-tv.png')
    add_video_item('http://live.kurdstream.net:1935/liveTrans/Pepule_360p/playlist.m3u8'                                                    ,{ 'title': 'KurdMax Pepûle TV '}, icons + 'http://karwan.tv/images/tvlogo/kurdmax-pepule.png')
    add_video_item('http://62.210.100.139:1935/ciratv/smil:cira.smil/playlist.m3u8'		,{ 'title': 'Cira TV'}, icons + 'http://karwan.tv/images/tvlogo/cira-tv.png')
    add_video_item('rtmp://kurd-live.com/live/cihan'     ,{ 'title': 'Cihan TV'}, icons + 'http://karwan.tv/images/tvlogo/cihan-tv.png')
    add_video_item('http://origin2.live.web.tv.streamprovider.net/streams/4da1be863730bb975a52b3341be8f037/index.m3u8'							,{ 'title': 'Halk TV'}, icons + 'http://karwan.tv/images/tvlogo/halk-tv.png')
    add_video_item('http://origin.live.web.tv.streamprovider.net/streams/e3490d55c5dfc38e758ade69815cd9ef_live_0_0/index.m3u8'						,{ 'title': 'JIYAN TV'}, icons + 'http://karwan.tv/images/tvlogo/jiyan-tv.PNG')
    add_video_item(''					,{ 'title': 'Tishk TV'}, icons + 'http://karwan.tv/images/tvlogo/tishk-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal16/_definst_/livestream/playlist.m3u8'				,{ 'title': 'Ronahi TV'}, icons + 'http://karwan.tv/images/tvlogo/ronahi-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal16/_definst_/livestream/playlist.m3u8'			,{ 'title': 'Rojhelat TV'}, icons + 'http://karwan.tv/images/tvlogo/rojhelat.png')
    add_video_item('http://live4.karwan.tv:8081/karwan.tv/komala-tv.stream/chunks.m3u8'				,{ 'title': 'Komala TV'}, icons + 'http://karwan.tv/images/tvlogo/komala-tv.png')
    add_video_item('http://62.210.100.139:1935/imctv/smil:imc.smil/playlist.m3u8'						,{ 'title': 'IMC TV'}, icons + 'http://karwan.tv/images/tvlogo/imc-tv.png')
    add_video_item('http://stream-09.vty.dailymotion.com/08/dm/1/x31ptjl/live.isml/events(live-1452563831)/live-audio=128000-video=1200000.m3u8'			,{ 'title': 'MED Nuce TV'}, icons + 'http://karwan.tv/images/tvlogo/med-nuce-tv.png')
    add_video_item('http://62.210.100.139:1935/sterktv/smil:sterk/playlist.m3u8?'					,{ 'title': 'Sterk TV'}, icons + 'http://karwan.tv/images/tvlogo/sterk-tv.png')
    add_video_item('http://62.210.100.139:1935/medmuziktv/smil:medmuzik.smil/chunklist_w1912875585_b886000_slen.m3u8'			,{ 'title': 'MED Muzik TV'}, icons + 'http://karwan.tv/images/tvlogo/med-muzik-tv.png')
    add_video_item('http://origin.live.web.tv.streamprovider.net/streams/8c4a5bd6d3c5d3c21c11deb333bd4b7d/index.m3u8'					,{ 'title': 'Damla TV'}, icons + 'http://karwan.tv/images/tvlogo/damla-tv.png')
    add_video_item('http://198.100.158.231:1935/kanal1/_definst_/livestream/playlist.m3u8'						,{ 'title': 'TV 10'}, icons + 'http://karwan.tv/images/tvlogo/tv-10.png')
    add_video_item('http://live4.karwan.tv:8081/karwan.tv/komala-tv.stream/chunks.m3u8'						,{ 'title': 'KM TV'}, icons + 'http://karwan.tv/images/tvlogo/kmtv.png')
    add_video_item('rtmp://178.254.20.205:2100/yol//yolstream'						,{ 'title': 'Yol TV'}, icons + 'http://karwan.tv/images/tvlogo/yol-tv.png')
    add_video_item('rtmp://yayin3.canlitv.com/live/dengetv'					,{ 'title': 'Denge TV'}, icons + 'http://karwan.tv/images/tvlogo/denge-tv.png')
    add_video_item('http://live4.karwan.tv:8081/karwan.tv/ozgur-gun-tv/chunks.m3u8?'								,{ 'title': 'Özgür Gün Tv'}, icons + 'http://karwan.tv/images/tvlogo/oezguer-guen-tv.png')
    add_video_item('http://origin.live.web.tv.streamprovider.net/streams/415b828121291eb48f01cc26b98c14ff/index.m3u8'                                                    ,{ 'title': 'Azadi TV TV'}, icons + 'http://karwan.tv/images/tvlogo/azadi-tv.PNG')
    add_video_item('http://origin2.live.web.tv.streamprovider.net/streams/894b55a9a7fa8f9b20da735e2112b034/index.m3u8'                      ,{ 'title': 'Havin TV '}, icons + 'http://karwan.tv/images/tvlogo/havin-tv.png')
    add_video_item('http://origin.live.web.tv.streamprovider.net//streams//d9d7ee96913217bbc757f40d4de65c29_live_0_0//index.m3u8'           ,{ 'title': 'Van TV'}, icons + 'http://karwan.tv/images/tvlogo/van-tv.PNG')
    add_video_item('http://origin.live.web.tv.streamprovider.net//streams//8afa5b0b23429365abd7dbbb4ba22326_live_0_0//index.m3u8'           ,{ 'title': 'HAYAT TV  '}, icons + 'http://karwan.tv/images/tvlogo/hayat-tv.png')
    add_video_item('http://origin2.live.web.tv.streamprovider.net//streams//894b55a9a7fa8f9b20da735e2112b034//index.m3u8'                   ,{ 'title': 'Havin TV'}, icons + 'http://karwan.tv/images/tvlogo/havin-tv.png')
    add_video_item('http://origin.live.web.tv.streamprovider.net//streams//04c042818579efb61acf6a75e6a02774//index.m3u8'                    ,{ 'title': 'Govend TV '}, icons + 'http://karwan.tv/images/tvlogo/govend-tv.png')
    add_video_item('rtmp://si.trtcdn.com/tv/trt6/mp4:trt6_3'                                                    ,{ 'title': 'TRT 6'}, icons + 'https://kurdistancommentary.files.wordpress.com/2010/12/trt6.png')
    add_video_item('rtmp://fms.1830A.phicdn.net/201830A/kurdishInstance/KurdishHLS'                       ,{ 'title': 'Sahar TV'}, icons + 'https://kurdishgallery.files.wordpress.com/2011/02/sahar-tv1.jpg')
    add_video_item('http://live4.karwan.tv:8081/karwan.tv/qellat-tv/chunks.m3u8?'                       ,{ 'title': 'QELLAT TV'}, icons + 'http://karwan.tv/images/tvlogo/qellat-tv.png')
    add_video_item('http://live4.karwan.tv:8081/karwan.tv/badinan-sat-tv/chunks.m3u8?'                       ,{ 'title': 'Badinan Sat TV'}, icons + 'http://karwan.tv/images/tvlogo/badinan-sat-tv.png')
    add_video_item('http://live4.karwan.tv:8081/sardam-tv/sardam-tv/chunks.m3u8?'       ,{ 'title': 'Sardam TV'}, icons + 'http://karwan.tv/images/tvlogo/sardam-tv.PNG')
    add_video_item('http://89.163.255.18:2052/live/babo/chunklist_w1303061677.m3u8'    ,{ 'title': 'IMOVES 3D HD'}, icons + 'https://scontent-arn2-1.xx.fbcdn.net/hphotos-xat1/v/t1.0-9/12654187_495147467340029_7943857214277295984_n.jpg?oh=fe24ae64ceaa213abbab6b8c67fa76e0&oe=5735753B')


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
