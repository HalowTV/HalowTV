# -*- coding: utf-8 -*-
import pyDes
import urllib
import re
from regexUtils import parseTextToGroups
from javascriptUtils import JsFunctions, JsUnpacker, JsUnpackerV2, JsUnpacker95High, JsUnwiser, JsUnIonCube, JsUnFunc, JsUnPP, JsUnPush
from hivelogic import hivelogic
try: import json
except ImportError: import simplejson as json
try: from Crypto.Cipher import AES
except ImportError: import pyaes as AES

def encryptDES_ECB(data, key):
    data = data.encode()
    k = pyDes.des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data)
    assert k.decrypt(d, padmode=pyDes.PAD_PKCS5) == data
    return d

def decryptDES_ECB(data, key):
    data = data.decode('base-64')
    k = pyDes.des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_PKCS5)
    return k.decrypt(data, padmode=pyDes.PAD_PKCS5)

def gAesDec(data, key):
    from mycrypt import decrypt
    return decrypt(key,data)

def cjsAesDec(data, key):
    from mycrypt import decrypt
    enc_data = json.loads(data.decode('base-64'))
    ciphertext = 'Salted__' + enc_data['s'].decode('hex') + enc_data['ct'].decode('base-64')
    return json.loads(decrypt(key,ciphertext.encode('base-64')))

def drenchDec(data, key):
    from drench import blowfish
    return blowfish(key).decrypt(data)

def wdecode(data):
    from itertools import chain
    
    in_data = re.split('\W+',data)
    pos = in_data.index(max(in_data,key=len))
    codec = "".join(chain(*zip(in_data[pos][:5], in_data[pos+1][:5], in_data[pos+2][:5])))
    data = "".join(chain(*zip(in_data[pos][5:], in_data[pos+1][5:], in_data[pos+2][5:])))
    
    ring = 0
    res = []
    for i in xrange(0,len(data),2):
        modifier = -1
        if (ord(codec[ring]) % 2):
            modifier = 1
        res.append( chr( int(data[i:i+2],36) - modifier ) )
        
        ring = ring + 1
        if ring >= len(codec):
            ring = 0
    return ''.join(res)

def onetv(playpath):
    import random,time,md5
    from base64 import b64encode
    user_agent = 'Mozilla%2F5.0%20%28Linux%3B%20Android%205.1.1%3B%20Nexus%205%20Build%2FLMY48B%3B%20wv%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Version%2F4.0%20Chrome%2F43.0.2357.65%20Mobile%20Safari%2F537.36'
    token = "65rSw"+"UzRad"
    servers = [ '176.31.231.58',
                '167.114.159.23',
                '167.114.159.80',
                '178.33.231.148',
                '5.196.86.78',
                '176.31.237.61',
                '192.99.149.33',
                '5.196.85.47',
                '37.59.17.46',
                '46.105.119.117',
                '51.254.43.148',
                '192.99.19.181',
                '5.196.85.58',
                '192.99.19.176']
    time_stamp = str(int(time.time()) + 14400)
    to_hash = "{0}{1}/hls/{2}".format(token,time_stamp,playpath)
    out_hash = b64encode(md5.new(to_hash).digest()).replace("+", "-").replace("/", "_").replace("=", "")
    server = random.choice(servers)
    
    url = "hls://http://{0}/p2p/{1}?st={2}&e={3}".format(server,playpath,out_hash,time_stamp)
    return '{url}|User-Agent={user_agent}&referer={referer}'.format(url=url,user_agent=user_agent,referer='6d6f6264726f2e6d65'.decode('hex'))
    

def encryptJimey(data):
    result = encryptDES_ECB(data,"PASSWORD").encode('base64').replace('/','').strip()
    return result

# used by 24cast
def destreamer(s):
    #remove all but[0-9A-Z]
    string = re.sub("[^0-9A-Z]", "", s.upper())
    result = ""
    nextchar = ""
    for i in range(0,len(string)-1):
        nextchar += string[i]
        if len(nextchar) == 2:
            result += ntos(int(nextchar,16))
            nextchar = ""
    return result

def ntos(n):
    n = hex(n)[2:]
    if len(n) == 1:
        n = "0" + n
    n = "%" + n
    return urllib.unquote(n)

