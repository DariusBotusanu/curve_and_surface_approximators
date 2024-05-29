'''
Created on Nov 12, 2021

@author: Darius
'''
import logic.Point as pt
from fractions import Fraction

class Bspline(object):
    '''
    classdocs
    '''


    def __init__(self, n, control_points, nodes):
        '''
        Constructor
        '''
        self.__n = n
        self.__control_points = control_points
        self.__nodes = nodes
        self.__N = len(nodes)-2*n
    
    def get_n(self):
        return self.__n
    def set_n(self, deg):
        self.__n = deg
    
    def get_control_points(self):
        return self.__control_points
    def set_control_points(self, control_points):
        self.__control_points = control_points
    
    def get_nodes(self):
        return self.__control_points
    def set_nodes(self, nodes):
        self.__nodes = nodes
        
    def deBoor(self, t) -> pt.Point:
        inter_points = []
        #t should be in the [nodes[n], nodes[n+N]] interval 
        r = 0
        for i in range(self.__n, self.__n + self.__N):
            if ((t >= self.__nodes[i]) and (t <= self.__nodes[i+1]) and (self.__nodes[i] != self.__nodes[i+1])):
                r = i
        print("r = {}".format(r))
                
        inter_points = self.__control_points[r-self.__n:r+1] #copies points 0 1 2 3
        for k in range(1, self.__n+1):
            print("k = {}".format(k))
            aux_list = []
            j = 0
            for i in range(r-self.__n+k, r+1):
                print("\ti = {}".format(i))
                j += 1
                alpha_i_k = Fraction((t-self.__nodes[i])/(self.__nodes[self.__n+1+i-k]-self.__nodes[i])).limit_denominator()
                print("\t\t alpha_{}_{} = {}".format(i,k,alpha_i_k))
                p1 = inter_points[j-1].scalar_multiply(1-alpha_i_k)
                p2 = inter_points[j].scalar_multiply(alpha_i_k)
                d_i_k = p1 + p2 
                print("\t\t d_{}_{} = {}".format(i,k,str(d_i_k)))
                aux_list.append(d_i_k)
            inter_points = aux_list[:]
            print(inter_points)
        return inter_points[0];
            
        
        
        
             
        
        