# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 08:35:11 2019

@author: nieswand
"""

import numpy as np
import matplotlib.pyplot as plt

def count_str(layer, string):
    counter = 0
    for line in layer:
        line = list(line)
        for symbol in line:
            if symbol == string:
                counter += 1
    return counter

inp = str(123456789012)
path= r"\\vgserv25\profile$\nieswand\Documents\code_snaps\input_8"
with open(path) as fp:
    for line in fp:
        inp = line.strip()
width = 25
height = 6

lines = [inp[i:i+width] for i in range(0, len(inp), width)]
layers = [lines[i:i + height] for i in range(0, len(lines), height)] 

def exec_part1(layers):
    layermin = []
    min_nr_zeros = 1000
    for layer in layers:
        nr_zeros = count_str(layer, "0")
        if nr_zeros< min_nr_zeros:
            min_nr_zeros = nr_zeros
            layermin = layer
    
    print(count_str(layermin, "1") * count_str(layermin, "2"))


buffer_pic = np.ones(shape = (height, width)) * 2

for layer in layers:
    for i,line in enumerate(layer):
        for j,symbol in enumerate(line):
            if buffer_pic[i,j] == 2:
                buffer_pic[i, j] = int(symbol)
                
plt.imshow(buffer_pic)