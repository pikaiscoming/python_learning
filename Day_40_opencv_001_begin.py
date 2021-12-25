# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 12:32:22 2021

@author: pikachu
"""

import cv2

img = cv2.imread(r'D:\python_learning\test_picture.jpg')

img = cv2.resize(img, (300, 300)) #resize to arbitrary size
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) #scale enlarge or shrink

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
