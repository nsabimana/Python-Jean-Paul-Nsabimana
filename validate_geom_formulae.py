__author__ = 'jean'
from dimension_validate1 import *
from numpy import *


#=============================Rectangle========================================


def rectangle_area(width = None, height = None):
    """
    Calculate the area of rectangle with width w and height h
    :param width: the length of width
    :param height: the length of height
    :return: area of rectangle
    >>> rectangle_area(3,5)
    15

    """
    if height is None or width is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(width, Number):
        raise TypeError('You entered a string! Please change it to a number')
    if not isinstance(height, Number):
        raise TypeError('You entered a string! Please change it to a number')
    elif dim_validate(height) and dim_validate(width):
        return width*height


    else:
        raise ("Please Check your values : " +str(width) + "," +str(height) + ". Enter a positive value")

if __name__ == '__main__':
    width = 3
    height = 5
    print("The area of rectangle is = ", rectangle_area(width, height), "sq. units")

#===============================Circle============================================

def circle_area(radius):
    """
    Calculate the area of circle with radius r
    :param radius: radius of the circle5
    :return:area of circle
    >>> circle_area(5)
    78.53981633974483

    """
    if radius is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif radius is None :
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(radius, Number):
        raise TypeError("You entered a string! please change it to a number")
    elif dim_validate(radius):
        return pi*radius*radius
    else:
        raise ValueError("please check your value :" +str(radius)  + ". Enter a positive value")
if __name__ == '__main__':
    radius = 4
    print("The area of circle is = ", circle_area(radius), "sq. units")



def circle_circumference(radius):
    """
    Calculate the circumference of circle with radius r
    :param radius: the length of the radius
    :return:circumference
    >>> circle_circumference(5)
    31.41592653589793

    """
    if radius is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(radius, Number):
        raise TypeError("you entered a string! please change it to a number")
    elif dim_validate(radius):
        return 2*pi*radius
    else:
        raise ValueError("please check your value :" +str(radius) + " . Enter a positive value")
if __name__ == '__main__':
    radius = 4
    print("The circumference of circle is = ", circle_circumference(radius), "sq. units")


#=====================================Triangle=====================

side1 = 3
side2 = 4
side3 = 5

def triangle_area(side1, side2, side3):
    """
     Calculate the area of triangle with side1, side2 and side3 length.
    :param side1: length of first side of a triangle
    :param side2: length of second side of the triangle
    :param side3: length of third side of the triangle
    :return: the area
     >>> triangle_area(3,4,5)
     6.0

    """
    if side1 is None or side2 is None or side3 is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(side1, Number):
        raise TypeError("you entered a string! please change it to a number")
    if not isinstance(side2, Number):
        raise TypeError("you entered a string! please change it to a number")
    if not isinstance(side3, Number):
        raise TypeError("you entered a string! please change it to a number")
    elif dim_validate(side1) and dim_validate(side2) and dim_validate(side3):
         s = (side1+side2+side3)/2
         area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
         return sqrt(s*(s-side1)*(s-side2)*(s-side3))
    else:
        raise ValueError("Please Check your values : " +str(side1) +", " +str(side2) +","  +str(side3) + "," ". Enter a positive value")
print(triangle_area(side1,side2,side3))

#========================================Parallelogram=====================================

base = 6
height = 4
def parallelogram_area(base, height):
    """
    Calculate the are of parallelogram with base b and height h at a right angle to b.
    :param base: length of base
    :param height: length of height
    >>> parallelogram_area(6,4)
    24

    """
    if base is None or height is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(base, Number):
        raise TypeError('You entered a string! Please change it to a number')
    if not isinstance(height, Number):
        raise TypeError('You entered a string! Please change it to a number')
    elif dim_validate(base) and dim_validate(height):
        return base*height
    else:
        raise ValueError("Please Check your values : " +str(base) + "," +str(height) + ". Enter a positive value")

print(parallelogram_area(base,height))

#=========================Trapezoid==================================================


def trapezoid_area(upper , lower, leg):
    """
    Calculate the area of trapezoid_area with large base , small base  and vertical height
    :param upper: length of upper base
    :param lower: length of lower base
    :param leg: length of vertical height at a right angle to large base
    :return:area
    >>> trapezoid_area(4,6,3)
    15.0

    """
    if upper is None or lower is None or leg is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(upper, Number):
        raise TypeError("you entered a string! please change it to a number")
    if not isinstance(lower, Number):
        raise TypeError("you entered a string! please change it to a number")
    if not isinstance(leg, Number):
        raise TypeError("you entered a string! please change it to a number")
    elif dim_validate(upper) and dim_validate(lower) and dim_validate(leg):
         return ((upper+lower)/2)*leg
    else:
        raise ValueError("Please Check your values : " +str(upper) +", " +str(lower) +","  +str(leg) + "," ". Enter a positive value")

if __name__ == "__main__":
    upper = 4
    lower = 6
    leg = 3
    print("The area of trapezoid is =", trapezoid_area(upper, lower, leg))

#=-======================================Ellipse===========================


def ellipse_area(semi_major_axis, semi_minor_axis):
    """
    Calculate the ellipse_area  with semi-major axis  and semi-minor axis.
    :param semi_major_axis: length of semi-major axis
    :param semi_minor_axis:length of semi-minor axis
    >>> ellipse_area(4,3)
    37.69911184307752

    """
    if semi_major_axis is None or semi_minor_axis is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(semi_major_axis, Number):
        raise TypeError('You entered a string! Please change it to a number')
    if not isinstance(semi_minor_axis, Number):
        raise TypeError('You entered a string! Please change it to a number')
    elif dim_validate(semi_major_axis) and dim_validate(semi_minor_axis):
        return pi*semi_major_axis*semi_minor_axis
    else:
        raise ValueError("Please Check your values : " +str(semi_major_axis) + "," +str(semi_minor_axis) + ". Enter a positive value")

