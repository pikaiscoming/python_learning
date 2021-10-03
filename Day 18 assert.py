# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 19:31:26 2021

@author: pikachu
"""

'''assert''' #自己認定錯誤的產生
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
print(ages)
#assert ages[0]<=ages[-1]

market_2nd = {'ns':'green', 'ew':'red'}
mission_16th = {'ns':'green', 'ew':'red'}

def switchlight(stoplight):
    for key in stoplight.keys():
        
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
        
    #assert 'red' in stoplight.values(), 'Neither light is red!' +str(stoplight)
    return print(str(stoplight))
switchlight(market_2nd)

'''logging'''
import logging
logging.basicConfig((level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s'))
 