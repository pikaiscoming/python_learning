# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:52:57 2022

@author: 皮皮卡卡
"""

import os
import subprocess
import re

f = open(r'D:\Users\pipikaka\Desktop\python\learning_coding\command_1.txt', mode='r')
output = subprocess.getoutput(str(f.read()))
#os.system(str(f.read()))

power_reg = re.compile('(Power: )(.*?) (W)')
time_reg = re.compile('(Current time: )(.*? \d\d:\d\d:\d\d)')
power_data = power_reg.search(output) 
time_data = time_reg.search(output)

print('Power: {} W\nTime: {}'.format(power_data.group(2), time_data.group(2)))


