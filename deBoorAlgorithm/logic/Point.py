'''
Created on Nov 12, 2021

@author: Darius
'''
from fractions import Fraction

class Point(object):
    '''
    classdocs
    '''


    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.__x = x
        self.__y = y
    
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
        
    def get_y(self):
        return self.__y
    def set_y(self, y):
        self.__y = y
        
    def __repr__(self):
        return "(" + str(self.__x) +", " + str(self.__y) + ")"
    
    def __eq__(self, other):
        if ((self.__x == other.__x) and (self.__y == other.__y)):
            return True
        else:
            return False
    
    def __add__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__y
        return Point(x,y)
    
    def __radd__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__y
        return Point(x,y)
    
    def copy(self):
        copy = Point(self.__x, self.__y)
        return copy
    
    def __str__(self):
        return "(" + str(Fraction(self.__x).limit_denominator()) +", "+ str(Fraction(self.__y).limit_denominator()) +")"
        
    
    def scalar_multiply(self, sc):
        return Point(self.__x*sc, self.__y*sc)