if __name__ == '__main__':
    semi_major_axis = 4
    semi_minor_axis = 3
    print("The area of ellipse is = ", ellipse_area(semi_major_axis, semi_minor_axis), "sq. units")

#========================================Sphere======================================

def sphere_area(radius):
    """
    Calculate sphere_area with radius r
    :param radius: length of radius r
    >>> sphere_area(4)
    201.06192982974676

    """
    if radius is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(radius, Number):
        raise TypeError("you entered a string! please change it to a number")
    elif dim_validate(radius):
        return 4*pi*radius*radius
    else:
        raise ValueError("please check your value :" +str(radius) + " . Enter a positive value")
if __name__ == '__main__':
    radius = 4
    print("The area of sphere is = ", sphere_area(radius), "sq. units")

def sphere_volume(radius):
    """
    Calculate the volume of sphere with radius r
    :param radius: length of sphere radius
    >>> sphere_volume(4)
    268.082573106329

    """
    if radius is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(radius, Number):
        raise TypeError("you entered a string! please change it to a number")
    elif dim_validate(radius):
        return 4/3*(pi*radius*radius*radius)
    else:
        raise ValueError("please check your number : " +str(radius) + " . Enter a positive value")
if __name__ == '__main__':
    radius = 4
    print("the volume of sphere is = ", sphere_volume(radius), "volume units")

#============================cube===========================
def cube_area(edge):
    """
    Calculate the area of cube with edge a
    :param edge: the length of any edge of the cube
    >>> cube_area(2)
    24

    """
    if radius is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(edge, Number):
        raise TypeError("you entered a string! please change it to a number")
    elif dim_validate(edge):
        return 6*edge*edge
    else:
        raise ValueError("please check your value :" +str(edge) + " . Enter a positive value")
if __name__ == '__main__':
    edge = 2
    print("The area of cube is = ", cube_area(edge), "sq. units")


def cube_volume(edge):
    """
    Calculate the volume of cube with edge a
    :param edge: the length of any edge of the cube
    >>> cube_volume(2)
    8
    """
    if edge is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(edge, Number):
        raise TypeError("you entered a string! please change it to a number")
    elif dim_validate(edge):
        return edge*edge*edge
    else:
        raise ValueError("please check your value :" +str(edge) + " . Enter a positive value")
if __name__ == '__main__':
    edge = 2
    print("The volume of cube is = ", cube_volume(edge), "sq. units")

#========================================Ellipsoid==============================


def ellipsoid_volume(radius1, radius2, radius3):
    """
     calculate the volume of ellipsoid with three radius
    :param radius1: length of first radius
    :param radius2: length of second radius
    :param radius3: length of third radius
    >>> ellipsoid_volume(4, 3, 2)
    100.53096491487338

    """
    if radius1 is None or radius2 is None or radius3 is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(radius1, Number):
        raise TypeError("you entered a string! please change it to a number")
    if not isinstance(radius2, Number):
        raise TypeError("you entered a string! please change it to a number")
    if not isinstance(radius3, Number):
        raise TypeError("you entered a string! please change it to a number")
    elif dim_validate(radius1) and dim_validate(radius2) and dim_validate(radius3):
         return 4/3*(pi*radius1*radius2*radius3)
    else:
        raise ValueError("Please Check your values : " +str(radius1) +", " +str(radius2) +","  +str(radius3) + "," ". Enter a positive value")

if __name__ == '__main__':
    radius1 = 4
    radius2 = 3
    radius3 = 2
    print("The volume of ellipsoid is =", ellipsoid_volume(radius1, radius2, radius3), " volume units")

#====================================Cylinder===================================
def cylinder_volume(radius, height):
    """
    Calculate the volume of the cylinder with base radius and height
    :param radius: length of base radius
    :param height: length of height
    >>> cylinder_volume(7,12)
    1847.2564803107982

    """
    if radius is None or height is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(radius, Number):
        raise TypeError('You entered a string! Please change it to a number')
    if not isinstance(height, Number):
        raise TypeError('You entered a string! Please change it to a number')
    elif dim_validate(radius) and dim_validate(height):
        return pi*radius*radius*height
    else:
        raise ValueError("Please Check your values : " +str(radius) + "," +str(height) + ". Enter a positive value")
if __name__ == '__main__':
    radius = 7
    height =12
    print("The volume of cylinder is =", cylinder_volume(radius,height), "volume units")

#==========================cone==========================================================


def cone_volume(radius, height):
    """
    Calculate the volume of cone with the radius and height
    :param radius: length of cone radius
    :param height: length of cone radius
    >>> cone_volume(2,4)
    16.755160819145562

    """
    if radius is None or height is None:
        raise AttributeError("arguments are invalid!! please additional argument is needed")
    elif not isinstance(radius, Number):
        raise TypeError('You entered a string! Please change it to a number')
    if not isinstance(height, Number):
        raise TypeError('You entered a string! Please change it to a number')
    elif dim_validate(radius) and dim_validate(height):
        return pi*radius*radius*height
    else:
        raise ValueError("Please Check your values : " +str(radius) + "," +str(height) + ". Enter a positive value")
if __name__ == '__main__':
    radius = 2
    height = 4
    print("The volume of cone is =",
          cone_volume(radius, height), "volume units")
#=============================================Cube_Solid====================================================

