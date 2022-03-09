# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:32:37 2022

@author: 皮皮卡卡
"""

import math
import numpy as np


'''points'''

x = [3, 2, 1, 0, -1, -2, -3]
pd_x = [0.45,0.55]
y = [9, 4, 1, 0, 1, 4, 9]
pd_y = []

'''dist'''

countx = {}

for num in x:
    countx.setdefault(num, 0)
    countx[num] = countx[num] + 1

county = {}

for num in y:
    county.setdefault(num, 0)
    county[num] = county[num] + 1
    
'''cal'''

class calculation:
    
    def __init__(self, list_x, list_y):
        self.x = list_x
        self.y = list_y

    '''enclidean'''

    def dis(self):
        return math.dist(self.x,self.y)

    def dis_x(self):
        squ = 0
        for i in range(len(self.x)):
            err = x[i] - y[i]
            squ += err**2
        return squ,math.sqrt(squ)


    '''correlation'''

    def corr(self):
        return (np.corrcoef(self.x,self.y)[0][1])

    def std(self):
        return np.std(self.x, ddof=1), np.std(self.y, ddof=1)

    def std_x(self):  
        squ = 0
        m = np.mean(self.x)
        for i in range(len(self.x)):
            err = self.x[i] - m
            squ += err**2
        ans = math.sqrt(squ/(len(self.x)-1))
        return squ, ans
    
    def std_y(self):  
        squ = 0
        m = np.mean(self.y)
        for i in range(len(self.y)):
            err = self.y[i] - m
            squ += err**2
        ans = math.sqrt(squ/(len(self.y)-1))
        return squ, ans

    '''cosine'''

    def cos(self):
        inner_product = np.inner(self.x, self.y)
        zero = np.zeros(len(self.x))
        length_x = math.dist(self.x, zero)
        length_y = math.dist(self.y, zero)
        return inner_product/(length_x*length_y)

    '''mutual information'''

    def Hx(self, pd_x=np.ones(len(x))):
        if len(pd_x) != len(self.x):
            Exception('length of list_pdf does not match list_y.')
        hx = 0
        if pd_x[0] == 1:

            for v in countx.values():
                p = v/len(x)
                hx += p*math.log(p, 2)
            return -hx
        else:
            for i in range(len(self.x)):
                hx += pd_x[i]*math.log(pd_x[i],2)
            return -hx
            
    def Hy(self, pd_y=np.ones(len(y))):
        if len(pd_x) != len(self.y):
            Exception('length of list_pdf does not match list_y.')         
        hy = 0
        if pd_y[0] == 1:
            for v in county.values():
                p = v/len(y)
                hy += p*math.log(p, 2)
            return -hy
        else:
            for i in range(len(self.y)):
                hy += pd_y[i]*math.log(pd_y[i],2)
            return -hy

    def Hxy_1to1(self, pd_x=np.ones(len(x))/len(x), pd_y=np.ones(len(y))/len(y)):      
        hxy = 0
        for i in range(len(self.x)):
            p = pd_x[i]
            hxy += p*math.log(p, 2)
        return -hxy


                
test = calculation(x, y)
print(test.Hy())
            
MI = (test.Hy() + test.Hx() - test.Hxy_1to1())/math.log(min(len(countx),len(county)), 2)

print(MI)         




        