# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 15:13:57 2022

@author: 皮皮卡卡
"""
import cv2
import numpy as np

points = []
def findpan(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    
    lower = np.array([0, 146, 195])
    upper = np.array([87, 255, 255])
    
    mask = cv2.inRange(img_hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    
    px, py = findcontour(mask)
    cv2.circle(imgcontour, (px, py), 5, (0, 255,0), cv2.FILLED)
    cv2.imshow('result', result)
    if px !=0:
        points.append([px, py])
    
    
def findcontour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        cv2.drawContours(imgcontour, cnt, -1, (255,0,0), 4)
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri*0.02, True)
            x, y, w, h = cv2.boundingRect(vertices) #find contour topleft point and width, height
    return x+w//2, y+h//2

def drawpoint(point):
    for point in points:
        cv2.circle(imgcontour, (point[0],point[1]), 5, (0, 255,0), cv2.FILLED)
        

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while (cap.isOpened()):
    ret, frame = cap.read()
    
    if ret:
        imgcontour = frame.copy() 
        cv2.imshow('video', frame)
        findpan(frame)
        drawpoint(points)
        cv2.imshow('contour', imgcontour)
        
    if cv2.waitKey(10) & 0xFF == ord('q'):                
        break
    
cap.release()
cv2.destroyAllWindows()