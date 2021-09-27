# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:21:08 2021

@author: pikachu
"""

import shutil, os #對於檔案的複製移動等等

from pathlib import Path

p = Path.home()

#print(shutil.copy(p/'spam.txt', p/'some_folder')) #copy to folder
#print(shutil.copy(p/'spam.txt', p/'some_folder/eggs2.txt'))     #copy and rename
print(p)

shutil.copytree(p/'spam', p/'spam_backup')  #create a new folder with the same content but new name

shutil.move('file_name', 'path_youwanted') #if path is not exist, python will rename file_name.txt to a file named.

 
