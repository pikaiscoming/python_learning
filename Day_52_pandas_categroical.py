# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:18:01 2022

@author: 皮皮卡卡
"""
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype

cut = ["Fair", "Good", "Very", "Premium", "Ideal"]
cut_facorl = pd.Categorical(cut) #order by letter
cut_facorl2 = pd.Categorical(cut, categories=["Good", "Fair", "Very", "Ideal", "Premium"],
                            ordered=True)
#cut_facorl2 = cut.astype(CategoricalDtype(categories=["Good", "Fair", "Very", "Ideal", "Premium"],
                                           #ordered=True))
#print(cut_facorl2)

df = pd.DataFrame({'x':['a', 'b','c'], '2022':[1, 3, 4], '2023':[3, 5, 2]})
print(df)
df_melt = pd.melt(df,id_vars='x', var_name='year', value_name='value')
print(df_melt)
df_pivot = df_melt.pivot_table(index = 'x', columns='year', values='value')
df_pivot = df_pivot.reset_index()
print(df_pivot)