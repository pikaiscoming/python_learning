# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 20:01:02 2021

@author: 皮皮卡卡
"""
import time, datetime, threading

print('Start of program.')

def takeanap():
    time.sleep(5)
    print('wake up!!')
    
threadobj = threading.Thread(target=takeanap) #want to run takeanap this function
threadobj.start()

print('End of program')

'''
wake up 會最後出現，因為 threadobj的目標就是執行一個新的執行緒，有兩個在往下執行程式碼，而threadobj只會
執行，指定的函數。所以在主執行續跑到print後就結束了，但是副執行續會做完。
'''