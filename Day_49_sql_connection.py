# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:25:08 2022

@author: pikachu
"""

import sqlalchemy
import pandas as pd
import pprint

engine = sqlalchemy.create_engine(
     "mysql+pymysql://root:19991023lf2@localhost/testdb",encoding='utf8')

#engine = sqlalchemy.create_engine(DB_CONNECT, echo=True)
cnx = engine.connect()
test_query = cnx.execute("SELECT * FROM japanese;")
test_df = pd.DataFrame([dict(i) for i in test_query])
pprint.pprint(test_df)
