# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:57:48 2021

@author: 皮皮卡卡
"""
import pprint

spam = {'apple':1, 'banana:':2, 'cat':3}
for v in spam.values():
    print(v)
for v in spam.keys():
    print(v)
for v,k in spam.items():
    print(v+str(k))
    
picnicitems = {'122':4, 'pikachu':2}
print(picnicitems.get(str(122), 0))

spam.setdefault('color', 'black') #if color not in spam, it will be added in it.

message = 'It was a bright cold day in April, \
           and the clocks were striking thirteen'
count={}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
print(count)    #calculate the number of every characters in message
#pprint.pprint(count)

word = {'fow':42}


