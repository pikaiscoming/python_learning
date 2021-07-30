# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 23:17:13 2021

@author: 皮皮卡卡
"""
message = 'call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
def isPhonenumber(text):
    if(len(text))!=12:
        
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False 
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

for i in range(len(message)):
    word = message[i:i+12]
    if isPhonenumber(word):
        print(word)
        
print('Done')