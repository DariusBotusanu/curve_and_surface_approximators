import logic.deCasteljauRational as dc
from fractions import Fraction

# points = rd.read_points(4)
# weights = rd.read_weights(4)
# print("Enter t = ", end = '')
# t = rd.read_float()
# while(t < 0 or t > 1):
#     print("t should be between [0,1]!")
#     print("Enter t = ", end = '')
#     t = rd.read_float()
    
# print(dc.rational_casteljau_2d(points, weights, t))
points = [(-3,1), (-2,5), (3,4), (4,-2)]
weights = [1,3,2,1]
t = 1/2
n = len(points)-1
r_t = dc.rational_casteljau_2d(n,points, weights, t)
print("r({}) = ({}, {})".format(Fraction(t), Fraction(r_t[0]).limit_denominator(), Fraction(r_t[1]).limit_denominator()))

# homogenous_pts = dc.homogenous_points(points, weights)

# import os
# from geomdl import NURBS
# from geomdl import utilities
# from geomdl.visualization import VisMPL

# # Fix file path
# os.chdir(os.path.dirname(os.path.realpath(__file__)))

# # Create a 3D B-Spline curve instance (Bezier Curve)
# curve = NURBS.Curve()

# # Set up the Bezier curve
# curve.degree = 3
# curve.ctrlptsw = homogenous_pts

# # Auto-generate knot vector
# curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlptsw))

# # Set evaluation delta
# curve.sample_size = 40

# # Evaluate curve
# curve.evaluate()

# # Draw the control point polygon and the evaluated curve
# vis_comp = VisMPL.VisCurve2D()
# curve.vis = vis_comp

# # Don't pop up the plot window, instead save it as a PDF file
# curve.render(filename="bezier_cubic.pdf", plot=False)

pass