# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:08:47 2021

@author: 皮皮卡卡
"""

stringOfjsondata = '{"name": "zophie", "isCat": true, "micecaught": 0, "felineIQ": null}'

import json
jsondata = json.loads(stringOfjsondata) #load string
print(jsondata)

pythonvalue = {'sicat':True, 'miceCaught':0, 'name': 'zophie', 'felineIQ':None}

stringofdata = json.dumps(pythonvalue)
print(stringofdata)

'''
loads: we change the value of JSON to python
dumps: we change the value of python to JSON
'''