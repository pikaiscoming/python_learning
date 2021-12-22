# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 23:27:35 2021

@author: 皮皮卡卡
"""
def printpicnic(itemdict, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth + rightwidth, '-'))
    for k,v in itemdict.items():
        print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidth))
    
picnicitems = {'apple':3, 'gold':12, 'phone':1, 'cola':10}

printpicnic(picnicitems, 12, 5)
