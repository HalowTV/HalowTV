# Special thanks to whufclee for the original Community Builds code used in this add-on

import xbmcgui
from urllib2 import Request, urlopen
import os, os.path, sys, urllib, time

def download(url, dest, dp = None):
	if not dp:
		dp = xbmcgui.DialogProgress()
		dp.create("","Downloading & Copying File",' ', ' ')
		dp.update(0)
    
	start_time=time.time()
	
	try:
		urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
	except:
		#delete partially downloaded file
		while os.path.exists(dest):
			try:
				os.remove(dest)
				break
			except:
				pass

	
	
	
 

 
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try:
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024)
            kbps_speed = numblocks * blocksize / (time.time() - start_time)
            if kbps_speed > 0:
                eta = (filesize - numblocks * blocksize) / kbps_speed
            else:
                eta = 0
            kbps_speed = kbps_speed / 1024
            total = float(filesize) / (1024 * 1024)
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total)
            e = 'Speed: %.02d Kb/s ' % kbps_speed
            e += 'ETA: %02d:%02d' % divmod(eta, 60)
            dp.update(percent, mbs, e)
            #print percent, mbs, e
        except:
            percent = 100
            dp.update(percent)
        if dp.iscanceled():
            dp.close()
            raise StopDownloading('Stopped Downloading') 
