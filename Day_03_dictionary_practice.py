# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:54:26 2021

@author: 皮皮卡卡
"""
stuff = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow':12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def display(items, lists):
    print("Inventory:")
    total = 0
    for tools in lists:
        if tools in items: 
            items[tools] = items.get(tools, 0) + 1
        else:
            items.setdefault(tools, 1)
    
    for k, v in items.items():
        print(str(v) + ' ' + k)
            
        
        
    
display(stuff, loot)
