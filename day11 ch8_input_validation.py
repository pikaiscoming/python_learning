# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:13:36 2021

@author: User
"""

'''
input limition
'''
import pyinputplus as pyip

response = pyip.inputNum() #可以規定回什麼樣格式的答案，還可以接受string的數字
print(response)

response2 = pyip.inputName('enter num:', min=4) #at least bigger than 4 or equal


while True:
    print('input your age')
    age = input()
    
    try:
        age = int(age)
    
    except ValueError:
        print('please inter numeric digits.')
        continue  #跳過本次迴圈
    if age < 1:
        print('please enter a postive number.')
        continue
   
    break

print('your age is {}'.format(age))

'''
RetryLimitException可以不符合幾次 and timeoutException可以規定多少時間內輸入
'''
response3 = pyip.inputNum(limit=2, default='we got wrong too many times')   #default
response4 = pyip.inputNum(timeout=10) #second

'''
can use in regex
'''
response5 = pyip.inputNum(allowRegexs=['(I|V|X|L|C|D|M)+', 'zero'])

response6 = pyip.inputNum(blockRegexes=['[02468]$'])    #不能是偶數結尾

