'''
Created on Nov 12, 2021

@author: Darius
'''
import ui.reading as rd
import logic.Point as pt
import logic.Bspline as bs
if __name__ == '__main__':
    
    points = rd.read_control_points(3)
    #nodes = rd.read_nodes(7)
    nodes = [2, 4, 6, 8, 10, 12]
    deg = len(nodes)-len(points)-1
    print(deg)
    curve = bs.Bspline(deg, points, nodes)
    #t = rd.read_t(nodes)
    t = 7
    result = curve.deBoor(t)
    print("r({}) = {}".format(t, result))