# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:34:12 2021

@author: 皮皮卡卡
"""
import cv2
import numpy as np

def empty(v):
    pass


img = cv2.imread('testt.jpg')
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # hsv 比較好過綠顏色

cv2.namedWindow('trackbar')
cv2.resizeWindow('trackbar', 640, 320)
cv2.createTrackbar('hue min', 'trackbar', 0, 179, empty) #色調
cv2.createTrackbar('hue max', 'trackbar', 179, 179, empty)
cv2.createTrackbar('sat min', 'trackbar', 0, 255, empty) #飽和度
cv2.createTrackbar('sat max', 'trackbar', 255, 255, empty)
cv2.createTrackbar('val min', 'trackbar', 0, 255, empty) #亮度
cv2.createTrackbar('val max', 'trackbar', 255, 255, empty)

while 1:
    h_min = cv2.getTrackbarPos('hue min', 'trackbar')
    h_max = cv2.getTrackbarPos('hue max', 'trackbar')
    s_min = cv2.getTrackbarPos('sat min', 'trackbar')
    s_max = cv2.getTrackbarPos('sat max', 'trackbar')
    v_min = cv2.getTrackbarPos('val min', 'trackbar')
    v_max = cv2.getTrackbarPos('val max', 'trackbar')
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    
    mask = cv2.inRange(img_hsv, lower, upper)

    cv2.imshow('frame', img)
    cv2.imshow('frame2', img_hsv)
    cv2.imshow('frame3', mask)
    
    if cv2.waitKey(1)==ord('q'):
        result = cv2.bitwise_and(img, img, mask=mask) #mask可以把黑色的部分蓋起來
        break

cv2.imshow('frame5',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
