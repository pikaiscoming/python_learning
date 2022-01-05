# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:48:44 2022

@author: 皮皮卡卡
"""
import cv2


img = cv2.imread('tyuzu.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('face_detect.XML')
face_rect = face_cascade.detectMultiScale(gray, 1.1, 3) #放大倍數, 找到臉幾次才算是找到

for (x, y, w, h) in face_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

