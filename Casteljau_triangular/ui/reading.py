# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:30:28 2022

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

def read_degree():
    num = -1
    while (num < 0):
        try:
            num = int(input())
        except ValueError:
            print("Please enter an integer >= 0!: ")
            continue
        else:
            return num
        
def read_control_points(degree):
    #degree represents the degree of the surface
    num = (degree+1)*(degree+2)/2 #the number of points
    points = []
    i = 1
    while (len(points) < num):
        print("Enter point {}: ".format(i))
        print("x = ", end = '')
        x = read_float()
        print("y = ", end = '')
        y = read_float()
        print("z = ", end = '')
        z = read_float()
        point = (x,y,z)
        if(point in points):
            print("Please let the points be different!")
        else:
            i += 1
            points.append(point)
    return points

def print_points(points):
    n = 1
    count = 0
    points_triangle = ""
    while (count < len(points)):
        for i in range(n):
            points_triangle += str((str(Fraction(points[count][0]).limit_denominator()),
                                    str(Fraction(points[count][1]).limit_denominator()),
                                    str(Fraction(points[count][2]).limit_denominator())))
            points_triangle += " "
            count += 1
        n += 1
        points_triangle += "\n"
    return points_triangle

def read_coordinates():
    print("Enter the barycentric coordinates (u,v,w) of the point")
    print("u = ", end = '')
    u = read_float();
    while(u <0 or u >1):
        print("u should be in the [0,1] interval!\n u = ", end = '')
        u = read_float()
    print("v = ", end = '')
    v = read_float();
    while(v <0 or v >1):
        print("v should be in the [0,1] interval!\n v = ", end = '')
        v = read_float()
    w = 1 - u - v
    while(w < 0):
        print("u + v should not exceed 1!\n Enter v again: v = ", end ='')
        v = read_float();
        while(v <0 or v >1):
            print("v should be in the [0,1] interval!\n v = ", end = '')
            v = read_float()
        w = 1 - u - v
    return (u,v,w)
            
            
            
            
    