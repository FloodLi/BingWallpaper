#!/usr/bin/env python2.7

import sys
import urllib
import urllib2
import json
import subprocess
import getpass
import time
import os

from AppKit import NSWorkspace, NSScreen
from Foundation import NSURL

__author__ = 'FloodLi'
__version__ = 0.1
__page__ = 'https://github.com/FloodLi/BingWallpaper'

def set_wallpaper(file):
    # make image options dictionary
    # we just make an empty one because the defaults are fine
    options = {}

    # get shared workspace
    ws = NSWorkspace.sharedWorkspace()
    
    file_url = NSURL.fileURLWithPath_(file)
    for screen in NSScreen.screens():
    # tell the workspace to set the desktop picture
        (result, error) = ws.setDesktopImageURL_forScreen_options_error_(file_url, screen, options, None)
    if error:
        print(error)
        print("setting Desktop wallpaper..............failed")
        exit(-1)


def main():
    print('')
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localtime + ':')
    
    today = time.strftime("%Y%m%d")
    local_file = 'bingwallpaper'+today+'.jpg'
    local_path = '/Users/' + getpass.getuser() + '/Pictures/'
    file = local_path+local_file
    if os.path.isfile(file):
        print('file has exist')
        exit()
    url_base = 'http://cn.bing.com/HPImageArchive.aspx?format=js&mbl=1&idx=0&n=1'
    codec = 'utf-8'

    print(local_path+local_file)
    
    webpage = urllib2.urlopen(url_base)
    js = webpage.read().decode(codec)
    download_url = 'http://cn.bing.com'+json.loads(js)['images'][0]['url']
    print(download_url)
    urllib.urlretrieve(download_url, file)
    set_wallpaper(file)


if __name__ == '__main__':
    main()

