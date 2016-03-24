import xbmc, xbmcgui, xbmcplugin
import urllib2,urllib,cgi, re, urlresolver  
import urlparse
import HTMLParser
import xbmcaddon
from operator import itemgetter
import traceback,cookielib
import base64,os,  binascii
import CustomPlayer,uuid
from time import time
import base64,sys
try:
    import json
except:
    import simplejson as json

__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
addon_id = 'plugin.video.sport365.live'
selfAddon = xbmcaddon.Addon(id=addon_id)
profile_path =  xbmc.translatePath(selfAddon.getAddonInfo('profile'))
S365COOKIEFILE='s365CookieFile.lwp'
S365COOKIEFILE=os.path.join(profile_path, S365COOKIEFILE)


def tr(param1 , param2 , param3):
    _loc4_ = 0;
    _loc5_= "";
    _loc6_ = None
    if( ord(param1[- 2]) == param2 and ord(param1[2]) == param3):
        _loc5_ = "";
        _loc4_ = len(param1)- 1;
        while(_loc4_ >= 0):
            _loc5_ = _loc5_ + param1[_loc4_]
            _loc4_-=1;
        param1 = _loc5_;
        _loc6_ = int(param1[-2:]);
        print 'xx',_loc6_
        param1 = param1[2:];
        param1 = param1[0:-3];
        _loc6_ = _loc6_ / 2;
        if(_loc6_ < len(param1)):
            _loc4_ = _loc6_;
        while(_loc4_ < len(param1)):
            param1 = param1[0:_loc4_]+ param1[_loc4_ + 1:]
            _loc4_ = _loc4_ + _loc6_ * 1;

        param1 = param1 + "!";

    return param1;

def swapme(st, fromstr , tostr):
    st=st.replace(tostr,"___")
    st=st.replace(fromstr,tostr)
    st=st.replace("___", fromstr)
    return st

     
def decode(encstring):
    encstring=tr(encstring ,114,65)
    mc_from="MD7cXIZxt5B61RHbN8dovGzW3C"
    mc_to="myilk4UpJfYLgn0u9eQwsVaT2="
    if 1==2:#encstring.endswith("!"):
        encstring=encstring[:-1]
        mc_from="ngU08IuldVHosTmZz9kYL2bayE"
        mc_to="v7ec41D6GpBtXx3QJRiN5WwMf="

    st=encstring
    for i in range(0,len(mc_from)):
        st=swapme(st, mc_from[i], mc_to[i])
    print st
    return st.decode("base64")
def getUrl(url, cookieJar=None,post=None, timeout=20, headers=None):

    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    #opener = urllib2.install_opener(opener)
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    if headers:
        for h,hv in headers:
            req.add_header(h,hv)

    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    return link;

def unwise_func( w, i, s, e):
    lIll = 0;
    ll1I = 0;
    Il1l = 0;
    ll1l = [];
    l1lI = [];
    while True:
        if (lIll < 5):
            l1lI.append(w[lIll])
        elif (lIll < len(w)):
            ll1l.append(w[lIll]);
        lIll+=1;
        if (ll1I < 5):
            l1lI.append(i[ll1I])
        elif (ll1I < len(i)):
            ll1l.append(i[ll1I])
        ll1I+=1;
        if (Il1l < 5):
            l1lI.append(s[Il1l])
        elif (Il1l < len(s)):
            ll1l.append(s[Il1l]);
        Il1l+=1;
        if (len(w) + len(i) + len(s) + len(e) == len(ll1l) + len(l1lI) + len(e)):
            break;

    lI1l = ''.join(ll1l)#.join('');
    I1lI = ''.join(l1lI)#.join('');
    ll1I = 0;
    l1ll = [];
    for lIll in range(0,len(ll1l),2):
        #print 'array i',lIll,len(ll1l)
        ll11 = -1;
        if ( ord(I1lI[ll1I]) % 2):
            ll11 = 1;
        #print 'val is ', lI1l[lIll: lIll+2]
        l1ll.append(chr(    int(lI1l[lIll: lIll+2], 36) - ll11));
        ll1I+=1;
        if (ll1I >= len(l1lI)):
            ll1I = 0;
    ret=''.join(l1ll)
    if 'eval(function(w,i,s,e)' in ret:
