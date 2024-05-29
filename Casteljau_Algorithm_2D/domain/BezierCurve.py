'''
Created on Oct 25, 2021

@author: Darius
'''

import domain.Point as pt
from fractions import Fraction

class BezierCurve(object):
    '''
    classdocs
    '''


    def __init__(self, degree, control_points = []):
        '''
        Constructor
        '''
        self.__deg = degree
        self.__control_points = control_points
    
    
    def get_deg(self):
        return self.__deg
    def set_deg(self, deg):
        self.__deg = deg
        
    def get_control_points(self):
        return self.__control_points
    def set_control_points(self, points):
        self.__constrol_points = points
    
    def find_point(self, t):
        if (t == 0):
            return self.__control_points[0]
        if (t == 1):
            return self.__control_points[-1]
        
        iterable_points = self.__control_points[:]
        aux_list = []
        num = self.__deg
        
        for r in range(1,self.__deg+1):
            print("r = {}".format(r))
            for i in range(0, self.__deg+1-r):
                p = pt.Point(Fraction(iterable_points[i].get_x()*(1-t) + t*iterable_points[i+1].get_x()).limit_denominator(),
                             Fraction(iterable_points[i].get_y()*(1-t) + t*iterable_points[i+1].get_y()).limit_denominator(),)
                aux_list.append(p)
                print("\ti = {}".format(i))
                print("\t{}".format(str(p)))
            iterable_points = aux_list[:]
            print(iterable_points)
            aux_list.clear()
        return iterable_points[0]
    
    def derivative_at_point(self, t):
        if (t == 0):
            return self.__control_points[0]
        if (t == 1):
            return self.__control_points[-1]
        
        iterable_points = self.__control_points[:]
        aux_list = []
        num = self.__deg
        
        if (num == 1):
            p = pt.Point(iterable_points[0].get_x()*(1-t) + t*iterable_points[1].get_x().limit_denominator(),
                         iterable_points[0].get_y()*(1-t) + t*iterable_points[1].get_y().limit_denominator())
            return p
            
        for r in range(1,self.__deg):
            for i in range(0, self.__deg+1-r):
                p = pt.Point(iterable_points[i].get_x()*(1-t) + t*iterable_points[i+1].get_x().limit_denominator(),
                             iterable_points[i].get_y()*(1-t) + t*iterable_points[i+1].get_y().limit_denominator())
                aux_list.append(p)
            iterable_points = aux_list[:]
            aux_list.clear()
        p = pt.Point(self.__deg*(iterable_points[1].get_x()-iterable_points[0].get_x()),
                     self.__deg*(iterable_points[1].get_y()-iterable_points[0].get_y()))
        return p
            
            
        
        