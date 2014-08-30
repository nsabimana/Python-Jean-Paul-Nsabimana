__author__ = 'jean'

# Area of a triangle with the sides of different length

from numpy import *


def triangle_area(side1: number, side2: number, side3: number) -> number:
    """

    :param side1: length of first side of a triangle
    :param side2: length of second side of the triangle
    :param side3: length of third side of the triangle
    :return: the area
     >>> triangle_area(3,4,5)
     6.0
    """
    s = (side1+side2+side3)/2
    area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area
triangle_area(3, 4, 5)
if __name__ == "__main__":
    side1 = 3
    side2 = 4
    side3 = 5
print("The area of triangle is =", triangle_area(side1, side2, side3), "sq. units")


#......Circle_circumference with radius r........
def circle_circumference(radius : number) ->number:
    """

    :param radius: the length of the radius
    :return:circumference
    >>> circle_circumference(5)
    31.4
    """
    circumference = 2*radius*pi
    return circumference
circle_circumference(5)

if __name__ == '__main__':
    radius = 5
    print(" The circumference of circle is =", circle_circumference(radius), "units of length")


#.....circle_area with radius r
def circle_area(radius : number) -> number:
    """
    Calculate the area of circle with radius r
    :param radius: radius of the circle
    :return:area of circle
    >>>circle_area(5)
    78.53
    """
    area = pi*radius*radius
    #print("The area of circle is =", area, "sq.units")
    return area
#circle_area(5)

if __name__ == '__main__':
    radius = 5
    print(" The area of circle is =", circle_circumference(radius), "sq. units")


# ....Rectangle_area with width  w and h height
def rectangle_area(width : number, height : number) ->number:
    """
    Calculate the area of rectangle with width w and height h
    :param width: the length of width
    :param height: the length of height
    :return: area of rectangle
    >>>rectangle_area(3,5)
    15
    """
    area = width*height
    #print("The area of rectangle is =", area, "sq. units")
    return area
#rectangle_area(3, 5)

if __name__ == '__main__':
    width = 3
    height = 5
    print(" The area of rectangle is =", rectangle_area(width, height), "sq. units")


#....trapezoid_area with large base b, small base a and vertical height
def trapezoid_area(small_base : number, large_base : number, height : number) ->number:
    """
    Calculate the area of trapezoid_area with large base , small base  and vertical height
    :param small_base: length of small base
    :param large_base: length of large base
    :param height: length of vertical height at a right angle to large base
    :return:area
    >>>trapezoid_area(4,6,3)
    15.0
    """
    area = (((small_base+large_base)/2)*height)
    return area
trapezoid_area(4, 6, 3)

if __name__ == "__main__":
    small_base = 4
    large_base = 6
    height = 3
    print("The area of trapezoid is =", trapezoid_area(small_base, large_base, height), "sq. units")


#....parallelogram_area with base b and height h at a right angle to b.

def parallelogram_area(base,height):
    """
    Calculate the are of parallelogram with base b and height h at a right angle to b.
    :param base: length of base
    :param height: length of height
    >>>parallelogram_area(6,4)
    24.0
    """
    area = base*height
    print("the area of parallelogram is =", area, "sq. units")
    return area
parallelogram_area(6, 4)


#......the ellipse_area
def ellipse_area(semi_major_axis: number, semi_minor_axis : number) -> number:
    """
    Calculate the ellipse_area  with semi-major axis  and semi-minor axis.
    :param semi_major_axis: length of semi-major axis
    :param semi_minor_axis:length of semi-minor axis
    >>>ellipse_area(4,3)
    37.69
    """
    area = pi*semi_major_axis*semi_minor_axis
    return area

if __name__ == '__main__':
    semi_major_axis = 4
    semi_minor_axis = 3
    print("The area of ellipse is = ", ellipse_area(semi_major_axis, semi_minor_axis), "sq. units")


#....sphere_area with radius r
def sphere_area(radius : number) -> number:
    """
    Calculate sphere_area with radius r
    :param radius: length of radius r
    >>>sphere_area(4)
    201.06
    """
    area = 4*pi*radius*radius
    print("The area of sphere is =", area, "sq. units")
    return area
sphere_area(4)


#...... sphere_volume with radius r
def sphere_volume(radius : number) -> number:
    """
    Calculate the volume of sphere with radius r
    :param radius: length of sphere radius
    >>>sphere_volume(4)
    268.08
    """
    volume = 4/3*(pi*radius*radius*radius)
    print("The volume of sphere is =", volume, "volume units")
    return volume
sphere_volume(4)


#....cube_area with edge a
def cube_area(edge : number) -> number:
    """
    Calculate the area of cube with edge a
    :param edge: the length of any edge of the cube
    >>>cube_area(2)
    24
    """
    area = 6*edge*edge
    print("The area of cube is =", area, 'Sq. units')
    return area
cube_area(2)


# ......cube_volume with the edge a
def cube_volume(edge : number) -> number:
    """
    Calculate the volume of cube with edge a
    :param edge: the length of any edge of the cube
    >>>cube_volume(2)
    8
    """
    volume = edge*edge*edge
    print("The volume of cube is =", volume, "Volume units")
    return volume
cube_volume(2)


# ...the volume of ellipsoid with three radii
def ellipsoid_volume(radius1: number, radius2: number, radius3: number) -> number:
    """
     calculate the volume of ellipsoid with three radius
    :param radius1: length of first radius
    :param radius2: length of second radius
    :param radius3: length of third radius
    >>>ellipsoid_volume(4, 3, 2)
    100.53
    """
    volume = 4/3*(pi*radius1*radius2*radius3)
    return volume
if __name__ == '__main__':
    radius1 = 4
    radius2 = 3
    radius3 = 2
    print("The volume of ellipsoid is =", ellipsoid_volume(radius1, radius2, radius3), " volume units")


#.... the volume of cylinder with base radius and height
def cylinder_volume(radius: number, height: number) -> number:
    """
    Calculate the volume of the cylinder with base radius and height
    :param radius: length of base radius
    :param height: length of height
    >>>cylinder_volume(7,12)
    1847.25
    """
    volume = pi*radius*radius*height
    return volume
if __name__ == '__main__':
    radius = 7
    height =12
    print("The volume of cylinder is =", cylinder_volume(radius,height), "volume units")


#....The Surface area of cone with radius and height
def cone_area(radius: number, height: number) -> number:
    """
    Calculate the surface area of cone with the radius and height
    :param radius: length of radius
    :param height: length of height
    >>>cone_area(2,4)
    40.66
    """
    length = sqrt(radius*radius+height*height)
    area = pi*radius*length+pi*radius*radius
    return area


def cone_volume(radius: number, height: number) -> number:
    """
    Calculate the volume of cone with the radius and height
    :param radius: length of cone radius
    :param height: length of cone radius
    >>>cone_volume(2,4)
    16.75
    """
    return 1/3*(pi*radius*radius*height)

if __name__ == '__main__':
    radius = 2
    height = 4
    print("The volume of cone is =",
          cone_volume(radius,height), "volume units")
    print("The area of cone is =",
          cone_area(radius,height), " square units")