#        print 'STILL GOing'
        ret=re.compile('eval\(function\(w,i,s,e\).*}\((.*?)\)').findall(ret)[0]
        return get_unwise(ret)
    else:
#        print 'FINISHED'
        return ret
def get_unwise( str_eval):
    page_value=""
    try:
        ss="w,i,s,e=("+str_eval+')'
        exec (ss)
        page_value=unwise_func(w,i,s,e)
    except: traceback.print_exc(file=sys.stdout)
    #print 'unpacked',page_value
    return page_value  
def get365CookieJar(updatedUName=False):
    cookieJar=None
    try:
        cookieJar = cookielib.LWPCookieJar()
        if not updatedUName:
            cookieJar.load(S365COOKIEFILE,ignore_discard=True)
    except: 
        cookieJar=None

    if not cookieJar:
        cookieJar = cookielib.LWPCookieJar()
    return cookieJar    
def get365Key(cookieJar,url=None):
    headers=[('User-Agent','AppleCoreMedia/1.0.0.13A452 (iPhone; U; CPU OS 9_0_2 like Mac OS X; en_gb)')]
    if not url:
        mainhtml=getUrl("http://www.sport365.live/en/main",headers=headers, cookieJar=cookieJar)
        kurl=re.findall("src=\"(http.*?/wrapper.js.*?)\"",mainhtml)[0]
    else:
        kurl=url
    khtml=getUrl(kurl,headers=headers, cookieJar=cookieJar)
    kstr=re.compile('eval\(function\(w,i,s,e\).*}\((.*?)\)').findall(khtml)[0]
    kunc=get_unwise(kstr)
    print kunc    
    
    kkey=re.findall('aes_key="(.*?)"',kunc)
    kkey=re.findall('aes\(\)\{return "(.*?)"',kunc)
    return kkey[0]
def Colored(text = '', colorid = '', isBold = False):
    if colorid == 'ZM':
        color = 'FF11b500'
    elif colorid == 'EB':
        color = 'FFe37101'
    elif colorid == 'bold':
        return '[B]' + text + '[/B]'
    else:
        color = colorid
        
    if isBold == True:
        text = '[B]' + text + '[/B]'
    return '[COLOR ' + color + ']' + text + '[/COLOR]'	
def getLinks():
    cookieJar=get365CookieJar()
    kkey=get365Key(cookieJar)
    headers=[('User-Agent','AppleCoreMedia/1.0.0.13A452 (iPhone; U; CPU OS 9_0_2 like Mac OS X; en_gb)')]

    liveurl="http://www.sport365.live/en/events/-/1/-/-"+'/'+str(getutfoffset())
    linkshtml=getUrl(liveurl,headers=headers, cookieJar=cookieJar)
    reg="images\/types.*?(green|red).*?px;\">(.*?)<\/td><td style=\"borde.*?>(.*?)<\/td><td.*?>(.*?)<\/td.*?__showLinks.*?,.?\"(.*?)\".*?\">(.*?)<"
    sportslinks=re.findall(reg,linkshtml)
    print 'got links',sportslinks
    progress = xbmcgui.DialogProgress()
    progress.create('Progress', 'Fetching Live Links')
#    print sportslinks
    c=0
    cookieJar.save (S365COOKIEFILE,ignore_discard=True)

    import HTMLParser
    h = HTMLParser.HTMLParser()
    ret=[]
    import jscrypto
    for tp,tm,nm,lng,lnk,cat in sportslinks:
        c+=1
        cat=cat.split("/")[0]
        progress.update( (c*100/len(sportslinks)), "", "fetting links for "+nm, "" )
        try:    
            lnk=json.loads(lnk.decode("base64"))
            lnk=jscrypto.decode(lnk["ct"],kkey,lnk["s"].decode("hex"))
            #print lnk
            lnk=lnk.replace('\\/','/').replace('"',"")
         
            qty=""
            cat=cat.replace('&nbsp;','')
            lng=lng.replace('&nbsp;','')
            mm=nm.replace('&nbsp;','')
            #print nm,tp
            if 'span' in lng:
                lng=lng.split('>')
                qty=lng[-2].split('<')[0]
                lng= lng[-1]
            if len(lng)>0:
                lng=Colored("[" +lng+"]","orange")
            if len(qty)>0:
                qty=Colored("["+qty+"]","red")
                
            
            if not lnk.startswith("http"):
                lnk='http://www.sport365.live'+lnk
            #print lnk
            if tp=="green":
                lnk=base64.b64encode("Sports365:"+base64.b64encode(lnk))
                #addDir(Colored(cat.capitalize()+": "+tm+" : "+ qty+lng+nm  ,'ZM') ,lnk,11 ,"",isItFolder=False)
                ret+=[(cat.capitalize()+": "+tm+" : "+ qty+lng+nm ,lnk,True)]
            else:
                ret+=[(cat.capitalize()+": "+tm+" : "+ qty+lng+nm ,lnk,False)]
        except: traceback.print_exc(file=sys.stdout)
        progress.close()
    return ret
