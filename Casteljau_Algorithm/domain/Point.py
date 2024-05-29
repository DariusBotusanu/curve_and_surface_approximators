'''
Created on Oct 25, 2021

@author: Darius
'''
from pickle import TRUE


class Point(object):
    '''
    classdocs
    '''

    def __init__(self, x, y, z):
        '''
        Constructor
        '''
        self.__x = x
        self.__y = y
        self.__z = z
    
    
    
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
    
    def get_y(self):
        return self.__y
    def set_y(self, y):
        self.__y = y
    
    def get_z(self):
        return self.__z
    def set_z(self, z):
        self.__z = z
        
    def __repr__(self):
        return "("+str(self.__x)+", "+str(self.__y)+", "+str(self.__z)+")"
    
    def __eq__(self, other):
        if((self.__x == other.__x) and (self.__y == other.__y) and (self.__z == other.__z)):
            return True
        else:
            return False
    
    def multiply(self, num):
        self.__x = self.__x * num
        self.__y = self.__y * num
        self.__z = self.__z * num
