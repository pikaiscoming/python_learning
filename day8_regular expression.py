# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 00:10:28 2021

@author: 皮皮卡卡
"""
import re
phoneNumRegex = re.compile('(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My numver is 415-555-4242.')   #search for which group with what 
print('Phone number found:' + mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group())   #show all
print(mo.groups())  #all groups a tyoe of turple
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())  #如果都府和條件的話，會顯示先符合的條件
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
test = batRegex.search('Batmobile lost a wheel')
print(test.group()) #剛好是Bat
print(test.group(1))    #g使Bat後面剛好可以配合的那一項

'''
optional matching with question mark
(...)? 這裡面的字串可以可無
'''
questionmark = re.compile('bat(wo)?man') 
m = questionmark.search('the adventures of batwoman')
m1 = questionmark.search('the adventures of batman')