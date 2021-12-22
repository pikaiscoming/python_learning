# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 22:19:58 2021

@author: 皮皮卡卡
"""
import csv, pprint
with open('example.csv') as file:   #跟單純open布一樣，會自動關閉資料，指示牌版上要注意
    filereader = csv.reader(file)#他只會巡迴一次，所以之後查詢都會是最後一行
    for row in filereader:
        print(str(filereader.line_num)+ ' ' +str(row))
 

file = open('example.csv')
filereader = csv.reader(file)#他只會巡迴一次，所以之後查詢都會是最後一行
for row in filereader:
    print(str(filereader.line_num)+ ' ' +str(row))
filereader = csv.reader(file)
data = list(filereader)
print(data[1][0], filereader.line_num)
