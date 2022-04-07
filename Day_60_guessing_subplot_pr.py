# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 22:09:02 2022

@author: 皮皮卡卡
"""
import matplotlib.pyplot as plt
import random
import pprint
import pandas as pd

result = {}
temp_res = []
result2 = {}
temp_res2 = []

'''random guessing'''
for i in range(1000):
    low = 1
    high = 10000
    ans = random.randint(low, high)
    #print('answer is ' +str(ans))
    
    for j in range(1, 999):
        guess = random.randint(low, high)
        #print(guess)
        if ans == guess:
            temp_res.append(j)
            #print('You get it!')
            
            break
        
        else:
            
            if guess > ans:
                high = guess-1
            else:
                low = guess+1
    
        #print('range is ' + str(low) +' to ' + str(high))
                
for num in temp_res:
    result.setdefault(num, 0)
    result[num] +=1
    
'''first guessing 50'''

for i in range(1000):
    low = 1
    high = 10000
    ans = random.randint(low, high)
    #print('answer is ' +str(ans))
    
    for j in range(1, 99):
        if j == 1:    
            guess = 5000
        elif j==2 and guess>ans:
            guess = 2500
        
        elif j==2 and guess<ans:
            guess = 7500
        
        else:
            guess = random.randint(low, high)
        #print(guess)
        if ans == guess:
            temp_res2.append(j)
            #print('You get it!')
            
            break
        
        else:
            
            if guess > ans:
                high = guess-1
            else:
                low = guess+1
    
        #print('range is ' + str(low) +' to ' + str(high))
                
for num in temp_res2:
    result2.setdefault(num, 0)
    result2[num] +=1

'''data_frame'''
#df = pd.DataFrame([result])
df = pd.DataFrame(list(result.items()), columns= ['guess_times', 'value'])
df.sort_values(by=['guess_times'], inplace=True)
df2 = pd.DataFrame(list(result2.items()), columns= ['guess_times', 'value'])
df2.sort_values(by=['guess_times'], inplace=True)

'''plot'''

fig = plt.figure(figsize=(10,8),dpi=80, facecolor='w', edgecolor='w')
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, sharey = ax1)

ax1.bar(df.guess_times, df.value)
ax2.bar(df2.guess_times, df2.value)
ax1.set_title('Guessing number', fontsize = 15)
ax2.set_title('Guessing number from 50', fontsize = 15)
ax1.set_xlabel("Guess times", fontsize = 12)
ax1.set_ylabel("value", fontsize = 12)
ax2.set_xlabel("Guess times", fontsize = 12)
plt.tight_layout()
plt.show()

