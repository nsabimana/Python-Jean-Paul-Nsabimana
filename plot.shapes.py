__author__ = 'jean'
from pylab import *
from numpy import *
from geom_formulae import *
import
#----------------------------------------triangle_plot-----------------
v_triangle_area = np.vectorize(triangle_area)
def triangle_plot_props(start, end):
    """
    Plot the area of a triangle as a function of side1, side2
    length, with side3 length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """

    S = np.linspace(0,10) # our side3 lengths
    B = 3
    C = 4
    A = v_triangle_area(S,B,C)  # the areas


    plot(S, A, '-r', label="Area")

    xlabel('side3, side1=3,side2=4 length')
    ylabel('geo values')
    title('triangle Geo Properties')
    legend(loc='upper right')

    show()
    pass

if __name__ == "__main__":
     triangle_plot_props(0, 10)

#-------------------------------circle_plot-----------------------------------
v_circle_area = np.vectorize(circle_area)
v_circle_circumference = np.vectorize(circle_circumference)
def circle_plot_props(start, end):
    v_circle_area = np.vectorize(circle_area)
    v_circle_circumference = np.vectorize(circle_circumference)

    S = np.linspace(0,10) # our side lengths

    A = v_circle_area(S)  # the areas
    P = v_circle_circumference(S)  # the perimeters

    plot(S, A, '-r', label="Area")
    plot(S, P, ':b', label="circumference")
    xlabel('radius length')
    ylabel('geo values')
    title('circle Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    circle_plot_props(0, 10)

#==============================sphere_plot===========================
v_sphere_area = np.vectorize(sphere_area)
v_sphere_volume = np.vectorize(sphere_volume)

def sphere_plot_props(start, end):
    """
    Plot the area and volume of a sphere as a function of radius
    length, with radius length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end) # our side lengths
    A = v_sphere_area(S)  # the areas
    P = v_sphere_volume(S)  # the volume
    plot(S, A, '-r', label="Area")
    plot(S, P, ':b', label="volume")
    xlabel('radius length')
    ylabel('geo values')
    title('sphere Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    sphere_plot_props(0, 10)

#==============================Cube================================

v_cube_area = np.vectorize(cube_area)
v_cube_volume = np.vectorize(cube_volume)

def cube_plot_props(start, end):
    """
    Plot the volume of cube  as a function of edge
    length, with edge length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end) # our edge lengths
    A = v_cube_area(S)  # the areas
    P = v_cube_volume(S,)  # the volume
    plot(S, A, '-r', label="area")
    plot(S, P, ':b', label="volume")
    xlabel('edge length')
    ylabel('geo values')
    title('cube Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    cube_plot_props(0, 10)

#===============================Ellipse===========================
from pylab import *

from geom_formulae import *


V_ellipse_area = np.vectorize(ellipse_area)
def ellipse_plot_props(start, end):
      S = np.linspace(start, end) # our semi_major axis lengths

      B = 2
      A = V_ellipse_area(S, B)# area
      plot(S, A, '-r', label="Area")
      xlabel('semi_major_axis, semi_minor_axis=4')
      ylabel('geo value')
      title('ellipse Geo properties')
      legend(loc='upper right')

      show()

if __name__ == "__main__":
    ellipse_plot_props(0, 10)

#===============================Cone========================================

v_cone_area = np.vectorize(cone_area)
v_cone_volume = np.vectorize(cone_volume)


def cone_plot_props(start, end):
    """
    Plot the area and volume of a cone as a function of radius
    length, with height length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end) # our height lengths
    B = 4
    A = v_cone_area(S, B)  # the areas
    P = v_cone_volume(S, B)  # the volume
    plot(S, A, '-r', label="Area")
    plot(S, P, ':b', label="volume")
    xlabel('height length')
    ylabel('geo values')
    title('The cone Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    cone_plot_props(0, 10)

#======================================Cylinder=================

v_cylinder_volume = np.vectorize(cylinder_volume)

def cylinder_plot_props(start, end):
    """
    Plot the volume of cylinder  as a function of height
    length, with radius length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end) # our height lengths
    C = 5
    A = v_cylinder_volume(S,C)  # the volume
    plot(S, A, '-r', label="volume")
    xlabel('radius length')
    ylabel('geo values')
    title('cylinder Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    cylinder_plot_props(0, 10)

#===========================parallelogram=================================

V_parallelogram_area = np.vectorize(parallelogram_area)
def parallelogram_plot_props(start, end):
    S = np.linspace(0,10)

    B = 3
    A = V_parallelogram_area(S, B)# area
    plot(S, A, '-r', label="Area")

    xlabel('height length, base=3')
    ylabel('geo value')
    title('parallelogram Geo properties')
    legend(loc='upper right')

    show()
if __name__ == "__main__":
    parallelogram_plot_props(0,10)

#=============================trapezoid_shape====================
from pylab import *

from geom_formulae import *

V_trapezoid_area = np.vectorize(trapezoid_area)
def trapezoid_plot_props(start, end):
    S = np.linspace(0,10)

    B = 3
    D = 6
    A = V_trapezoid_area(S, B, D)# area
    plot(S, A, '-r', label="Area")
    xlabel('height length, small_base=3, large_base=6')
    ylabel('geo value')
    title('trapezoid Geo properties')
    legend(loc='upper right')
    show()
    pass
if __name__ == "__main__":
    trapezoid_plot_props(0,10)

#=============================Rectangle_plot======================================
V_rectangle_area = np.vectorize(rectangle_area)
def rectangle_plot_props(start, end):
    S = np.linspace(0,10)
    B = 3
    A = V_rectangle_area(S, B)# area
    plot(S, A, '-r', label="Area")
    xlabel('width length')
    ylabel('geo value')
    title('rectangle Geo properties')
    legend(loc='upper right')

    show()
    pass

if __name__ == "__main__":
    rectangle_plot_props(0, 10)

#========================Ellipsoid_Shape===========================

from pylab import *

from geom_formulae import *

# make functions able to operate on vectors
v_ellipsoid_volume = np.vectorize(ellipsoid_volume)

def ellipsoid_plot_props(start, end):
    """
    Plot the volume of an ellipsoid as a function of radius1 and radius2
    length, with radius3 length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end) # our radius3 lengths
    B = 3
    C = 4
    A = v_ellipsoid_area(S,B,C) # volume
    plot(S, A, '-r', label="volume")
    xlabel('radius3, radius1=3,radius2=4 length')
    ylabel('geo values')
    title('ellipsoid Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    ellipsoid_plot_props(0, 10)