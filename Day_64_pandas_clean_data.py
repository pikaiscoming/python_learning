# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:57:06 2022

@author: 皮皮卡卡
"""
import pandas as pd
import sqlalchemy
import pprint
'''need to install pymysql'''
engine = sqlalchemy.create_engine(
     "mysql+pymysql://root:19991023lf2@localhost/testdb",encoding='utf8')

#engine = sqlalchemy.create_engine(DB_CONNECT, echo=True)
cnx = engine.connect()
test_query = cnx.execute("SELECT * FROM daily_tw;")
test_df = pd.DataFrame([dict(i) for i in test_query])
pprint.pprint(test_df)

mask = test_df.county != '空值'
df = test_df[mask]