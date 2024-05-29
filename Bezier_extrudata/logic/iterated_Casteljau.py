# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:32:33 2021

@author: Darius
"""

from fractions import Fraction

def get_extrudated_points_matrix(points, delta, v):
    control_matrix = []
    for i in range(len(points)):
        control_matrix.append([])
        #b_i_0 = b_i for i = 0,...,n 
        control_matrix[i].append(points[i])
        #b_i_1 = b_i + delta*v for i = 0,...,n
        control_matrix[i].append((points[i][0] + delta*v[0], 
                                  points[i][1] + delta*v[1], 
                                  points[i][2] + delta*v[2]))
    return control_matrix
    
    
def iterated_Casteljau(points, delta, v, pair):
    n = len(points)-1
    aux_list = []
    aux_matrix = []
    iteration_matrix = get_extrudated_points_matrix(points, delta, v)
    #now we begin the actual algorithm
    for r in range(1, n+1): 
        print("r = {}".format(r))
        for i in range(0,n-r+1):
            print("\ti = {}".format(i))
            for j in range(0,1+1):
                print("\t\tj = {}".format(j))
                aux1 = Fraction((1-pair[0])*iteration_matrix[i][j][0]+pair[0]*iteration_matrix[i+1][j][0]).limit_denominator()
                aux2 = Fraction((1-pair[0])*iteration_matrix[i][j][1]+pair[0]*iteration_matrix[i+1][j][1]).limit_denominator()
                aux3 = Fraction((1-pair[0])*iteration_matrix[i][j][2]+pair[0]*iteration_matrix[i+1][j][2]).limit_denominator()
                aux_list.append((aux1, aux2, aux3))
                print("\t\t\t("+str(aux1)+", "+str(aux2)+", "+str(aux3)+")")
            aux_matrix.append(aux_list[:])
            for elem in aux_list:
                print("\t\t("+str(elem[0])+", "
                      +str(elem[1])+", "+str(elem[2])+"), ", end ="")
            print("\n")
            aux_list.clear()
        iteration_matrix = aux_matrix[:]
        aux_matrix.clear()
        
    iteration_list = iteration_matrix[0]
    
    print("ITERATION LIST")
    for elem in iteration_list:
        print("\t\t("+str(elem[0])+", "
              +str(elem[1])+", "+str(elem[2])+"), ", end ="")
    print("\n")
    print("-------------")
    for s in range(1,1+1):
        print("s = {}".format(s))
        for j in range(0,1-s+1):
            print("\tj = {}".format(j))
            aux1 = Fraction((1-pair[1])*iteration_list[j][0]+pair[1]*iteration_list[j+1][0]).limit_denominator()
            aux2 = Fraction((1-pair[1])*iteration_list[j][1]+pair[1]*iteration_list[j+1][1]).limit_denominator()
            aux3 = Fraction((1-pair[1])*iteration_list[j][2]+pair[1]*iteration_list[j+1][2]).limit_denominator()
            aux_list.append((Fraction(str(aux1)).limit_denominator(),Fraction(str(aux2)).limit_denominator(),Fraction(str(aux3)).limit_denominator()))
            print("\t\t("+str(aux1)+", "+str(aux2)+", "+str(aux3)+")")
            
        for elem in aux_list:
            print("\t\t("+str(elem[0])+", "
                  +str(elem[1])+", "+str(elem[2])+"), ", end ="")
        print("\n")
        iteration_list = aux_list[:]
        aux_list.clear()
    return iteration_list[0]