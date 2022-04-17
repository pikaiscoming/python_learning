# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:59:01 2022

@author: 皮皮卡卡
"""

import requests
from bs4 import BeautifulSoup as BS
import selenium

#response = requests.get("http://en.wikipedia.org/wiki/Nobel_Prize")
#print(response.headers) 

'''get json'''

# response1 = requests.get('https://data.ct.gov/resource/y6p2-px98.json?'\
#                          'category=Fruit&item=Peaches')
# data = response1.json()

# print(data[0].keys())

'''country data'''

url_country = "https://restcountries.com/v2" #現在都改用這個
'''check here https://restcountries.com/'''

def REST_country_req(field='all', name=None, params=None):
    headers = {'User-Agent':'Mozilla/5.0'}
    
    if not params:
        params = {}
        
    if field == 'all':
        return requests.get(url_country + '/all')
    
    url = '%s/%s/%s'%(url_country, field, name)
    print('requesting URL: '+ url)
    
    response = requests.get(url, params=params, headers=headers)
    
    if not response.status_code == 200:
        raise Exception('Request failed')
        
    return response

response = REST_country_req('currency', 'usd')
print(response.json())
        
    