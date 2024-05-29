# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:32:33 2021

@author: Darius
"""
from fractions import Fraction

def iterated_Casteljau(n, m, points, pair):
    # n=2 m=2
    #points is a (n+1)x(m+1) matrix
    #points is of the form
    #   [[00 01 02]
    #    [10 11 12]
    #    [20 21 22]]
    # we will apply the algorithm on u, then on v, where (u,v) is the pair
    aux_list = []
    aux_matrix = []
    iteration_matrix = points[:] #first step of the algorithm
    #now we begin the actual algorithm
    first_matrix = []
    for r in range(1, n+1): 
        print("r = {}".format(r))
        for i in range(0,n-r+1):
            print("\ti = {}".format(i))
            for j in range(0,m+1):
                print("\t\tj = {}".format(j))
                aux1 = (1-pair[0])*iteration_matrix[i][j][0]+pair[0]*iteration_matrix[i+1][j][0]
                aux2 = (1-pair[0])*iteration_matrix[i][j][1]+pair[0]*iteration_matrix[i+1][j][1]
                aux3 = (1-pair[0])*iteration_matrix[i][j][2]+pair[0]*iteration_matrix[i+1][j][2]
                aux_list.append((Fraction(str(aux1)),Fraction(str(aux2)),Fraction(str(aux3))))
                print("\t\t\t("+str(Fraction(aux1))+", "+str(Fraction(aux2))+", "+str(Fraction(aux3))+")")
            aux_matrix.append(aux_list[:])
            for elem in aux_list:
                print("\t\t("+str(Fraction(elem[0]).limit_denominator())+", "
                      +str(Fraction(elem[1]).limit_denominator())+", "+str(Fraction(elem[2]).limit_denominator())+") |", end ="")
            print("\n")
            aux_list.clear()
        
        iteration_matrix = aux_matrix[:]
        aux_matrix.clear()
    iteration_list = iteration_matrix[0]
    
    print("ITERATION LIST")
    for elem in iteration_list:
        print("\t\t("+str(Fraction(elem[0]).limit_denominator())+", "+str(Fraction(elem[1]).limit_denominator())+", "+str(Fraction(elem[2]).limit_denominator())+") |", end ="")
    print("\n")
    print("-------------")
    for s in range(1,m+1):
        print("s = {}".format(s))
        for j in range(0,m-s+1):
            print("\tj = {}".format(j))
            aux1 = Fraction((1-pair[1])*iteration_list[j][0]+pair[1]*iteration_list[j+1][0]).limit_denominator()
            aux2 = Fraction((1-pair[1])*iteration_list[j][1]+pair[1]*iteration_list[j+1][1]).limit_denominator()
            aux3 = Fraction((1-pair[1])*iteration_list[j][2]+pair[1]*iteration_list[j+1][2]).limit_denominator()
            aux_list.append((Fraction(str(aux1)).limit_denominator(),Fraction(str(aux2)).limit_denominator(),Fraction(str(aux3)).limit_denominator()))
            print("\t\t("+str(Fraction(aux1).limit_denominator())+", "+str(Fraction(aux2).limit_denominator())+", "+str(Fraction(aux3).limit_denominator())+")")
            
        for elem in aux_list:
            print("("+str(Fraction(elem[0]).limit_denominator())+", "+str(Fraction(elem[1]).limit_denominator())+", "+str(Fraction(elem[2]).limit_denominator())+")" + "  ", end = " ")
        print("\n")
        iteration_list = aux_list[:]
        aux_list.clear()
            
    
    
    
    # for r in range (1,n+1):
    #     print("r = {}".format(r))
    #     for i in range(0,n+1-r):
    #         print("\ti = {}".format(i))
    #         for j in range(0,m+1):
    #             print("\t\tj = {}".format(j))
    #             aux1 = (1-pair[0])*iteration_matrix[i][j][0]+pair[0]*iteration_matrix[i+1][j][0]
    #             aux2 = (1-pair[0])*iteration_matrix[i][j][1]+pair[0]*iteration_matrix[i+1][j][1]
    #             aux3 = (1-pair[0])*iteration_matrix[i][j][2]+pair[0]*iteration_matrix[i+1][j][2]
    #             aux_list.append((Fraction(str(aux1)),Fraction(str(aux2)),Fraction(str(aux3))))
    #             print("\t\t\t("+str(Fraction(aux1))+", "+str(Fraction(aux2))+", "+str(Fraction(aux3))+")")
            
    #         aux_matrix.append(aux_list[:])
    #         aux_list.clear()
    #     iteration_matrix = aux_matrix[:]
    #     aux_matrix.clear()
    
    # iteration_list = iteration_matrix[0]
    # for s in range(1,m+1):
    #     for j in range(0,m+1-s):
    #         aux1 = Fraction((1-pair[1])*iteration_list[j][0]+pair[1]*iteration_list[j+1][0]).limit_denominator()
    #         aux2 = Fraction((1-pair[1])*iteration_list[j][1]+pair[1]*iteration_list[j+1][1]).limit_denominator()
    #         aux3 = Fraction((1-pair[1])*iteration_list[j][2]+pair[1]*iteration_list[j+1][2]).limit_denominator()
    #         aux_list.append((aux1,aux2,aux3))
    #     iteration_list = aux_list[:]
    #     aux_list.clear()
    return(iteration_list[0])
    