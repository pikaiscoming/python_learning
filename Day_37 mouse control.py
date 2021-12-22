# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:18:00 2021

@author: 皮皮卡卡
"""
import pyautogui as gui
import time

print(gui.position())

#gui.moveTo(482, 1060, duration=0.5)

gui.click(482,1060, duration=1) #chrome 可以 doubleClick or rightClick middleClick

#time.sleep(1)

gui.click(1299, 541)

gui.moveTo(179, 86, duration=0.5)
gui.dragTo(1054, 65, duration=0.5)
gui.rightClick()

gui.mouseInfo()
