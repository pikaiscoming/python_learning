# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:24:09 2021

@author: 皮皮卡卡
"""
import datetime
import time

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
after=dt-thousandDays
print(after) #天數可以加減

'''直到某個時間在執行'''
birthday2022 = datetime.datetime(2020, 10, 23, 0, 0, 0)
while datetime.datetime.now() < birthday2022:
    time.sleep(1)
    
#%Y ex: 2014 1999 2020
#%y ex: 1-99
#%m 01-12
#%B 完整月份名字
#%b 月份縮寫
#%d 01-31
# can search from strftime 指令

oct10 = datetime.datetime(2019, 10, 10, 0, 0 ,0)  
print(oct10.strftime('%Y/%m/%d'))

'''convert string to datetime object'''

print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))