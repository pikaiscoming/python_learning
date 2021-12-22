# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 11:17:26 2021

@author: 皮皮卡卡
"""
import re

'''
Greedy and non-greedy. regular expressions are greedy by default, which means that in ambiguous 
situations they will match the "longest string".
'''
haregex = re.compile('(ha){3,5}')
mo1 = haregex.search('hahahahaha')
print(mo1.group())

'''
findall will return a list of strings which match the regex. and if there are the groups in 
regular expression, then it will return a list of 'tuples'
'''
phonenumberRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d') #has no groups
num = phonenumberRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(num)

phonenumberRegex = re.compile('(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #has groups
num = phonenumberRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(num)

nongreedyRegex = re.compile('<.*?>')    #use question mark to control greedy or not
non = nongreedyRegex.search('<To serve man> for dinner.>')
print(non.group())

greedyRegex = re.compile('<.*>')
greedy = greedyRegex.search('<To serve man> a dinner>')
print(greedy.group())

'''
the dot-star('.*') will match everything except a newline(\n)
'''

beginsWithHello = re.compile('^Hello')
result = beginsWithHello.search('Hello, world!')
print(result.group())


