# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 09:49:56 2021

@author: User
"""

'''
your own custom validation by inputCustom()
'''
import pyinputplus as pyip

def addsuptoten(nums):
    numberlist = list(nums)
    for i,digit in enumerate(numberlist):
        numberlist[i] = int(digit)  #dictionary
    if sum(numberlist) !=10:
        raise Exception('the digits must add up to 10, not {}'.format(sum(numberlist))) #直接終止迴圈，可以參考這個網址https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
        
    return int(nums)

response = pyip.inputCustom(addsuptoten)



