# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:35:31 2019

@author: nieswand
"""
import numpy as np

def count_orbits(planet , planetlist):
    if planet == "COM":
        return 0;

    return(count_orbits(planetlist[planet], planetlist) + 1)
    
def get_inherited_objects(planet, inherited_objects, planetlist):
    if planet == "COM":
        return inherited_objects;
    inherited_objects =np.append(inherited_objects, planetlist[planet])

    return(get_inherited_objects(planetlist[planet],inherited_objects, planetlist))

def read_planet_dictionary(path):
    planetlist = {}
    with open(path) as fp:
        for line in fp:
            line = line.split(")")
            
            planetlist[line[1].strip()] = line[0]
    return planetlist           

    

path= r"\\vgserv25\profile$\nieswand\Documents\code_snaps\input_6"
planetlist = read_planet_dictionary(path)
#inp = np.loadtxt(path, delimiter = ",")

#inp = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
#inp = inp.split("\n")
count = 0
inherited_objects_dictionary = {}
for item in planetlist.items():
    inherited_objects = np.array([])
    count += count_orbits(item[0], planetlist)
    inherited_objects = get_inherited_objects(item[0], inherited_objects, planetlist)
    inherited_objects_dictionary[item[0]] = inherited_objects
    
print(inherited_objects_dictionary["SAN"])
print(inherited_objects_dictionary["YOU"])
path_santa = np.flip(inherited_objects_dictionary["SAN"])
path_you = np.flip(inherited_objects_dictionary["YOU"])

for i,(obj_san, obj_you) in enumerate(zip(path_santa, path_you)):
    if obj_san != obj_you:
        print(np.size(path_santa)-i + np.size(path_you) - i)
        break