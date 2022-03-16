# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:45:16 2022

@author: 皮皮卡卡
"""
import pandas as pd
import numpy as np

'''pandas privids three types data to collect data. One is series which save one dimension data,
another is dataframe can save two dimension data, the other is panel.'''

s = pd.Series([1, 3, 2, 4])

print(s.values)
print(s.index)

s2 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
print(s2.index)

df = pd.DataFrame([['a', 1, 2], ['b', 2, 5], ['c', 3, 3]], columns = ['x', 'y', 'z'])
df_1 = pd.DataFrame(np.zeros((3,3)), columns=['x', 'y', 'z'])

print(df_1)

'''use dictionary to create dataframe'''

df_2 = pd.DataFrame({'x': ['a', 'b', 'c'], 'y':range(1,4), 'z':[2, 5, 3]})
print(df_2)

check_by_name = df.iloc[:, ['y']]
check_by_number = df.iloc[:, [1]]
check_first_5 = df.head()
check_info = df.info()
f = df[df.z>=3]
f_1 = df.query("z>=3 & x='a'")

'''3D'''
a = ['a', 'b', 'c']
b = [5, 7, 9]
X,Y = np.meshgrid(a,b)
df_grid = pd.DataFrame({'x':X.flatten(), 'y':Y.flatten()})