# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:58:35 2022

@author: pikachu
"""

import numpy as np

a = np.arange(12).reshape(3,4)
b = np.linspace(0, 9, 10)
print(b)
print(a)
print(a[:,1]) #row first and column second (row,colume)
print(a[a[:,1]>2,])