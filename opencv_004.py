# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:22:18 2021

@author: 皮皮卡卡
"""
import cv2
import numpy as np

kernal = np.ones((3, 3), np.uint8)
kernal1 = np.ones((3, 3), np.uint8)

img = cv2.imread('test_picture.jpg')
img = cv2.resize(img, (0, 0), fx = 0.5, fy =0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (17, 17), 0) #third parameter is std error 第二個正方要奇數
'''是以高斯分布來處理(17, 17)內的像素，然後標準差又可以決定是怎麼分布的'''
canny = cv2.Canny(img, 100, 250) #thread deicide 邊界
dilate = cv2.dilate(canny, kernal, iterations=1) #變粗
erode = cv2.erode(dilate, kernal1, iterations=2) #變細




cv2.imshow('frame1', img)
cv2.imshow('frame2', gray)
cv2.imshow('frame3', canny)
cv2.imshow('frame4', dilate)
cv2.imshow('frame5', erode)

cv2.waitKey(0)

cv2.destroyAllWindows()
