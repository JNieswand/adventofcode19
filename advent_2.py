# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:47:10 2019

@author: nieswand
"""
import numpy as np
import copy
import itertools

class Instruction:
    def __init__(self, opcode, parameters):
        self.opcode = opcode
        self.parameters = parameters
            
class Computer:
    def __init__(self, noun, verb, memory):
        
        self.noun = noun
        self.verb = verb
        self.memory = memory
        self.memory[1] = noun
        self.memory[2] = verb
        
        self.instruction_pointer = 0
    
    def exec_instruction(self, instruction):
        if instruction.opcode == 99:
            self.opcode_99();
            return False;
        elif instruction.opcode == 1:
            self.opcode_1(instruction.parameters)
        elif instruction.opcode == 2:
            self.opcode_2(instruction.parameters)
        return True
    
    def opcode_1(self, parameters):
        self.memory[parameters[2]] = (self.memory[parameters[0]] +
            self.memory[parameters[1]])
    
    def opcode_2(self, parameters):
        self.memory[parameters[2]] = (self.memory[parameters[0]] *
            self.memory[parameters[1]])
    
    def opcode_99(self):
        print("breaking...")
        
    def execute(self):
        while(True): 
            instruction = Instruction(self.memory[self.instruction_pointer],
                    self.memory[self.instruction_pointer + 1 : self.instruction_pointer +4])
#            print(instruction.opcode)
#            print(instruction.parameters)
            if(False == self.exec_instruction(instruction)):
                break
            self.instruction_pointer += 4;
            
        return self.memory[0]

path= r"\\vgserv25\profile$\nieswand\Documents\code_snaps\input_2"
inp = np.loadtxt(path, dtype = int, delimiter = ",")
noun = 12
verb = 2
compter = Computer(noun, verb, copy.deepcopy(inp))


print(compter.execute())

### part 2 ###

output = 0
verb = 0
noun = 0
compter = Computer(noun, verb, copy.deepcopy(inp))
buf1 = np.arange(100)
buf2 = np.arange(100)
for noun, verb in itertools.product( buf1, buf2):
    print("Noun: " + str(noun))
    print("Verb: " + str(verb))
    compter.__init__(noun, verb, copy.deepcopy(inp))
    output = compter.execute()
    if(output == 19690720):
        print("stopping... result is")
        print(100 *noun + verb)
        break
 