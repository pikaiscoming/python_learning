# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 23:49:40 2021

@author: 皮皮卡卡
"""
import traceback

def spam():
    bacon()
    
def bacon():
    raise Exception('This is the error message.')
    




def a():
    try:
        raise Exception('This is the error message.')
    except:
        errorfile = open('errorinfo.txt', 'w')
        print(traceback.format_exc(), file=errorfile)
        #errorfile.write(traceback.format_exc())
        errorfile.close()
        print('It\'s done')
        
a()

'''we just record the error information to the txt file.'''