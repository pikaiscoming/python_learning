# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:17:04 2021

@author: 皮皮卡卡
"""
import openpyxl, pprint


print('Opeining workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData={}

print('reading rows...')

for row in range(2, sheet.max_row+1):
    state = sheet['B' + str(row)].value
    county = sheet['C' +str(row)].value
    pop = sheet['D' + str(row)].value
    
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts':0, 'pop':0})
    countyData[state][county]['tracts'] +=1
    countyData[state][county]['pop'] += int(pop)

popdata = open(file='pop.txt', mode='w')    
print('alldata = ' + pprint.pformat(countyData), file=popdata)
popdata.close()