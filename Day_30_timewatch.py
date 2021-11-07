# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 11:11:38 2021

@author: 皮皮卡卡
"""
import time 

print('please press Enter to begin. Afterward, press Enter to click the stopwatch. Press Ctrl-c to quit')

input()
print('Started', end='')
starttime = time.time()
lasttime = starttime
lap = 1

try:
    while True:
        
        input()
        laptime = round(time.time() - lasttime, 2)
        totaltime = round(time.time() - starttime, 2)
        print('Lap #%s: %s (%s)' %(lap, totaltime, laptime), end=' ')
        lap += 1
        lasttime = time.time() #laptime is start from this time
except KeyboardInterrupt:
    print('Done!')
        
    
    