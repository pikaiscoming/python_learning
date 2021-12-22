# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 23:14:06 2021

@author: 皮皮卡卡
"""
TheBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ',
            'midL': ' ', 'midM': ' ', 'midR': ' ',
            'lowL': ' ', 'lowM': ' ', 'lowR': ' '}

def printooxx (board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'], end='\n\n')
    

choose = 'O'
for i in range(9):
    printooxx(TheBoard)
    print('Now please write the ' + choose)
    move = input()
    TheBoard[move] = choose
    if choose == 'O':
        choose = 'X'
    else:
        choose = 'O'


