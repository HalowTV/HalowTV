# -*- coding: utf-8 -*-

import urllib
import urlparse
import re, datetime
import socket


import common

from utils import datetimeUtils as dt
from utils import regexUtils as reg
from utils import xppod as xp

from utils.xbmcUtils import select
from utils.fileUtils import getFileContent, fileExists


def __parseParams(params):
    seperator = "','"
    arr = params.split(seperator)
    for ndx, member in enumerate(arr):
        arr[ndx] = member.strip("'")
    return arr


def replaceFromDict(dictFilePath, wrd):

    dictionary = getFileContent(dictFilePath)
    dictionary = dictionary.replace('\r\n','\n')

    p_reg = re.compile('^[^\r\n]+$', re.IGNORECASE + re.DOTALL + re.MULTILINE + re.UNICODE)
    m_reg = p_reg.findall(dictionary)

    word = wrd
    try:
        if m_reg and len(m_reg) > 0:
            index = ''
            words = []
            newword = ''
            for m in m_reg:
                if not m.startswith(' '):
                    index = m
                    del words[:]
                else:
                    replWord = m.strip()
                    words.append(replWord)
                    if word.find(' ') != -1:
                        newword = word.replace(replWord,index)

                if (word in words) or (word == index):
                    return index

            if newword != '' and newword != word:
                return newword
    except:
        common.log('Skipped Replacement: ' + word)

    return word


def select(params,src):
    paramArr = __parseParams(params)
    title = paramArr[0]
    params = paramArr[1]
    menuItems = params.split("|")
    return select(title, menuItems)


def convDate(params, src):
    language = common.language

    if params.find("','") != -1:
        paramArr = __parseParams(params)
        oldfrmt = paramArr[0]
        newfrmt = paramArr[1]
        offsetStr = ''
        if len(paramArr) > 2:
            offsetStr = paramArr[2]
        return dt.convDate(language, src, str(oldfrmt), str(newfrmt), offsetStr)
    else:
        params = params.strip("'")
        return dt.convDate(language, src,params)


def convTimestamp(params, src):
    if params.find("','") != -1:
        paramArr = __parseParams(params)
        newfrmt = paramArr[0]
        offsetStr = paramArr[1]
        return dt.convTimestamp(src, str(newfrmt), offsetStr)
    else:
        newfrmt = params.strip("'")
        return dt.convTimestamp(src, str(newfrmt))
    
def convDateUtil(params, src):
    if params.find("','") != -1:
        paramArr = __parseParams(params)
        newfrmt = paramArr[0]
        timezone = paramArr[1]
        return dt.convDateUtil(src, str(newfrmt), timezone)
    else:
        newfrmt = params.strip("'")
        return dt.convDateUtil(src, str(newfrmt))


def offset(params, src):
    paramArr = __parseParams(params)
    t = paramArr[0].replace('%s', src)
    o = paramArr[1].replace('%s', src)

    hours = int(t.split(':')[0])
    minutes = int(t.split(':')[1])
    ti = datetime.datetime(2000, 1, 1, hours, minutes)

    offset = dt.datetimeoffset(ti, o)

    return offset.strftime('%H:%M')


def getSource(params, src):
    paramPage = ''
    paramReferer = ''
    if params.find('\',\'') > -1:
        paramPage, paramReferer = __parseParams(params)
    else:
        paramPage = params.strip('\',\'')

    paramPage = paramPage.replace('%s', src)
    return common.getHTML(paramPage, None, paramReferer)


def parseText(item, params, src):
    paramArr = __parseParams(params)

    text = paramArr[0].replace('%s',src)
    if text.startswith('@') and text.endswith('@'):
        text = item.getInfo(text.strip('@'))

    regex = paramArr[1].replace('%s', src)
    if regex.startswith('@') and regex.endswith('@'):
        regex = item.getInfo(regex.strip('@'))

    variables = []
    if len(paramArr) > 2:
        variables = paramArr[2].split('|')
    return reg.parseText(text, regex, variables)


def getInfo(item, params, src, xml=False, mobile=False):
    paramArr = __parseParams(params)
    paramPage = paramArr[0].replace('%s', src)

    if paramPage.startswith('@') and paramPage.endswith('@'):
        paramPage = item.getInfo(paramPage.strip('@'))

    
    paramRegex = paramArr[1].replace('%s', src)
    if paramRegex.startswith('@') and paramRegex.endswith('@'):
        paramRegex = item.getInfo(paramRegex.strip('@'))
        
    referer = ''
    form_data = ''
    variables=[]
    if len(paramArr) > 2:
        referer = paramArr[2]
        referer = referer.replace('%s', src)
        if referer.startswith('@') and referer.endswith('@'):
            referer = item.getInfo(referer.strip('@'))
    if len(paramArr) > 3:
        variables = paramArr[3].strip("'").split('|')
        
    parsed_link = urlparse.urlsplit(referer)
    parsed_link = parsed_link._replace(netloc=parsed_link.netloc.encode('idna'),path=urllib.quote(parsed_link.path.encode('utf-8')))
    referer = parsed_link.geturl().encode('utf-8')
    
    try:
        parts = (paramPage.split('|', 1) + [None] * 2)[:2]
        paramPage, form_data = parts
        form_data = urlparse.parse_qsl(form_data)
    except: 
        pass

    common.log('Get Info from: "'+ paramPage + '" from "' + referer + '"')
    data = common.getHTML(paramPage, form_data, referer, xml, mobile, ignoreCache=False,demystify=True)
    return reg.parseText(data, paramRegex, variables)


