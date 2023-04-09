# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:02:28 2023

@author: Sapta Sindhu Palit
"""

a=[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
def func(x):
    return(" ".join(x))
print(list(map(func,a)))