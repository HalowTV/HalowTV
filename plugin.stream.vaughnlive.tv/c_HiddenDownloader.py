### ############################################################################################################
###	#	
### # Author: 			#		The Highway
### # Description: 	#		Downloader File For:  The Binary Highway
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
#from common import *
#from common import (_addon,_artIcon,_artFanart,_addonPath,_OpenFile)
import os,xbmc
def isPath(path): return os.path.exists(path)
def isFile(filename): return os.path.isfile(filename)
def download(url,destfile,destpath,useResolver=True):
	import urllib
	dp=''; link=url
	if isPath(destpath)==False: os.mkdir(destpath)
	myNote('Starting Download',destfile,100)
	urllib.urlretrieve(link,xbmc.translatePath(os.path.join(destpath,destfile)),lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
	myNote('Download Complete',destfile,15000)
def _pbhook(numblocks,blocksize,filesize,url,dp):
	try:
		percent=min((numblocks*blocksize*100)/filesize,100)
	except:
		percent=100
def downloadSilent(url,destfile,destpath,useResolver=True):
	import urllib
	dp=''; link=url
	if isPath(destpath)==False: os.mkdir(destpath)
	urllib.urlretrieve(link,xbmc.translatePath(os.path.join(destpath,destfile)),lambda nb,bs,fs,url=url:_pbhook(nb,bs,fs,url,dp))
