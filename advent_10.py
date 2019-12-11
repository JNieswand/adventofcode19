# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:13:58 2019

@author: nieswand
"""
import numpy as np
import copy
import matplotlib.pyplot as plt
def flip_array(a):
    n = len(a)
    for i in range(0, n):
        for j in range(i+1, n):
            a[i][j],a[j][i] = a[j][i],a[i][j]
    return a
def read_input(string_input):
    print("reading input...")
    string_input = string_input.split("\n")[:-1]
    out = np.zeros(shape = (len(string_input[0]), np.size(string_input)))
    for i,line in enumerate(string_input):
        line = line.replace(".", "0").replace("#", "1")        
        out[:,i] = [int(k) for k in line]
    return out
    
def is_vector_in_array(array, vector):
    if (vector[0]>= np.shape(array)[0] or 
        vector[1]>= np.shape(array)[1] or
        vector[0] < 0 or
        vector[1] < 0):
        return False
    return True

def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_maximum_stepsize(array, position):
    xrange = (0, np.shape(array)[0])
    yrange = (0, np.shape(array)[1])
    
    corners = np.array([(xrange[0], yrange[0]),
                        (xrange[0], yrange[1] -1),
                        (xrange[1] -1, yrange[0]),
                        (xrange[1] -1, yrange[1] -1)])
    max_dist = 0
    max_corner = (0,0)
    for corner in corners:
        if distance(position, corner) > max_dist:
            max_dist = distance(position, corner)
            max_corner = corner
    x_stepsize = np.abs(max_corner[0] - position[0])
    y_stepsize = np.abs(max_corner[1] - position[1]) 
    
    return x_stepsize, y_stepsize
    
def get_angles_array(array, position):
    array_angles = copy.deepcopy(array)
    for x in np.arange(0, np.shape(array)[0]):
        for y in np.arange(0, np.shape(array)[1]):
            if array[x,y] == 0:
                array_angles[x,y] = np.nan
                continue
            if position[0] == x and position[1] == y:
                array_angles[x,y] = np.nan
                continue

            array_angles[x,y] = np.angle( complex( x-position[0], y-position[1]), deg = True)

    return array_angles
def count_for_pos(array, pos):
    angles = get_angles_array(array, pos)
    angle_list = np.array([])
    for x in np.arange(0, np.shape(angles)[0]):
        for y in np.arange(0, np.shape(angles)[1]):
            if np.isnan(angles[x,y]):
                continue
            if angles[x,y] in angle_list:
                continue
            else:
                angle_list = np.append(angle_list, angles[x,y])
    print(angle_list)
    print(angles)
    return np.size(angle_list)

def exec_max_nr(array):
    max_nr_visual = 0
    max_pos = (0,0)
    sol_array = copy.deepcopy(array)
    for x in np.arange(np.shape(array)[0]):
        for y in np.arange(np.shape(array)[1]):
            pos = (x,y)
            if array[x,y] == 0:
                continue
            nr_pos = count_for_pos(array, pos)
            sol_array[y,x] = nr_pos
            if nr_pos >max_nr_visual:
                max_nr_visual = nr_pos
                max_pos = pos
    print(max_pos)
    print(max_nr_visual)
#    print(sol_array)

if __name__ == "__main__":
#    string = ("......#.#.\n"+
#    "#..#.#....\n"+
#    "..#######.\n"+
#    ".#.#.###..\n"+
#    ".#..#.....\n"+
#    "..#....#.#\n"+
#    "#..#....#.\n"+
#    ".##.#..###\n"+
#    "##...#..#.\n"+
#    ".#....####")
#    string = (".#..#\n"+
#               ".....\n"+
#               "#####\n"+
#               "....#\n"+
#               "...##")
    path= r"\\vgserv25\profile$\nieswand\Documents\code_snaps\input_10"
    string = ""
    with open(path) as fp:
        print(fp)
        string =fp.read()
    print(string)
    array = read_input(string)
    
#    exec_max_nr(array)
    pos = (2,2)
#    print(get_maximum_stepsize(array, pos))
    print(exec_max_nr(array))

        
            
        