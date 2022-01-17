# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:39:16 2022

@author: pikachu
"""

import js2py

f = js2py.eval_js('{console.log("hello world"); }')

print(f)