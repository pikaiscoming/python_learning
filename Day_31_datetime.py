# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:14:54 2021

@author: 皮皮卡卡
"""
'''可以知道關於日子的訊息'''
import datetime
print(datetime.datetime.now())

dt = datetime.datetime(2019, 10, 21,16, 29, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

my_birthday = datetime.datetime(1999, 10, 23, 0, 0, 0)
her_birthday = datetime.datetime(1999, 9, 25, 0, 0, 0)

if my_birthday > her_birthday:
    print('She is old. haha')
else:
    print('my sorry')

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)#no month and year to contrl.

print(delta.days, delta.seconds, delta.microseconds)

print()
