# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:12:51 2021

@author: 皮皮卡卡
"""
import subprocess,time
calcpopen = subprocess.Popen(r'C:\Windows\System32\mspaint.exe') #open calculator
#time.sleep(5) #等個5 sec can get 0.
print(calcpopen.poll())
# if return 0 代表現在已經沒處理東西，相反return None
#time.sleep(3)
print(calcpopen.wait()) #直到我關閉mspaint才會繼續往下
print(calcpopen.poll()) #再次確認code是否結束

subprocess.Popen(['start', 'hello.txt'], shell = True) #start, open, see都可以
