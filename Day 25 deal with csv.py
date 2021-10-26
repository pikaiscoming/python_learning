# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:41:47 2021

@author: 皮皮卡卡
"""
import csv 
outfile = open('output.csv', 'w', newline='')# just remember wirte newline in function 
#or line distance will become two times bigger
outfilewriter = csv.writer(outfile)
outfilewriter.writerow(['spam', 'eggs', 'bacon', 'ham'])

csvfile = open('output.tsv', 'w', newline='')
csvwriter = csv.writer(csvfile, delimiter='\t', lineterminator='\n\n') #pinrt 的 sep and end

'''deal with the csv data with header'''



