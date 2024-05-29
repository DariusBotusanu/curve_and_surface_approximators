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
            
def read_points(num):
    points = []
    for i in range(num):
        
        print("Point {}: x =".format(i+1), end = " ")
        p1 = read_float()
        print("y =", end =" ")
        p2 = read_float()
        
        while ((p1, p2) in points):
            print("({},{}) was already entered! Enter another one".format(p1,p2))
            print("Point {}: x =".format(i+1), end = " ")
            p1 = read_float()
            print("y =", end =" ")
            p2 = read_float()
        points.append((p1, p2))
    return points

def read_weights(num):
    weights = []
    i = 1
    while(len(weights)<num):
        print("Enter weight w{} = ".format(i), end = "")
        w = read_float()
        while(w < 0):
                print("Weight should not be negative! Enter it again w{} = ".format(i), end = "")
                w = read_float()
                
        i += 1
        weights.append(w)
        
    return weights