# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:26:44 2021

@author: pikachu
"""

import cv2
import numpy as np
img = cv2.imread(r'D:/python_learning/test_picture.jpg')
img = cv2.resize(img, (0, 0), fx = 1, fy=1)
#img = np.empty((300, 1000, 3), np.uint8) 

for row in range(300):
    for column in range(img.shape[1]):
        img[row][column] = [255, 0 ,0]
        
img = img[:500, :400] #切割
        
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape[0])
print(img.shape[1])
