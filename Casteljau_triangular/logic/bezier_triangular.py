# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 15:57:09 2022

@author: Darius
"""
from fractions import Fraction
from ui.reading import print_points

def find_point(degree, points, point):
    u = point[0]
    v = point[1]
    w = point[2]
    iterating_triangles = points[:]
    aux_triangles = []
    aux_degree = degree
    while(len(iterating_triangles) > 1):
        row = 1
        count = row
        for i in range(0, len(iterating_triangles)-aux_degree-1):
            if(count == 0):
                row += 1
                count = row
                print('')
            count -= 1
            p1 = iterating_triangles[i]
            p2 = iterating_triangles[i+row]
            p3 = iterating_triangles[i+row+1]
            x = Fraction(v*p1[0]+w*p2[0]+u*p3[0]).limit_denominator()
            y = Fraction(v*p1[1]+w*p2[1]+u*p3[1]).limit_denominator()
            z = Fraction(v*p1[2]+w*p2[2]+u*p3[2]).limit_denominator()
            aux_triangles.append((x,y,z))
        aux_degree -= 1
        print(print_points(aux_triangles))
        print("\n")
            
        iterating_triangles = aux_triangles[:]
        aux_triangles.clear()
    return iterating_triangles[0]