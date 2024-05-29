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
            

def read_points_matrix(n, m):
    points_matrix =[]
    for i in range(0,n+1):
        points_matrix.append([]);
        for j in range(0,m+1):
            print("Enter b{}{}:".format(i,j))
            print("x = ", end = "")
            p1 = read_float()
            print("y = ", end ="")
            p2 = read_float()
            print("z = ", end ="")
            p3 = read_float()
            points_matrix[i].append((p1,p2,p3))     
    return points_matrix

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    