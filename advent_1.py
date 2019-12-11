# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:36:18 2019

@author: nieswand
"""

import numpy as np
import copy 
def fuel_required(mass):
    return np.max((np.floor(mass/3.) -2 , 0))

def full_fuel_required(mass):
    fuel_mass = fuel_required(mass)    
    mass_increment = copy.deepcopy(fuel_mass)
    while (mass_increment > 0):
        mass_increment = fuel_required(mass_increment)
        fuel_mass += mass_increment
    return(fuel_mass)


path= r"\\vgserv25\profile$\nieswand\Documents\code_snaps\input"

modules = np.loadtxt(path)
total_fuel = 0
for mass in modules:
    total_fuel += full_fuel_required(mass)


print(total_fuel)