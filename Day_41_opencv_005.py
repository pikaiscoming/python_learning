# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:26:01 2021

@author: 皮皮卡卡
"""
import cv2
import numpy as np

black = np.zeros((300, 450, 3), np.uint8) #(y, x)
print(black.shape)
cv2.line(black, (0, 0), (black.shape[1], black.shape[0]), (255, 255, 0), 1) #(x, y)
cv2.rectangle(black, (0, 0), (100, 100), (255, 255, 255), 2) #cv2.FILLED
cv2.circle(black, (200, 200), 50, (22, 50, 100), cv2.FILLED)
cv2.putText(black, 'hello', (200, 300), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0 ,0), 3) #字的大小, 顏色, 粗細


cv2.imshow('frame', black)
cv2.waitKey(0)

cv2.destroyAllWindows()
