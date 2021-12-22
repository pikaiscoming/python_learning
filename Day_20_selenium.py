# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:16:15 2021

@author: 皮皮卡卡
"""
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome() 
type(browser)

browser.get('https://2048game.com/')
browser.maximize_window()
#linkElem = browser.find_element_by_link_text('Automate the Boring Stuff with Python')
#linkElem.click()
htmlElem = browser.find_element_by_tag_name('html')     #按鍵都傳給他
#htmlElem.send_keys(Keys.PAGE_DOWN)

for i in range(100):

    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.UP)
