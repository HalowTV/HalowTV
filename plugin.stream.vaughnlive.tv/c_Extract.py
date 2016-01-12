### ############################################################################################################
###	#	
### # Author: 			#		The Highway
### # Description: 	#		Unzipper File For:  The Binary Highway
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath,_OpenFile)
import zipfile
def all(_i,_o,dp=None):
	if dp: return allWithProgress(_i,_o,dp)
	return allNoProgress(_i,_o)
def allNoProgress(_i,_o):
	try:
		try: debob([_i,_o]); #debob(z.infolist()); 
		except: pass
		z=zipfile.ZipFile(_i, 'r')
		z.extractall(_o)
	except: return False
	return True
def allWithProgress(_i,_o,dp):
	z=zipfile.ZipFile(_i,  'r'); nFiles=float(len(z.infolist())); count=0
	try:
		try: debob([_i,_o]); debob(z.infolist()); 
		except: pass
		for item in z.infolist():
			count+=1; update=count / nFiles * 100
			dp.update(int(update))
			try: debob(item)
			except: pass
			zin.extract(item,_o)
	except: return False
	return True

