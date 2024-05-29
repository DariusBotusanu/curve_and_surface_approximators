'''
Created on Oct 25, 2021

@author: Darius
'''

from domain.Point import Point 
import interface.reading as rd


class UI(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def read_points(self, num):
        points = []
        print("Enter the control points: ")
        for i in range(num + 1):
            print("Point {}: x =".format(i), end=" ")
            x = rd.read_float()
            print("y =", end=" ")
            y = rd.read_float()
            p = Point(x, y)
            found = False
            for point in points:
                if point == p:
                    print("\nPlease enter different control points!")
                    i = i - 1
                    found = True
            if(found == False):
                points.append(p)
        return points
    
    def read_degree(self):
        print("Enter the degree:")
        num = rd.read_int()
        while(num < 1):
            print("The degree should not be smaller than 1!")
            num = rd.read_int()
        return num
    
        
