# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:37:16 2022

@author: 皮皮卡卡
"""

import numpy as np
import matplotlib.pyplot as plt

import json


with open('fraud_step.json', 'r') as f:
    steps = json.load(f)
    
every_hour_fraud = np.zeros(24)
for i in range(1, len(steps)+1):
    a = i%24
    if a == 0:
        every_hour_fraud[-1] += steps[str(i)]
    else:
        every_hour_fraud[a-1] += steps[str(i)]
        


fig = plt.figure(figsize=(10,6),dpi=80, facecolor='w', edgecolor='w')
ax = fig
x = np.arange(1, 25)
plt.bar(x,every_hour_fraud, width=0.65, color='firebrick', alpha = 1)

plt.title('Fraudulent Transactions in 24 Hours', fontsize=15, y=1.03)
plt.xlabel("24 hours ",fontsize=13)
plt.xticks(np.arange(1, 33, 2))
plt.ylabel("Number of fraudulent transactions",fontsize=13)
#plt.yaxis.set_label_coords(-.1, .1)
plt.axhline(y=342.2, linewidth = 2, c='royalblue')
plt.axis([0.5, 24.5, 0, 500])
t = ax.text(
    1.02, 0.66 , "342.2", ha="center", va="center", rotation=0, size=14, c='royalblue',
    bbox=dict(boxstyle="square,pad=0.3", fc="w", ec="royalblue", lw=1))
#plt.annotate("342.2", xy=(23.2,370), xytext=(23.2,370), fontsize=16, c='royalblue')
plt.tight_layout()
plt.show()