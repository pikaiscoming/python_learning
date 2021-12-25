# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 13:19:52 2021

@author: pikachu
"""

import cv2 

cap = cv2.VideoCapture(r'D:\python_learning\lich_king.mp4') #這邊可以直接接上鏡頭

while 1:
    ret, frame = cap.read()
    
    
    if ret:
        cv2.imshow('frame', frame)
        
    else:
        break
    
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
    
    
