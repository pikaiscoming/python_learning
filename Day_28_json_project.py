# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:20:55 2021

@author: 皮皮卡卡
"""

import json, requests, sys

APPID = '8518721b76237a43dda00d014f2eb389' 


if len(sys.argv)<2:
    print('Usage: getOpenWheather.py city_name, 2-letter_country_code')
    sys.exit()
    
location = ''.join(sys.argv[1:]) #第二個跟第三個地名之間不能有空隙

url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s'%(location, APPID)
response = requests.get(url) #save the data of json
response.raise_for_status()
#print(response.text)

#load json

weatherData = json.loads(response.text)
T = int(weatherData['main']['temp'])-273
H = weatherData['main']['humidity']
#pprint.pprint(weatherData)
print('Current weather in {}.'.format(location))
print('Temperature is {} degrees Celsius.'.format(T))
print('Humidity:%s%%'%H)