def doDemystify(data):
    escape_again=False
    
    #init jsFunctions and jsUnpacker
    jsF = JsFunctions()
    jsU = JsUnpacker()
    jsU2 = JsUnpackerV2()
    jsUW = JsUnwiser()
    jsUI = JsUnIonCube()
    jsUF = JsUnFunc()
    jsUP = JsUnPP()
    jsU95 = JsUnpacker95High()
    JsPush = JsUnPush()
    JsHive = hivelogic()

    # replace NUL
    #data = data.replace('\0','')


    # unescape
    r = re.compile('a1=["\'](%3C(?=[^\'"]*%\w\w)[^\'"]+)["\']')
    while r.findall(data):
        for g in r.findall(data):
            quoted=g
            data = data.replace(quoted, urllib.unquote_plus(quoted))
    
    
    r = re.compile('unescape\(\s*["\']((?=[^\'"]*%\w\w)[^\'"]+)["\']')
    while r.findall(data):
        for g in r.findall(data):
            quoted=g
            data = data.replace(quoted, urllib.unquote_plus(quoted))
    
    r = re.compile('unescape\(\s*["\']((?=[^\'"]*\\u00)[^\'"]+)["\']')
    while r.findall(data):
        for g in r.findall(data):
            quoted=g
            data = data.replace(quoted, quoted.decode('unicode-escape'))

    r = re.compile('(\'\+dec\("\w+"\)\+\')')
    while r.findall(data):
        for g in r.findall(data):
            r2 = re.compile('dec\("(\w+)"\)')
            for dec_data in r2.findall(g):
                res = ''
                for i in dec_data:
                    res = res + chr(ord(i) ^ 123)
            data = data.replace(g, res)
            
    r = re.compile('((?:eval\(decodeURIComponent\(|window\.)atob\([\'"][^\'"]+[\'"]\)+)')
    while r.findall(data):
        for g in r.findall(data):
            r2 = re.compile('(?:eval\(decodeURIComponent\(|window\.)atob\([\'"]([^\'"]+)[\'"]\)+')
            for base64_data in r2.findall(g):
                data = data.replace(g, urllib.unquote(base64_data.decode('base-64')))
                
    r = re.compile('(<script.*?str=\'@.*?str.replace)')
    while r.findall(data):
        for g in r.findall(data):
            r2 = re.compile('.*?str=\'([^\']+)')
            for escape_data in r2.findall(g):
                data = data.replace(g, urllib.unquote(escape_data.replace('@','%')))
       
    r = re.compile('(base\([\'"]*[^\'"\)]+[\'"]*\))')
    while r.findall(data):
        for g in r.findall(data):
            r2 = re.compile('base\([\'"]*([^\'"\)]+)[\'"]*\)')
            for base64_data in r2.findall(g):
                data = data.replace(g, urllib.unquote(base64_data.decode('base-64')))
                escape_again=True
    
    r = re.compile('(eval\\(function\\((?!w)\w+,\w+,\w+,\w+.*?join\\(\'\'\\);*}\\(.*?\\))', flags=re.DOTALL)
    for g in r.findall(data):
        try:
            data = data.replace(g, wdecode(g))
            escape_again=True
        except:
            pass

    if '"result2":"'in data:
        r = re.compile(r""":("(?!http)\w+\.\w+\.m3u8")""")
        gs = r.findall(data)
        if gs:
            for g in gs:
                _in = json.loads(g).split('.')
                aes = AES.new('5e41564050447a7e4631795f33373037374f313337396d316862396c34654763'.decode('hex'), AES.MODE_CBC, _in[1].decode('hex'))
                unpad = lambda s : s[0:-ord(s[-1])]
                try:
                    _url = unpad(aes.decrypt(_in[0].decode('hex')))
                except:
                    _url = None
                if _url:
                    data = data.replace(g,json.dumps( _url ))
                else:
                    aes = AES.new('5e6d59405052757e4b65795f393738373831313335396d316775336c346e7472'.decode('hex'), AES.MODE_CBC, _in[1].decode('hex'))
                    data = data.replace(g,json.dumps( unpad(aes.decrypt(_in[0].decode('hex'))) ))
                
        r = re.compile(r""":("(?!http)[\w=\\/\+]+\.m3u8")""")
        gs = r.findall(data)
        if gs:
            for g in gs:
                data = data.replace(g,json.dumps(decryptDES_ECB(json.loads(g)[:-5], '5333637233742600'.decode('hex'))))

    # n98c4d2c
    if 'function n98c4d2c(' in data:
        gs = parseTextToGroups(data, ".*n98c4d2c\(''\).*?'(%[^']+)'.*")
        if gs != None and gs != []:
            data = data.replace(gs[0], jsF.n98c4d2c(gs[0]))
            
    if 'var enkripsi' in data:
        r = re.compile(r"""enkripsi="([^"]+)""")
        gs = r.findall(data)
        if gs:
            for g in gs:
                s=''
                for i in g:
                    s+= chr(ord(i)^2)
                data = data.replace("""enkripsi=\""""+g, urllib.unquote(s))
    # o61a2a8f
    if 'function o61a2a8f(' in data:
        gs = parseTextToGroups(data, ".*o61a2a8f\(''\).*?'(%[^']+)'.*")
        if gs != None and gs != []:
            data = data.replace(gs[0], jsF.o61a2a8f(gs[0]))

    # RrRrRrRr
    if 'function RrRrRrRr(' in data:
        r = re.compile("(RrRrRrRr\(\"(.*?)\"\);)</SCRIPT>", re.IGNORECASE + re.DOTALL)
        gs = r.findall(data)
        if gs != None and gs != []:
            for g in gs:
                data = data.replace(g[0], jsF.RrRrRrRr(g[1].replace('\\','')))

    # hp_d01
    if 'function hp_d01(' in data:
        r = re.compile("hp_d01\(unescape\(\"(.+?)\"\)\);//-->")
        gs = r.findall(data)
        if gs:
            for g in gs:
                data = data.replace(g, jsF.hp_d01(g))

    # ew_dc
    if 'function ew_dc(' in data:
        r = re.compile("ew_dc\(unescape\(\"(.+?)\"\)\);</SCRIPT>")
        gs = r.findall(data)
        if gs:
            for g in gs:
                data = data.replace(g, jsF.ew_dc(g))
                
     # pbbfa0
    if 'function pbbfa0(' in data:
        r = re.compile("pbbfa0\(''\).*?'(.+?)'.\+.unescape")
        gs = r.findall(data)
        if gs:
            for g in gs:
                data = data.replace(g, jsF.pbbfa0(g))
    
    if 'eval(function(' in data:
        data = re.sub(r"""function\(\w\w\w\w,\w\w\w\w,\w\w\w\w,\w\w\w\w""",'function(p,a,c,k)',data.replace('#','|'))
        data = re.sub(r"""\(\w\w\w\w\+0\)%\w\w\w\w""",'e%a',data)
        data = re.sub(r"""RegExp\(\w\w\w\w\(\w\w\w\w\)""",'RegExp(e(c)',data)
        r = re.compile(r"""\.split\('([^']+)'\)""")
        gs = r.findall(data)
        if gs:
            for g in gs:
                data = data.replace(g,'|')
        
    if """.replace(""" in data:
        r = re.compile(r""".replace\(["']([^"']+)["'],\s*["']([^"']*)["']\)""")
        gs = r.findall(data)
        if gs:
            for g in gs:
                data = data.replace(g[0],g[1])

    # util.de
    if 'Util.de' in data:
        r = re.compile("Util.de\(unescape\(['\"](.+?)['\"]\)\)")
        gs = r.findall(data)
        if gs:
            for g in gs:
                data = data.replace(g,g.decode('base64'))

    # 24cast
    if 'destreamer(' in data:
        r = re.compile("destreamer\(\"(.+?)\"\)")
        gs = r.findall(data)
        if gs:
            for g in gs:
                data = data.replace(g, destreamer(g))
                
    # JS P,A,C,K,E,D
    if jsU95.containsPacked(data):
        data = jsU95.unpackAll(data)
        escape_again=True
        
    if jsU2.containsPacked(data):
        data = jsU2.unpackAll(data)
        escape_again=True
    
    if jsU.containsPacked(data):
        data = jsU.unpackAll(data)
        escape_again=True

    # JS W,I,S,E
    if jsUW.containsWise(data):
        data = jsUW.unwiseAll(data)
        escape_again=True

    # JS IonCube
    if jsUI.containsIon(data):
        data = jsUI.unIonALL(data)
        escape_again=True
        
    # Js unFunc
    if jsUF.cointainUnFunc(data):
        data = jsUF.unFuncALL(data)
        escape_again=True
    
    if jsUP.containUnPP(data):
        data = jsUP.UnPPAll(data)
        escape_again=True
        
    if JsPush.containUnPush(data):
        data = JsPush.UnPush(data)

    if JsHive.contains_hivelogic(data):
        data = JsHive.unpack_hivelogic(data)

    # unescape again
    if escape_again:
        data = doDemystify(data)
    return data
