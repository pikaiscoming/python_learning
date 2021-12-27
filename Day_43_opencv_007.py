# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:04:33 2021

@author: pikachu
"""

import cv2

img = cv2.imread('D:\python_learning\contour.jpg')
imgcon = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 155, 255)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)



'''把形狀都框起來，排除雜訊'''
for cnt in contours:
    cv2.drawContours(imgcon, cnt, -1, (255,255,0), 3) #-1全部畫出來
    area = cv2.contourArea(cnt)
    if area > 500:
        peri = cv2.arcLength(cnt,True)
        vertices = cv2.approxPolyDP(cnt, peri*0.02, True) #找頂點
        corner = len(vertices)
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(imgcon,  (x,y), (x+w, y+h), (255, 0, 0), 2)
        if corner ==3:
            cv2.putText(imgcon, 'triangle', (x, y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (160, 20, 230), 3)
        elif corner == 4:
            cv2.putText(imgcon, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (160, 20, 230), 3)
        
    #print(cv2.arcLength(cnt, True))


cv2.imshow('frame', img)
cv2.imshow('canny', canny)
cv2.imshow('contour', imgcon)
cv2.waitKey(0)
cv2.destroyAllWindows()
