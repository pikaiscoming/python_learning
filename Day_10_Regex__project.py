# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:58:57 2021

@author: User
"""

import re 
import pyperclip as pyp

phoneRegex = re.compile(
    '0[1-9]-\d{8}')

emailRegex = re.compile('([A-Za-z\d\._+]+@(gmail|yahoo)\.(com|edu|org|net))')

text = str(pyp.paste())

match = []
for groups in phoneRegex.findall(text):
    match.append(groups)

for groups in emailRegex.findall(text):
    match.append(text)
    
if len(match) >0:
    pyp.copy('\n'.join(match))
    print('Copied to clipboard')
    print('\n'.join(match))
else:
    print('There is no phone number or email addresses found')
