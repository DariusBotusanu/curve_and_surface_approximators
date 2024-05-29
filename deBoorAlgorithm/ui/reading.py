'''
Created on Nov 11, 2021

@author: Darius
'''
import logic.Point as pt

from fractions import Fraction

def read_float():
    num = 0.
    while True:
        try:
            num = Fraction(input())
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            return num


def read_int():
    num = 0
    while True:
        try:
            num = int(input())
        except ValueError:
            print("Please enter an integer!: ")
            continue
        else:
            return num
            
def read_point():
    print("x = ", end ="")
    x = read_float()
    print("y = ", end = "")
    y = read_float()
    return pt.Point(x,y) 

def read_control_points(num):
    '''
    Returns a list of the control points (the points will be different)
    Params:
    - num: represents the number of points 
    '''
    points = []
    i = 1
    while(i <= num):
        print("Enter the #{} point: ".format(i))
        pt = read_point()
        if pt in points:
            print("The points need to be different!")
        else:
            points.append(pt)
            i += 1
    return points

def read_nodes(num):
    '''
    Returns a list of the nodes (sorted ascendingly)
    Params:
    - num: represents the number of nodes
    '''
    nodes = []
    i = 0
    while(i < num):
        print("t{} = ".format(i), end = '')
        t = read_float()
        nodes.append(t)
        i += 1
    nodes.sort()
    return nodes

def read_t(nodes):
    '''
    '''
    print("Enter t (needs to be between {} and {}): ".format(nodes[3], nodes[5]), end ="")
    t = read_float()
    while(t < nodes[3] or t > nodes[5]):
        print("Please enter a number between {} and {} : ".format(nodes[3], nodes[5]), end="")
        t = read_float();
    return t
        
        
