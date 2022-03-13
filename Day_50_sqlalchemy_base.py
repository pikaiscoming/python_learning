# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:20:08 2022

@author: pikachu
"""

import sqlalchemy
import pandas as pd


engine = sqlalchemy.create_engine(
     "mysql+pymysql://root:19991023lf2@localhost/testdb",encoding='utf8')

#engine = sqlalchemy.create_engine(DB_CONNECT, echo=True)
cnx = engine.connect()
test_query = cnx.execute("SELECT * FROM testdb.japanese;")
#test_df = pd.DataFrame([dict(i) for i in test_query])
values = test_query.fetchall()

print(values)


