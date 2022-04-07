# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 22:23:19 2022

@author: 皮皮卡卡
"""

import matplotlib.pyplot  as plt
import numpy as np
def squ(x):
    return x**2

x1 = np.linspace(1,10, 10) #last one 
x2 = np.arange(1,11, 1)
print(x2)
fig = plt.figure()
ax1 = fig.add_subplot(221, facecolor='b')
ax1.plot(x1, squ(x1), c='r', linewidth=5)
ax2 = fig.add_subplot(212)

plt.subplots(ncols=2, nrows=2)



plt.show()