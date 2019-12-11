# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:38:51 2019

@author: nieswand
"""
from int_computer import Computer
import itertools
import copy
import numpy as np

class Amplifier:
    def __init__(self,phase_setting , program):
        self.phase_setting =phase_setting
        self.input_signal = inp
        self.program = program
    def run_program(self, inp):
        print("running program:..")
        comp = Computer(self.program, False, False, "auto", [self.phase_setting, inp])
        comp.execute()
        return comp.output
class Connected_amps:
    def __init__(self, phases, program):
        self.ampA = Amplifier( phases[0], copy.deepcopy(program))
        self.ampB = Amplifier( phases[1], copy.deepcopy(program))
        self.ampC = Amplifier( phases[2], copy.deepcopy(program))
        self.ampD = Amplifier( phases[3], copy.deepcopy(program))
        self.ampE = Amplifier( phases[4], copy.deepcopy(program))
    
    def execute(self, inp):  
        out = self.ampA.run_program(inp)
        out = self.ampB.run_program(out)
        out = self.ampC.run_program(out)
        out = self.ampD.run_program(out)
        out = self.ampE.run_program(out)
        print(out)
        return out       

### part 1 
        
#phases = [0,1,2,3,4]
#
#path= r"\\vgserv25\profile$\nieswand\Documents\code_snaps\input_7"
#program = np.loadtxt(path, dtype = int, delimiter = ",")
#permutations = [i for i in itertools.permutations(phases, 5)]
#
#largest_output = 0
#largest_out_permutation = []
#for permutation in permutations:
#    amps = Connected_amps(permutation, program) 
#    out = amps.execute(0)
#    if out > largest_output:
#        largest_out_permutation = permutation
#        largest_output = out
#print(largest_output)
#print(largest_out_permutation)
    
### part 2 ###
        
program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

phases = [5,6,7,8,9]

largest_output = 0
largest_out_permutation = []
for permutation in permutations:
    amps = Connected_amps(permutation, program)
    out = 0
    while(True):
        out = amps.execute(out)
    if out > largest_output:
        largest_out_permutation = permutation
        largest_output = out
print(largest_output)
print(largest_out_permutation)
