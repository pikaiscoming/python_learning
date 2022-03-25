# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:13:17 2022

@author: 皮皮卡卡
"""
import pandas as pd
import numpy as np
import apyori
import mlxtend

df = pd.DataFrame({'x':['a', 'b','c'], '2022':[1, 3, 4], '2023':[3, 5, 2]})
df_melt = pd.melt(df, id_vars='x', var_name='year', value_name='value')
#df_melt['value2'] = df_melt['value'] #easy to create another coulumn with cal

# df_melt['value2'] = df_melt.apply(lambda x: x['value']*2 
#                                      if x['year']=="2022" else x['value'], axis=1)

def f(c):
    if c['year'] == '2022':
        return c['value']*2
    return c['value']

df_test = df_melt.copy()
df_test['value2'] = df_test.apply(f, axis=1)

#df_melt['value2'] = df_melt.transform(lambda x: x*2, axis=1)

print(df_test)

'''x 是 代表axis=1這欄的值代入計算'''
