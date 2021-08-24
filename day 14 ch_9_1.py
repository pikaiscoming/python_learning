# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:54:27 2021

@author: User
"""

import os 
from pathlib import Path



print(Path.cwd())   #os.getcwd() old function

try:
    
    os.makedirs(r'C:\Users\User\\Desktop\python_learning\pipikaka')  #create a file named pipikaka 
except FileExistsError:
    
    print('file is existed')
#Path(r'C:\Users\User\Desktop\python_learning').mkdir() #just like above

'''
check whether a given path is an absolute path.
'''

test_path = Path.cwd()

print(test_path.is_absolute()) #ture like os.path.isabs(path)

print(Path('spam\bacon\egg').is_absolute())

print(os.path.abspath('.')) #can get the absolute path

print(os.path.relpath(r'C:\Users\User\Desktop\python_learning', r'C:\Users\User\Desktop\web crawler'))  #相對路徑要先'..'回到上一頁才能找到
#所以是跟前面的路徑的相對路徑

'''
we can part the path into three parts. 
'''

print(Path.cwd())
print(Path.cwd().parents[0]) #可以得到每一層的path 由長到短 從0到大

'''
os also have the similar function.
'''
 
filepath = r'C:\Users\user\Desktop\web crawler'
print(os.path.basename(filepath), os.path.dirname(filepath)) #basename 最近的'\'之後(就是檔案) dirname是之前
print(filepath.split(os.sep)) #用list來存



