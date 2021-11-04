# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:17:18 2021

@author: 皮皮卡卡
"""
import time 
starttime = time.time()
print(time.time())
print(time.ctime())

time.sleep(1)

endtime = time.time()
print(round((endtime-starttime),5))