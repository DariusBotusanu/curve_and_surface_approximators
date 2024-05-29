'''
Created on Oct 25, 2021

@author: Darius
'''

from interface.ui import UI
from interface.reading import read_float
from domain.BezierCurve import BezierCurve
from domain.Point import Point

if __name__ == '__main__':
    ui = UI()
    deg = ui.read_degree()
    points = ui.read_points(deg) 
    curve = BezierCurve(deg, points)
    print("Enter t: ")
    t = read_float()
    while((t < 0) or (t>1)):
        print("t should be in the interval [0, 1]!\n t=", end = " ")
        t = read_float()
    print("r({}) = {}".format(t, curve.find_point(t)))
    print("r'({}) = {}".format(t, curve.derivative_at_point(t)))
    