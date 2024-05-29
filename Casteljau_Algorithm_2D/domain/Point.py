'''
Created on Oct 25, 2021

@author: Darius
'''
from pickle import TRUE


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
        return "("+str(self.__x)+", "+str(self.__y)+")"
    
    def __eq__(self, other):
        if((self.__x == other.__x) and (self.__y == other.__y)):
            return True
        else:
            return False
    
    def multiply(self, num):
        self.__x = self.__x * num
        self.__y = self.__y * num