def total_seconds(dt):
    # Keep backward compatibility with Python 2.6 which doesn't have
    # this method
    import datetime
    if hasattr(datetime, 'total_seconds'):
        return dt.total_seconds()
    else:
        return (dt.microseconds + (dt.seconds + dt.days * 24 * 3600) * 10**6) / 10**6
        
def getutfoffset():
    import time
    from datetime import datetime

    ts = time.time()
    utc_offset = total_seconds((   datetime.fromtimestamp(ts)-datetime.utcfromtimestamp(ts)))/60
              
    return int(utc_offset)
    
def selectMatch(url):
    url=select365(url)
    if url=="": return 
    import HTMLParser
    h = HTMLParser.HTMLParser()

    #urlToPlay=base64.b64decode(url)
    cookieJar=get365CookieJar()
    html=getUrl(url,headers=[('Referer','http://www.sport365.live/en/main')],cookieJar=cookieJar)
    #print html
    reg="iframe frameborder=0.*?src=\"(.*?)\""
    linkurl=re.findall(reg,html)
    if len(linkurl)==0:
        reg="http://www.sport365.live.*?'\/(.*?)'\)"
        linkurl=re.findall(reg,html)[0]
        linkurl="http://www.sport365.live/en/player/f/"+linkurl
        html=getUrl(h.unescape(linkurl),cookieJar=cookieJar)
        reg="iframe frameborder=0.*?src=\"(.*?)\""
        linkurl=re.findall(reg,html)[0]
#        print linkurl
    else:
        linkurl=linkurl[0]
    enclinkhtml=getUrl(h.unescape(linkurl),cookieJar=cookieJar)
    reg='player_div", "st".*?file":"(.*?)"'
    enclink=re.findall(reg,enclinkhtml)
    usediv=False
    
    if len(enclink)==0:
        reg='name="f" value="(.*?)"'
        enclink=re.findall(reg,enclinkhtml)[0]  
        reg='name="s" value="(.*?)"'
        encst=re.findall(reg,enclinkhtml)[0]
        reg="\('action', ['\"](.*?)['\"]"
        postpage=re.findall(reg,enclinkhtml)
        if len(postpage)>0:
            
            reg='player_div", "st".*?file":"(.*?)"'
            post={'p':'http://cdn.adshell.net/swf/player.swf','s':encst,'f':enclink}
            post = urllib.urlencode(post)
            enclinkhtml2= getUrl(postpage[0],post=post, headers=[('Referer',linkurl),('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')])
            #enclink=re.findall(reg,enclinkhtml2)
            if 'player_div' in enclinkhtml2>0:
                usediv=True
                #enclinkhtml=enclinkhtml2
                #print 'usediv',usediv
                reg="player_div\",.?\"(.*?)\",.?\"(.*?)\",(.*?)\)"
                encst,enclink,isenc=re.findall(reg,enclinkhtml2)[0]
                #print 'encst,enclink',encst,enclink,isenc
                isenc=isenc.strip();
                if isenc=="1":
                    reg="src=\"(.*?\\/wrapper.js.*)\""
                    wrapurl=re.findall(reg,enclinkhtml2)[0]
                    kkey=get365Key(cookieJar,url=wrapurl)
                    #print 'kkey',kkey
                    enclink=json.loads(enclink.decode("base64"))
                    import jscrypto
                    lnk=jscrypto.decode(enclink["ct"],kkey,enclink["s"].decode("hex"))
                    
                    #print lnk
                    enclink=lnk
                #enclink=enclink[0]
                #print 'enclink',enclink
                #reg='player_div", "st":"(.*?)"'
                #encst=re.findall(reg,enclinkhtml)[0]
        
    else:
        usediv=True
        #print 'usediv',usediv
        enclink=enclink[0]
        #print 'enclink',enclink
        reg='player_div", "st":"(.*?)"'
        encst=re.findall(reg,enclinkhtml)[0]
    #if usediv:
    #    print 'usediv',usediv
    #    enclink=enclink[0]
    #    print 'enclink',enclink
    #    reg='player_div", "st":"(.*?)"'
    #    encst=re.findall(reg,enclinkhtml)[0]
        
    decodedst=decode(encst)

    #print encst, decodedst
    reg='"stkey":"(.*?)"'
    sitekey=re.findall(reg,decodedst)[0]
    #sitekey="myFhOWnjma1omjEf9jmH9WZg91CC"#hardcoded

    urlToPlay= decode(enclink.replace(sitekey,""))+"|Referer=%s&User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"%"http://h5.adshell.net/flash"
    return urlToPlay
