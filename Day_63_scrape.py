# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 12:19:53 2022

@author: 皮皮卡卡
"""
import requests
from bs4 import BeautifulSoup as BS

Headers = {'User-Agent': 'Mozilla/5.0'}
base_url = "http://en.wikipedia.org"

def get_nobel_soup():
    response = requests.get(base_url + '/wiki/List_of_Nobel_laureates', headers = Headers)
    
    return BS(response.text, 'html.parser')

bs = get_nobel_soup()
bs = bs.find('table', {'class':'wikitable sortable'})
print(bs)