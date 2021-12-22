# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:10:05 2020

@author: 皮皮卡卡
"""

spam = ['Alice', 'ants', 'Bod', 'badgers', 'Carol', 'cats']
spamd = sorted(spam, key = str.lower, reverse = True)
print(spamd)
