# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 12:39:48 2022

@author: 皮皮卡卡
"""
import cv2 
import numpy as np

def empty(v):
    pass

cap = cv2.VideoCapture(0) #1 is your camera


cv2.namedWindow('trackbar')
cv2.resizeWindow('trackbar', 640, 320)
cv2.createTrackbar('hue min', 'trackbar', 0, 179, empty) #色調
cv2.createTrackbar('hue max', 'trackbar', 179, 179, empty)
cv2.createTrackbar('sat min', 'trackbar', 0, 255, empty) #飽和度
cv2.createTrackbar('sat max', 'trackbar', 255, 255, empty)
cv2.createTrackbar('val min', 'trackbar', 0, 255, empty) #亮度
cv2.createTrackbar('val max', 'trackbar', 255, 255, empty)
while (cap.isOpened()):
    h_min = cv2.getTrackbarPos('hue min', 'trackbar')
    h_max = cv2.getTrackbarPos('hue max', 'trackbar')
    s_min = cv2.getTrackbarPos('sat min', 'trackbar')
    s_max = cv2.getTrackbarPos('sat max', 'trackbar')
    v_min = cv2.getTrackbarPos('val min', 'trackbar')
    v_max = cv2.getTrackbarPos('val max', 'trackbar')
    
    ret, img = cap.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    
    mask = cv2.inRange(img_hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    
# hsv 比較好過綠顏色
    
    
    
    if ret:
        cv2.imshow('frame1', result)
        cv2.imshow('frame', img)
        cv2.imshow('frame3', mask)
        width = cap.get(3)
        height = cap.get(4)
        fps = cap.get(5)
        frames_number = cap.get(7)
        
    if cv2.waitKey(10) & 0xFF == ord('q'):                
        break
    
    

print(h_min +','+ s_min+','+v_min+','+h_max+','+ s_max +','+ v_max)
cap.release()
cv2.destroyAllWindows()
        
