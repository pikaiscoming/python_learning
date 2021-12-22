# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:13:38 2021

@author: 皮皮卡卡
"""
import pyautogui as gui

#s = gui.locateOnScreen('chrome.png')

#print(s) #Box(left=463, top=1041, width=42, height=39)

#s.left equals s[0] 

try:
    b = gui.locateOnScreen('chrome.png')
    print(b)
except:
    print('Could not be found.') #如果找不到很容易當掉所以用這個，像素還要完全一樣
    
'''找使用中的screen'''
'''
fw = pyautogui.getActiveWindow()

print(fw)
'''

gui.click(485, 1058, duration=1)
gui.click(480, 67, duration=0.5)
gui.write('pikachU')  #查pyautogui.KEYBOARD_KEYS
gui.typewrite('\n')

'''
can use keyDown('ctrl') and keyUp('c') 來控制快捷鍵，這邊用control舉例
'''
