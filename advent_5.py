# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:38:06 2019

@author: nieswand
"""

import numpy as np
import copy
import itertools

parametermodedix = {0:"position", 1:"immediate" }

class Instruction:
    def __init__(self, opcode, parameters):
        self.opcode = opcode
        self.parameters = parameters
                
    
class Parameter:
    def __init__(self, value, parametermode = "position"):
        self.value = value
        self.mode = parametermode
        
    
            
class Computer:
    def __init__(self, memory, noun = False, verb = False):
        
        self.noun = noun
        self.verb = verb
        self.memory = memory
        if(noun and verb):
            self.memory[1] = noun
            self.memory[2] = verb
        
        self.instruction_pointer = 0
    
    def read_Instruction(self):
        first = self.memory[self.instruction_pointer]
        digits = [int(d) for d in str(first)]
        parameters = np.array([])
        if np.size(digits)>1:
            opcode = digits[-2] * 10 + digits[-1]
        else:
            opcode = digits[-1]
        n_parameters = 0
        if (opcode == 1 or opcode == 2 or opcode ==7 or opcode ==8):
            n_parameters = 3
        elif (opcode == 3 or opcode == 4):
            n_parameters = 1
        elif (opcode == 5 or opcode == 6):
            n_parameters = 2
        elif (opcode == 99):
            n_parameters = 0
        else:
            print("Unknown Parameter error")
        for i, index in enumerate(np.arange(-3,-3 - n_parameters, -1)):
            if abs(index)> np.size(digits):
                parametermode = parametermodedix[0]
            else:
                parametermode = parametermodedix[digits[index]]
            parameters = np.append(parameters, Parameter(self.memory[self.instruction_pointer + i + 1], parametermode))
        return Instruction(opcode, parameters), n_parameters

    def exec_instruction(self, instruction):
        if instruction.opcode == 99:
            self.opcode_99();
            return False;
        elif instruction.opcode == 1:
            self.opcode_1(instruction.parameters)
        elif instruction.opcode == 2:
            self.opcode_2(instruction.parameters)
        elif instruction.opcode == 3:
            self.opcode_3(instruction.parameters)
        elif instruction.opcode == 4:
            self.opcode_4(instruction.parameters)
        elif instruction.opcode == 5:
            self.opcode_5(instruction.parameters)
        elif instruction.opcode == 6:
            self.opcode_6(instruction.parameters)
        elif instruction.opcode == 7:
            self.opcode_7(instruction.parameters)
        elif instruction.opcode == 8:
            self.opcode_8(instruction.parameters)
        return True
    
    def read_param(self, parameter):
        if parameter.mode == "position":
            return self.memory[parameter.value]
        elif parameter.mode == "immediate":
            return parameter.value
        else:
            print("Unknown Parameter mode")
            return np.nan
    def opcode_1(self, parameters):
        self.memory[parameters[2].value] = (self.read_param(parameters[0]) +
            self.read_param(parameters[1]))
    
    def opcode_2(self, parameters):
#        for param in parameters:
#            print(param.value)
        self.memory[parameters[2].value] = (self.read_param(parameters[0]) *
            self.read_param(parameters[1]))
    
    def opcode_3(self, parameters):
        print("OPCODE3: Input value ...")
        inputvalue = input()
        self.memory[parameters[0].value] = inputvalue
    
    def opcode_4(self, parameters):
        print("OPCODE4: Output! : " + str(self.read_param(parameters[0])))
        return self.read_param(parameters[0])
    
    def opcode_5(self, parameters):
        if(self.read_param(parameters[0]) != 0):
            self.instruction_pointer = self.read_param(parameters[1])
        else:
            self.instruction_pointer += 3
    
    def opcode_6(self, parameters):
        if(self.read_param(parameters[0]) == 0):
            self.instruction_pointer = self.read_param(parameters[1])
        else:
            self.instruction_pointer += 3
            
    def opcode_7(self, parameters):
        if(self.read_param(parameters[0]) < self.read_param(parameters[1])):
            self.memory[parameters[2].value] = 1
        else:
            self.memory[parameters[2].value] = 0
    
    def opcode_8(self, parameters):
        if(self.read_param(parameters[0]) == self.read_param(parameters[1])):
            self.memory[parameters[2].value] = 1
        else:
            self.memory[parameters[2].value] = 0
    
    def opcode_99(self):
        print("breaking...")
        
    def execute(self):
        while(True): 
            instruction, nr_params = self.read_Instruction()
            if (instruction.opcode != 5 and instruction.opcode != 6):
                self.instruction_pointer += nr_params +1
            if(False == self.exec_instruction(instruction)):
                break
#            print("pointer: " + str(self.instruction_pointer))
        return self.memory[0]
    
path= r"\\vgserv25\profile$\nieswand\Documents\code_snaps\input_5"
inp = np.loadtxt(path, dtype = int, delimiter = ",")
#inp = [1002,4,3,4,33]
compter = Computer(inp)
print(compter.execute())
