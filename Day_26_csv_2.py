# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:09:45 2021

@author: 皮皮卡卡
"""
import csv 

'''deal with the csv data with header. just like using dictionary key to get value.'''
examplefile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(examplefile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
    
'''if i want to deal with the data without header, we can create it by youself'''

exampleFile = open('example.csv')
exampleDictReader = csv.Dict_reader(exampleFile, ['time', 'name', 'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])
    
#can use DictWriter
