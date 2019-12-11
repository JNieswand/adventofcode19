# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:05:08 2019

@author: nieswand
"""
import numpy as np 
import itertools
class Coordinate():
    def __init__(self, x, y, direction, steps=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.steps = steps
        
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y, "random")
        
def append_to_coordinates(coordinateList, direction, steps, totalsteps):
    last = coordinateList[-1]
    print(str(last.x) + " " +str(last.y))
    if(direction == "U"):
        coordinateList = np.append(coordinateList, [Coordinate(last.x, last.y + steps, direction, totalsteps)],axis = 0)
    elif(direction ==  "D"):
        coordinateList = np.append(coordinateList, [Coordinate(last.x, last.y - steps, direction, totalsteps)],axis = 0)
    elif(direction ==  "R"):
        coordinateList = np.append(coordinateList, [Coordinate(last.x + steps, last.y, direction, totalsteps)],axis = 0)
    elif(direction == "L"):
        coordinateList = np.append(coordinateList, [Coordinate(last.x - steps, last.y, direction, totalsteps)],axis = 0)
    return coordinateList
def create_coordinateList(input1):        
    input1 = input1.split(",")
    
    coordinateList = np.array([Coordinate(0,0,"Empty",0)])
    totalsteps = 0
    for inp in input1:
        direction = inp[0]
        steps = int(inp[1:])
        totalsteps += steps
        coordinateList = append_to_coordinates(coordinateList, direction, steps, totalsteps)
    return coordinateList

def intersect(p1, p2, p21, p22):
    if(p1.direction == "U" or p1.direction =="D"):
        if( p21.direction == "U" or p21.direction == "D"):
            return False
        elif( min((p21.x, p22.x)) > p1.x or max((p21.x, p22.x)) < p1.x ):
            return False
        elif( min((p1.y, p2.y)) > p21.y or max((p1.y, p2.y)) < p21.y ):
            return False
        return True
       
    if(p1.direction == "L" or p1.direction =="R"):
        if( p21.direction == "L" or p21.direction == "R"):
            return False
        elif( min((p21.y, p22.y)) > p1.y or max((p21.y, p22.y)) < p1.y ):
            return False
        elif( min((p1.x, p2.x)) > p21.x or max((p1.x, p2.x)) < p21.x ):
            return False
        return True
    

    
def calculateCrossPoint(p1, p2, p21, p22):
    if(p1.direction == "U" or p1.direction =="D"):
        return Coordinate(p1.x, p21.y, "e")
    elif(p1.direction == "L" or p1.direction =="R"):
        return Coordinate(p21.x, p1.y, "e")
    return Coordinate(np.nan, np.nan, "e")
    

def distance(point):
    return abs(point.x) + abs(point.y)

def closest_distance(crosspoints):
    closestDistance = 1e10
    nearestPoint = Coordinate(100, 100, "e")
    for point in crosspoints:
        if(distance(point) < closestDistance):
            closestDistance = distance(point)
            nearestPoint = point
    return closestDistance, nearestPoint

def less_steps(crosspoints):
    minSteps = 1e10
    nearestPoint = Coordinate(100, 100, "e")
    for point in crosspoints:
        if(point.steps < minSteps):
            minSteps = point.steps
            nearestPoint = point
    return minSteps, nearestPoint
def compare_coordinateLists(list1, list2):
    
    crosspoints = np.array([])
    print("size: " +str(np.size(list1)) + " * " +str(np.size(list2)))
    for i in np.arange(1, np.size(list1)):
        for j in np.arange(1, np.size(list2)):
            if(intersect(list1[i], list1[i-1], list2[j], list2[j-1])):
                point = calculateCrossPoint(list1[i], list1[i-1], list2[j], list2[j-1])
                point.steps = list1[i-1].steps + list2[j-1].steps + distance(point- list1[i-1]) + distance(point- list2[j-1])
                crosspoints = np.append(crosspoints, [point], axis = 0)
#    closestDistance, nearestPoint = closest_distance(crosspoints)
    closestDistance, nearestPoint = less_steps(crosspoints)
    print(str(nearestPoint.x) + " " + str(nearestPoint.y))
    return closestDistance

def execute_inputs(input1, input2):
    print("create list 1...")
    list1 = create_coordinateList(input1)
    print("create list 2...")
    list2 = create_coordinateList(input2)
    print("compare...")
    print(compare_coordinateLists(list1[1:], list2[1:]))

with open('input_3', 'r') as myfile:
    data = myfile.read()
    
input1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
input2 = "U62,R66,U55,R34,D71,R55,D58,R83"

data = data.split("\n")
execute_inputs(data[0], data[1])
#execute_inputs(input1, input2)
