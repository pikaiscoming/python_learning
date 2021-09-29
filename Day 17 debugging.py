# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:26:47 2021

@author: 皮皮卡卡
"""

'''raise Exception 算是一種合併用法'''

def boxprint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <=2:
        raise Exception('Width must be greater than 2.')
    if height <=2:
        raise Exception('Height must be greater than 2')
    
    print(symbol*width)
    for i in range(height-2):
        print(symbol + (' ' *(width-2)) + symbol)
    print(symbol*width)
    
for sym, w, h, in (('*', 4, 4), ('d', 12, 5), ('x', 1, 3), ('zzz', 3, 4)):
    try:
        boxprint(sym, w, h)
    except Exception as err:    #if exception happened then sentence will be saved in err
        print('An exception happened:' + str(err))