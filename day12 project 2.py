# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 14:32:22 2021

@author: User
"""

import pyinputplus as pyip
import re

def yesorno(answer):
    

    
        if answer == 'yes' or answer =='no':
        
            if answer == 'no':
                print('Thank you. Have a nice day')

    
            if answer == 'yes':
                return None
            else:
                print(str(answer)+' is not a valid yes/no response')
    
        return None

while True:        
    print('want to know how to keep an idiot busy for hours?')
    response = pyip.inputCustom(yesorno)
    
        
    
    
            