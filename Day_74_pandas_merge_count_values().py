# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 20:44:24 2022

@author: pikachu
"""
#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%

df = pd.read_csv(r'C:\Users\pikachu\OneDrive\桌面\viz&analysis_python\Data Science Job Salaries\ds_salaries.csv', index_col=0)

df.info()
df.head()
df.tail()
df.columns

#%%
# work_year

print(df['work_year'].value_counts(dropna=False))

# 2022    318
# 2021    217
# 2020     72

print(df['experience_level'].value_counts(dropna=False))

# SE    280
# MI    213
# EN     88
# EX     26

print(df['employment_type'].value_counts(dropna=False))

# SE    280
# MI    213
# EN     88
# EX     26

print(df['job_title'].value_counts())
# Data Scientist                              143
# Data Engineer                               132
# Data Analyst                                 97
# Machine Learning Engineer                    41
# Research Scientist                           16
# Data Science Manager                         12
# Data Architect                               11
# Big Data Engineer                             8
#...

print(df['employee_residence'].value_counts())

#len() = 57

print(df['company_location'].value_counts())

#len() = 50

print(df['company_size'].value_counts())

# M    326
# L    198
# S     83

'''or you can use loop to print them'''

print([pd.DataFrame(df[col].value_counts())  for col in df.columns])
#%%
'''experiment level and salary in usd'''

#method 1
ndf = df[['experience_level', 'salary_in_usd']].copy()
ndf = ndf.groupby(['experience_level'])['salary_in_usd'].agg('mean').reset_index()
count = dict(df['experience_level'].value_counts())
ndf['count'] = ndf['experience_level'].map(count)

#method 2 df merge df
count1 = df['experience_level'].value_counts().rename_axis('unique_values').to_frame('counts')  #one columns
count2 = df['experience_level'].value_counts().rename_axis('experience_level').reset_index(name='counts') #a df
ndf= pd.merge(ndf, count)
ndf

fig = plt.figure(figsize=(10, 6), dpi=80, facecolor='w', edgecolor='w')
# x = np.arange(1, 25)
# plt.bar(x,every_hour_fraud, width=0.65, color='firebrick', alpha = 1)

# plt.title('Fraudulent Transactions in 24 Hours', fontsize=15, y=1.03)
# plt.xlabel("24 hours ",fontsize=13)
# plt.xticks(np.arange(1, 33, 2))
# plt.ylabel("Number of fraudulent transactions",fontsize=13)
# #plt.yaxis.set_label_coords(-.1, .1)
# plt.axhline(y=342.2, linewidth = 2, c='royalblue')
# plt.axis([0.5, 24.5, 0, 500])
