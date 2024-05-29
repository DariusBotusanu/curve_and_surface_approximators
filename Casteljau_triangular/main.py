# -*- coding: utf-8 -*-

import ui.reading as rd
import logic.bezier_triangular as bez
from fractions import Fraction

test_points_1 = [(2,3,1), (2,5,3), (2,9,1), (5,2,1), (5,6,4), (6,8,1)]
n = 2
print("The test points: ")
print(rd.print_points(test_points_1))

test_point_1 = (Fraction(1/3).limit_denominator(),Fraction(1/3).limit_denominator(),Fraction(1/3).limit_denominator())
result = bez.find_point(n, test_points_1, test_point_1)
print("First test: r{} = ({}, {}, {})".format(test_point_1, str(result[0]),str(result[1]),str(result[2])))

# test_point_2 = (1/2,1/6,1/3)
# print("First test: r{} = {}".format(test_point_1, bez.find_point(3, test_points_1, test_point_2)))
# print('')

# print("Enter the degree: ")
# degree = rd.read_degree();

# print("Enter the points")
# points = rd.read_control_points(degree)

# print("You have entered the points: ")
# print(rd.print_points(points))

# print("Enter the barycentric coordinates of the point you wish to find: ")
# point = rd.read_coordinates()

# print("These are the cartesian coordiantes of the point you entered: {}".format(bez.find_point(degree, points, point)))

