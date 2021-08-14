# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:26:20 2021

@author: User
"""

'''
create a timed quiz. about multiplication 有點像九九乘法表
'''
import pyinputplus as pyip
import random, time

numsofquestions = 10 
correctAn = 0

for Q in range(1, numsofquestions+1):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '{}: {} x {} ='.format(Q,num1,num2)   
    
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1*num2)],  #to be sure this answer belong the begins and ends at same time.
                      blockRegexes=[('.*'), 'incorrect!'],   #in this case, what number user input will cancle and display incorrect
                      timeout=8, limit=3)
    
    except pyip.TimeoutException:
        print('Out of time')
        
    except pyip.RetryLimitException:
        print('Out of try')

    else:
        '''
        run this meaning the aanswer is correct!
        '''
        print('you are right')
        correctAn +=1
        
print(str(correctAn) +'/'+ str(numsofquestions))
