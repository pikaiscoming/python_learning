# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:22:13 2021

@author: 皮皮卡卡
"""
import requests, os, threading
from bs4 import BeautifulSoup as BS
os.makedirs('xkcd', exist_ok=True)



def downloadxkcd(startcomic, endcomic):
    url = r'http://xkcd.com/'
    for num in range(startcomic, endcomic):
        print('Downloading page http://xkcd/%s...' %(num))
        
        req = requests.get(url+str(num))
        
        bs = BS(req.text)
        
        #find the url of comic page
        
        comicelem = bs.select('#comic img') #tag:div id:comic tag:img attrs:src
        
        if comicelem ==[]:
            print('Could not get image.')
            
        else:
            comicurl = comicelem[0].get('src')
            print('Would download image %s' (comicurl))
            
            res = requests.get(comicurl)
            imagefile = open(os.path.join('xkcd', os.path.basename(comicurl)))
            for chunk in res.iter_content(100000): #downlaod size
                imagefile.write(chunk)
            imagefile.close()
downloadthreads = []           
for i in range(0, 140, 10):
    start = i
    end = i+9
    if start==0:
        start = 1
    
    downloadthread = threading.Thread(target=downloadxkcd, args=(start, end)) #first 1-9 two 10-19
    #three 20-29....一個執行續跑10個圖
    downloadthreads.append(downloadthread)
    downloadthread.start()
    
    
#wait for all threads to end.

for downladthread in downloadthreads:
    downloadthread.join()
print('Done.')