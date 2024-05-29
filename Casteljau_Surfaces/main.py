# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:13:12 2021

@author: Darius
"""
from fractions import Fraction
from logic.Casteljau_surfaces_iterated import iterated_Casteljau

# points_matrix = [[(2,3,1), (2,5,3), (2,9,1)],
#                   [(5,2,1), (5,6,4), (6,8,1)],
#                   [(6,2,0), (8,6,3), (8,8,1)]]

points_matrix = [[(0,0,0), (1,0,3), (2,4,3)],
                  [(2,2,1), (0,-2,1), (1,5,3)]]
pair = (Fraction(1/2),Fraction(1/3).limit_denominator());
n = len(points_matrix)-1
m = len(points_matrix[0])-1
r_u_v = iterated_Casteljau(n,m,points_matrix, pair)
print("r({},{}) = ({}, {}, {})".format(str(pair[0]), str(pair[1]),
                                       str(r_u_v[0]), str(r_u_v[1]), str(r_u_v[2])))


# import os
# from geomdl import BSpline
# from geomdl import utilities
# from geomdl.visualization import VisMPL


# # Fix file path
# os.chdir(os.path.dirname(os.path.realpath(__file__)))

# # Create a BSpline surface instance (Bezier surface)
# surf = BSpline.Surface()

# # Set up the Bezier surface
# surf.degree_u = 2
# surf.degree_v = 2
# control_points = points
# surf.set_ctrlpts(control_points, 3, 3)
# surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, surf.ctrlpts_size_u)
# surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, surf.ctrlpts_size_v)

# # Set sample size
# surf.sample_size = 25

# # Evaluate surface
# surf.evaluate()

# # Plot the control point grid and the evaluated surface
# vis_comp = VisMPL.VisSurface()
# surf.vis = vis_comp
# surf.render(filename="bezier_surface.pdf", plot=False)

pass