def decodeBase64(src):
    from base64 import b64decode
    return b64decode(src)

def encodeBase64(src):
    from base64 import b64encode
    return b64encode(src)

def decodeRawUnicode(src):
    try:
        return src
    except:
        return src
    
def resolve(src):
    try:
        parsed_link = urlparse.urlsplit(src)
        tmp_host = parsed_link.netloc.split(':')
        if 'streamlive.to' in tmp_host[0]:
            servers = ['80.82.78.4',
                       '93.174.93.230',
                       '95.211.210.69',
                       '95.211.196.5',
                       '184.173.85.91',
                       '85.17.31.102',
                       '169.54.85.69']
                       #'62.210.139.136']
            import random
            tmp_host[0] = random.choice(servers)
        elif tmp_host[0] == 'xlive.sportstream365.com':
            servers = ["93.189.57.254",
                       "93.189.62.10",
                       "185.49.70.58",
                       "46.28.205.96",
                       "178.17.168.90",
                       "185.28.190.69",
                       "85.114.135.215",
                       "94.242.254.211"]
            import random
            tmp_host[0] = random.choice(servers)
        elif tmp_host[0] == 'live.pub.stream':
            servers = [ "195.154.169.244",
                        "195.154.185.109",
                        "195.154.179.159",
                        "195.154.167.95",
                        "62.210.203.163",
                        "195.154.168.230",
                        "62.210.203.170",
                        "62.210.203.167",
                        "195.154.173.124",
                        "195.154.172.90",
                        "195.154.179.167",
                        "195.154.177.110",
                        "195.154.179.174",
                        "195.154.168.218",
                        "195.154.185.113",
                        "195.154.187.46",
                        "195.154.168.233",
                        "195.154.187.23",
                        "195.154.168.222",
                        "195.154.169.233",
                        "195.154.169.234",
                        "195.154.182.101"]
            import random
            tmp_host[0] = random.choice(servers)
        else:
            tmp_host[0] = socket.gethostbyname(tmp_host[0])
        tmp_host = ':'.join(tmp_host)
        parsed_link = parsed_link._replace(netloc=tmp_host)
        return parsed_link.geturl()
    except:
        return src


def replace(params, src):
    paramArr = __parseParams(params)
    paramstr = paramArr[0].replace('%s', src)
    paramSrch = paramArr[1]
    paramRepl = paramArr[2]
    return paramstr.replace(paramSrch,paramRepl)


def replaceRegex(params, src):
    paramArr = __parseParams(params)
    paramStr = paramArr[0].replace('%s', src)
    paramSrch = paramArr[1]
    paramRepl = paramArr[2]

    r = re.compile(paramSrch, re.IGNORECASE + re.DOTALL + re.MULTILINE + re.UNICODE)
    ms = r.findall(paramStr)
    if ms:
        for m in ms:
            paramStr = paramStr.replace(m, paramRepl,1)
        return paramStr
    return src


def resolveVariable(item, param):
    if param.startswith('@') and param.endswith('@'):
        return item.getInfo(param.strip('@'))
    return param
    

def ifEmpty(item, params, src):
    paramArr = __parseParams(params)

    paramSource = resolveVariable(item, paramArr[0].replace('%s', src))
    paramTrue = resolveVariable(item, paramArr[1].replace('%s', src))
    paramFalse = resolveVariable(item, paramArr[2].replace('%s', src))

    if paramSource == '':
        return paramTrue
    else:
        return paramFalse


def isEqual(item, params, src):
    paramArr = __parseParams(params)
    paramSource = resolveVariable(item, paramArr[0].replace('%s', src))
    paramComp = resolveVariable(item, paramArr[1].replace('%s', src))
    paramTrue = resolveVariable(item, paramArr[2].replace('%s', src))
    paramFalse = resolveVariable(item, paramArr[3].replace('%s', src))

    if (paramSource == paramComp):
        return paramTrue
    else:
        return paramFalse


def ifFileExists(item, params, src):
    paramArr = __parseParams(params)
    paramSource = resolveVariable(item, paramArr[0].replace('%s', src))
    paramTrue = resolveVariable(item, paramArr[1].replace('%s', src))
    paramFalse = resolveVariable(item, paramArr[2].replace('%s', src))

    if fileExists(paramSource):
        return paramTrue
    else:
        return paramFalse    


def ifExists(item, params, src):
    paramArr = __parseParams(params)
    paramSource = resolveVariable(item, paramArr[0].replace('%s', src))
    paramTrue = resolveVariable(item, paramArr[1].replace('%s', src))
    paramFalse = resolveVariable(item, paramArr[2].replace('%s', src))
    
    return paramTrue



def urlMerge(params, src):
    paramArr = __parseParams(params)
    paramTrunk = paramArr[0].replace('%s', src).replace("\t","")
    paramFile= paramArr[1].replace('%s', src).replace("\t","")

    if not paramFile.startswith('http'):
        up = urlparse.urlparse(urllib.unquote(paramTrunk))
        if paramFile.startswith('/'):
            return urllib.basejoin(up[0] + '://' + up[1], paramFile)
        else:
            return urllib.basejoin(up[0] + '://' + up[1] + '/' + up[2],paramFile)
    return src

def decodeXppod(src):
    return xp.decode(src)

def decodeXppod_hls(src):
    return xp.decode_hls(src)

def getCookies(cookieName, url):
    domain = urlparse.urlsplit(url).netloc
    return common.getCookies(cookieName, domain)
    
    
