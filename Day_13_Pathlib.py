# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:23:52 2021

@author: User
"""

from pathlib import Path
#why we need to learn this module? because every different systerm use different \ or / to describe path

way = str(Path('spam', 'bacon', 'eggs'))

print(way)


myfile = ['exp_1.csv', 'exp_2.txt', 'exp_3.docx']   #以後輸入很多檔案比較好用
for filename in myfile:
    print(Path(r'C:Users\Al', filename))
    
homefile = r'C:\User\Al'
subfolder = 'test.txt'

allpath = homefile + '\\' + subfolder
allpath = '\\'.join([homefile, subfolder]) #this method only can be use on Window

homefile1 = Path(r'C:/Users/Al')
subfolder1 = Path(r'spam')

print(str(homefile1/subfolder1))    #only Path object can use '/' to join together





