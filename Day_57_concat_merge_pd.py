# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:24:53 2022

@author: pikachu
"""

import pandas as pd

df = pd.DataFrame({'x':['A', 'B', 'C', 'A', 'C'], '2010':[1, 3, 4, 3, 4], '2011':[3, 5, 2, 3, 1]})
df1 = pd.DataFrame(dict(x=['a', 'b', 'c'], y=range(0,3)))
df2 = pd.DataFrame(dict(z=['B', 'D', 'H'], g=[2,5,3]))
df3 = pd.DataFrame(dict(x=['g', 'd'], y=[2,5]))

df_cbind = pd.concat([df1, df2], axis=1)  #1 means 水平延伸 0 是垂直
df_rbind = pd.concat([df1, df3], axis=0)

print(df_cbind, df_rbind)


'''merge just like sql join'''

df3 = pd.DataFrame(dict(x=['a', 'b', 'c'], z = [2, 5, 3]))

df_join = pd.merge(left = df1, right = df3, how='left', on='x')

print(df_join)

df_melt = pd.melt(df, id_vars = ['x'], var_name = 'year', value_name = 'value')

print(df_melt)

'''import'''

df_in =pd.read_csv("data.csv", sep=',', header=0, index_col=None, encoding='utf8')

