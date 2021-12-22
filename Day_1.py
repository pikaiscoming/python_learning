# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:47:14 2020

@author: 皮皮卡卡
"""


'''def spam(number):
    try:
        return 
    except ZeroDivisionError:
        print('please enter a integral')
 '''


def collatz():
    if (number%2):
        final = 3*number + 1
    else:
        final = number//2

    return final 
 
  

number =int(input())
        

while (1):
    number = int(number)
    if(collatz()!=1):
        print(collatz())
        number = collatz()
    else:
        print(1)
        break            

 
