# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:55:50 2021

@author: Darius
"""

from fractions import Fraction

def read_float():
    num = 0.
    while True:
        try:
            num = Fraction(input()).limit_denominator()
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            return num

def read_delta():
    num = -1.
    while (num <= 0):
        try:
            num = float(input())
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            return num

def read_vector():
    print("\tx = ", end = "")
    x = read_float()
    print("\n\ty = ", end = "")
    y = read_float()
    print("\n\tz = ", end = "")
    z = read_float()
    return (x,y,z)
    
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
            

def read_points(n):
    control_points = []
    for i in range(0, n+1):
        print("Enter b_{} ".format(i))
        print("\tx = ", end = "")
        x = read_float()
        print("\n\ty = ", end = "")
        y = read_float()
        print("\n\tz = ", end = "")
        z = read_float()
        
        control_points.append((x,y,z))
          
    return control_points

def read_pair():
    print("Enter u_0 = : ", end = "")
    u = read_float()
    while(u < 0 or u > 1):
        print("The number should be in the [0,1] interval! Enter it again: ", end="")
        u = read_float()
    print("Enter v_0 = : ", end = "")
    v = read_float()
    while(u < 0 or u > 1):
        print("The number should be in the [0,1] interval! Enter it again: ", end="")
        v = read_float()
    return (u,v)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    