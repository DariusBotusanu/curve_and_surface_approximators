# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:11:24 2021

@author: Darius
"""
from fractions import Fraction

def homogenous_points(points, weights):
    #the parameters are a list of points and their corresponding weights
    homog_points = []
    for i in range(0,len(points)):
        if(weights[i] == 0):
            homog_points.append([points[i][0], points[i][1], 0])
        else:
            x = points[i][0] * weights[i]
            y = points[i][1] * weights[i]
            homog_points.append([x, y, weights[i]])
    return homog_points

def rational_casteljau_2d(n,points, weights, t):
        
    it_points = points[:]
    it_weights = weights[:]
    aux_points = []
    aux_weights = []
    for j in range(1, n+1):
        print("j = {}".format(j))
        for i in range(0, n+1-j):
            print("\ti = {}".format(i))
            w_j_i = Fraction((1-t)*it_weights[i] + t*it_weights[i+1]).limit_denominator()
            aux1 = Fraction((1-t)*(it_weights[i]/w_j_i)*it_points[i][0] + t*(it_weights[i+1]/w_j_i)*it_points[i+1][0]).limit_denominator()
            aux2 = Fraction((1-t)*(it_weights[i]/w_j_i)*it_points[i][1] + t*(it_weights[i+1]/w_j_i)*it_points[i+1][1]).limit_denominator()
            b_j_i = (aux1,aux2)
            aux_points.append(b_j_i)
            aux_weights.append(w_j_i)
            print("\t\tw_{}_{} = {}".format(j,i, w_j_i))
            print("\t\tb_{}_{} = ".format(j,i) + "(" +str(Fraction(str(b_j_i[0]))) +", " + str(Fraction(str(b_j_i[1]))) +")")
        it_points = aux_points[:]
        it_weights = aux_weights[:]
        aux_points.clear()
        aux_weights.clear()
        print("Points: " + str(it_points))
        print("Weights: " + str(it_weights))
    return it_points[0]
    