def select365(url):
    print 'select365',url
    url=base64.b64decode(url)
    retUtl=""
    
    try:
        links=[]
        matchhtml=getUrl(url)        
        reg=".open\('(.*?)'.*?>(.*?)<"
        sourcelinks=re.findall(reg,matchhtml)
        b6=False

        enc=False
        if 1==2 and len(sourcelinks)==0:
            reg="showPopUpCode\\('(.*?)'.*?\\.write.*?d64\\(\\\\\\'(.*?)\\\\\\'\\)"
            sourcelinks=re.findall(reg,matchhtml)
            #print 'f',sourcelinks
            b6=True
        if 1==2 and len(sourcelinks)==0:
            reg="showPopUpCode\\('(.*?)'.*?\\.write.*?atob\\(\\\\\\'(.*?)\\\\\\'\\)"
            sourcelinks=re.findall(reg,matchhtml)
            #print 's',sourcelinks
            b6=True            
        if len(sourcelinks)==0:
            reg="showWindow\\('(.*?)',.*?>(.*?)<"
            sourcelinks=re.findall(reg,matchhtml)
            #print sourcelinks
            enc=True    
            b6=False
        if len(sourcelinks)==0:
            reg="showPopUpCode\\(.*?,.?'(.*?)'.*?,.*?,(.*?)\\)"
            sourcelinks=re.findall(reg,matchhtml)
            #print sourcelinks
            enc=True    
            b6=False
            
        #print 'sourcelinks',sourcelinks
        kkey=get365Key(get365CookieJar())
        if len(sourcelinks)==0:
            print 'No links',matchhtml
            #addDir(Colored("  -"+"No links available yet, Refresh 5 mins before start.",'') ,"" ,0,"", False, True,isItFolder=False)		#name,url,mode,icon
            return ""
        else:
            available_source=[]
            ino=0
            for curl,cname in sourcelinks:
                ino+=1
                try:
                    if b6:
                        curl,cname=cname,curl
                        #print b6,curl
                        curl=base64.b64decode(curl)
                        curl=re.findall('(http.*?)"',curl)[0]#+'/768/432'
                    if enc:
                        #print curl
                        curl=json.loads(curl.decode("base64"))
                        import jscrypto
                        #print curl["ct"],kkey,curl["s"]
                        curl=jscrypto.decode(curl["ct"],kkey,curl["s"].decode("hex"))
                        #print curl
                        curl=curl.replace('\\/','/').replace('"',"")
                        print 'fina;',curl
                        if 'window.atob' in curl:
                            reg="window\\.atob\(\\\\(.*?)\\\\\\)"
                            #print 'in regex',reg,curl
                            curl=re.findall(reg,curl)[0]
                            curl=base64.b64decode(curl)
                            curl=re.findall('(http.*?)"',curl)[0]#+'/768/432'
                            if not curl.split('/')[-2].isdigit():
                                curl+='/768/432'
                                
                    print curl
                    cname=cname.encode('ascii', 'ignore').decode('ascii')
                    #if not cname.startswith('link'):
                    cname='source# '+str(ino)
                    available_source.append(cname)
                    links+=[[cname,curl]]
                except:
                    traceback.print_exc(file=sys.stdout)
            if len(curl)==0:
                return ""
            if len(curl)==1:
                return links[0][1]
            dialog = xbmcgui.Dialog()
            index = dialog.select('Choose your link', available_source)
            if index > -1:
                return links[index][1]    

    except:
        traceback.print_exc(file=sys.stdout)
    return retUtl
