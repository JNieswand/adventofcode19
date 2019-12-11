# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:04:10 2019

@author: nieswand
"""

## part 1
import numpy as np
def read_code(code):
    adjacent_double = False
    for i,digit in enumerate(code):
        if i == 0:
            continue
        if digit< code[i-1]:
            return False
        elif digit == code[i-1]:
            adjacent_double = True
    return adjacent_double



##part 2

def read_code2(code):
    in_double = False
    in_triple_or_longer = False
    adjacent_double = False
    for i,digit in enumerate(code):
        if i == 0:
            continue
        if digit< code[i-1]:
            return False
        elif digit == code[i-1]:
            if in_triple_or_longer:
                continue
            elif in_double:
                in_double = False
                in_triple_or_longer = True
            else:
                in_double = True
        else:
            in_triple_or_longer = False
            if in_double:
                adjacent_double = True
    if in_double:
        adjacent_double = True
    return adjacent_double


count = 0
for i in np.arange(367479, 893699):
    if(read_code2([int(d) for d in str(i)])):
        count +=1
        print(i)
        
print(count)