# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 00:47:59 2021

@author: 皮皮卡卡
"""
import pyautogui as gui

print(gui.size())

for i in range(3):
    gui.moveTo(100, 100, duration=0.25) #moveTo is 瞬間
    gui.moveTo(200, 100, duration=0.25)
    gui.moveTo(200, 200, duration=0.25)
    gui.moveTo(1, 1, duration=0.25)

for i in range(2):
    gui.move(1910, 0, duration=1) #往右多少 下多少
    gui.move(0, 1070, duration=1)
    gui.move(-1910, 0, duration=1)
    gui.move(0, -1070, duration=1)
    
'''
Cannot touch four corner
'''