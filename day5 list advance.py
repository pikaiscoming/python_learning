# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:57:41 2021

@author: 皮皮卡卡
"""
print('''Dear Alice,
      
      Eve's cat has been arrested for catnapping, cat burglary, and extortion.
      
      Sincerely,
      Bob''')

print('Dear Alice,\n\n\
      Eve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\n\
      Sincerely,\n\
      Bob')

"""this can let user type comments without the limit
"""
#but this way only can use for one line

first = 'great'
second = 'GReat'
second = second.lower()
print(first == second)
print(first.isupper())
print(first.upper().isupper())
#only number and not empty isdecimal()
#only number and litter but not empty isalnum()
#only litter and not empty isalpha()
spam = ['i', 'want', 'to', 'play', 'a', 'game']
print('1'.join(spam))
print('my1name1i1simon'.split('1'))
print('abcd'.rjust(20))
print('abcd'.ljust(20, 'a')) #total 20 litters
number = '   123   '
print(number.strip(' '))
print(number.rstrip(' '))