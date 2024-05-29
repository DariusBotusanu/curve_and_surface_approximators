from fractions import Fraction
import logic.iterated_Casteljau as ic
import ui.reading as rd


n = 3

# print("Enter the {} control points ".format(n))
# points = rd.read_points(n)
points = [(1,1,0), (2,1,0), (2,1,1)]
# print("Enter the vector: ")
# v = rd.read_vector()
v = (1/3,1/6,1/2)

# print("Enter delta = ", end = "")
# delta = rd.read_delta()
# print("\n")
delta = 3
                            

# print("Enter the pair = ")
# pair = rd.read_pair()
pair = (1/3,1/3)

r_v = ic.iterated_Casteljau(points, delta, v, pair)

print("r({},{}) = ({}, {}, {})".format(str(Fraction(pair[0]).limit_denominator()), 
                                       str(Fraction(pair[0]).limit_denominator()), 
                                       str(r_v[0]), str(r_v[1]), str(r_v[2])))

#we prepare the points for plotting
control_points_matrix = ic.get_extrudated_points_matrix(points, delta, v)
control_points = []
for i in range(len(control_points_matrix)):
    for j in range(len(control_points_matrix[0])):
        control_points.append([control_points_matrix[i][j][0],
                                control_points_matrix[i][j][1],
                                control_points_matrix[i][j][2]])
                              
import os
from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance (Bezier surface)
surf = BSpline.Surface()

# Set up the Bezier surface
surf.degree_u = 3
surf.degree_v = 1
surf.set_ctrlpts(control_points, 4, 2)
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, surf.ctrlpts_size_u)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, surf.ctrlpts_size_v)

# Set sample size
surf.sample_size = 25

# Evaluate surface
surf.evaluate()

# Plot the control point grid and the evaluated surface
vis_comp = VisMPL.VisSurface()
surf.vis = vis_comp
surf.render(filename="bezier_surface.pdf", plot=True)