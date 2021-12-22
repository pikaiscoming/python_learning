# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:15:55 2021

@author: 皮皮卡卡
"""
table = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Bob', 'Carol','David'],
         ['dogs', 'cat', 'moose', 'goose']]

for i in table[0]:
    print(i.ljust(10, '/'))

def printtable(name):
    for x in name:
        lengh = 0
        for y in range(len(x)):
            if lengh <= len(x[y]):
                lengh = len(x[y])
        for s in x:
            print(s.rjust(lengh, ' '))
            
printtable(table)     

def platformprint(name):
        num = len(name[0])
        final = 0
        for y in range(num):
            lengh=0
            for x in range(len(name)):
                
                lengh += len(name[x][y])

            if final < lengh:
                final = lengh
        return final


    
    
    
    
    
    
    
    
final = platformprint(table)
