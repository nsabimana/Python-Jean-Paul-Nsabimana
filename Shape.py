__author__ = 'jean'

import turtle
from numpy import *
from math import *

#=============================Shapes_object==============================================
def dim_checker(**kwargs):
    errmsg = "All given arguments must be positive numbers; provided :"\
             + \
             str({k: v for k, v in kwargs.items() if v is not None})
    for name, arg in kwargs.items():
        if arg is None:
            pass # ignore nones, only checking provided arguments here
        elif not isinstance(arg, (int, float)):
            raise TypeError(errmsg)
        elif not arg >= 0:
            raise ValueError(errmsg)

class Shape(object):
    shapes_created = 0
    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.shapes_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
               "; area : "+str(self.area)+\
               "; perimeter: "+str(self.perimeter)

class Solid(object):
    solids_created = 0
    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.solids_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
               "; area : "+str(self.area)+\
               "; volume: "+str(self.volume)
#=========================================Circle Shape===========================


class Circle(Shape):
    """a class representation of square"""
    circle_created = 0

    def __init__(self, radius_length: (int,float)):
        super(Circle, self).__init__(radius_length=radius_length)
        self.circle_created += 1
        self.radius_length = radius_length
        self.area = self.radius_length**2 * pi
        self.perimeter = self.radius_length*pi*2

    def __str__(self):
        return super(Circle, self).__str__()+\
               ";radius length:"+str(self.radius_length)


    def __cmp__(self, other):
        if not isinstance(other, circle):
            raise TypeError("you entered a string!! please enter a number")
        else:
            return self.radius_length - other.radius_length

    def draw(self):
        turtle.circle(100)
        turtle.done()


if __name__ == '__main__':
    cir = Circle(5)
    print(cir)
    cir.draw()



#=========================================Rectangle_Shape=========================================


class Rectangle(Shape):
    """a class representation of square"""
    rectangle_created = 0
    def __init__(self, base:(int, float), height: (int, float)):
        super(Rectangle, self).__init__(base=base, height=height)
        self.rectangle_created += 1
        self.base = base
        self.height = height
        self.area = self.base*self.height
        self.perimeter = (self.base + self.height)*2

    def __str__(self):
        return super(Rectangle, self).__str__()+\
        ":rectangle, base: "+str(self.base)+", height:"+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        else:
            return self.height, self.base - other.height, other.base

    def draw(self):
        for i in range(0,2):
           turtle.forward(self.base)
           turtle.left(90)
           turtle.forward(self.height)
           turtle.left(90)
           i = i+1
        turtle.done()
if __name__ == "__main__":
    rec = Rectangle(200, 150)
    print(rec)
    rec.draw()



#=====================Triangle_Shape=================================================


class Triangle(Shape):
    """a class representation of Triangle"""
    triangle_created = 0
    def __init__(self, side1_length: (int, float), side2_length: (int, float), side3_length: (int, float)):
        super(Triangle, self).__init__(side1_length=side1_length, side2_length=side2_length, side3_length=side3_length)
        self.triangle_created += 1
        self.side1 = side1_length
        self.side2 = side2_length
        self.side3 = side3_length
        s = (self.side1 + self.side2 + self.side3)/2
        self.area = sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
        self.perimeter = (self.side1 + self.side2 + self.side3)

    def __str__(self):
        return super(Triangle, self).__str__()+\
        ";triangle, side1: "+str(self.side1)+", side2:"+str(self.side2)+",side3:"+str(self.side3)
    def __cmp__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError
        else:
            return self.side1, self.side2, self.side3 - other.side1, other.side2, other.side3


    def draw(self):

        turtle.forward(self.side1)
        turtle.left(120)
        turtle.forward(self.side2)
        turtle.left(120)
        turtle.forward(self.side3)
        turtle.left(120)
        turtle.done()

if __name__ == "__main__":
    tri = Triangle(200, 200, 200)
    print(tri)
    tri.draw()


#====================Parallelogram_Shape=========================================


class Parallelogram(Shape):
    """a class representation of circles"""
    parallelogram_created = 0

    def __init__(self, base_length: (int, float), leg_length: (int, float), height_length: (int,float)):
        super(Parallelogram, self).__init__(base_length=base_length, leg_length=leg_length, height_length=height_length)
        self.parallelogram_created += 1
        self.base = base_length
        self.leg = leg_length
        self.height = height_length
        self.area = self.base*self.height
        self.perimeter = self.base*2+self.leg*2

    def __str__(self):
        return super(Parallelogram, self).__str__()+\
        ";parallelogram, base: "+str(self.base)+", height:"+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Parallelogram):
            raise TypeError
        else:
            return self.base - other.base, self.height - other.height, self.leg - other.leg

    def draw(self):
        i = 0
        for i in range(0,2):
              turtle.forward(self.base)
              turtle.left(45)
              turtle.forward(self.leg)
              turtle.left(135)
              i = i+1
        turtle.done()

if __name__ == "__main__":
    par = Parallelogram(200, 150, 60)
    print(par)
    par.draw()


#====================================Trapezoid_Shape======================================


class Trapezoid(Shape):
    """a class representation of trapezoid"""
    trapezoid_created = 0

    def __init__(self, lower_length: (int, float), leg_length: (int, float), upper_length: (int,float)):
        super(Trapezoid, self).__init__(lower_length=lower_length, leg_length=leg_length, upper_length=upper_length)
        self.trapezoid_created += 1
        self.lower = lower_length
        self.upper = leg_length
        self.leg = upper_length
        self.area = (self.lower + self.upper)/2 * self.leg
        self.perimeter = self.lower + self.upper + self.leg*2


    def __str__(self):
        return super(Trapezoid, self).__str__()+\
        ":trapezoid, lower: "+str(self.lower)+", leg:"+str(self.leg)+", upper: "+str(self.upper)

    def __cmp__(self, other):
        if not isinstance(other, Trapezoid):
            raise TypeError
        else:
            return self.lower - other.lower, self.leg - other.leg, self.upper - other.upper

    def draw(self):
        turtle.forward(self.lower)
        turtle.left(120)
        turtle.forward(self.leg)
        turtle.left(60)
        turtle.forward(self.upper)
        turtle.left(60)
        turtle.forward(self.leg)
        turtle.done()


if __name__ == "__main__":
    tra = Trapezoid(250, 150, 100)
    print(tra)
    tra.draw()

#========================Sphere_Solid======================================================


class Sphere(Solid):
    """a class representation of square"""
    sphere_created = 0

    def __init__(self, radius_length: (int,float)):
        super(Sphere, self).__init__(radius_length=radius_length)
        self.sphere_created += 1
        self.radius_length = radius_length
        self.area = 4*(self.radius_length**2 * pi)
        self.volume = 4/3*(self.radius_length**3*pi)

    def __str__(self):
        return super(Sphere, self).__str__()+\
               ";radius length:"+str(self.radius_length)


    def __cmp__(self, other):
        if not isinstance(other, Sphere):
            raise TypeError("you entered a string!! please enter a number")
        else:
            return self.radius_length - other.radius_length
if __name__ == '__main__':
    sph = Sphere(5)
    print(sph)

#=================================Cube_solid===============================


class Cube(Solid):
    """a class representation of square"""
    cube_created = 0

    def __init__(self, edge_length: (int,float)):
        super(Cube, self).__init__(edge_length=edge_length)
        self.cube_created += 1
        self.edge_length = edge_length
        self.area = 6*self.edge_length**2
        self.volume = self.edge_length**3

    def __str__(self):
        return super(Cube, self).__str__()+\
               ";edge length:"+str(self.edge_length)


    def __cmp__(self, other):
        if not isinstance(other, Sphere):
            raise TypeError("you entered a string!! please enter a number")
        else:
            return self.edge_length - other.edge_length
if __name__ == '__main__':
    cu = Cube(5)
    print(cu)

#============================Cylinder_Solid==================================


class Cylinder(Solid):
    """a class representation of circles"""
    cylinder_created = 0

    def __init__(self, radius_length: (int, float), height_length: (int,float)):
        super(Cylinder, self).__init__(radius_length=radius_length, height_length=height_length)
        self.cylinder_created += 1
        self.radius = radius_length
        self.height = height_length
        self.area = 2*pi*self.radius*(self.radius+self.height)
        self.volume = pi*self.radius**2*self.height

    def __str__(self):
        return super(Cylinder, self).__str__()+\
        ";cylinder, radius: "+str(self.radius)+", height:"+str(self.height)

if __name__ == "__main__":
    cyl = Cylinder(7, 12)
    print(cyl)

#=======================Cone_Solid==================================================


class Cone(Solid):
    """a class representation of circles"""
    cone_created = 0

    def __init__(self, radius_length: (int, float), height_length: (int,float)):
        super(Cone, self).__init__(radius_length=radius_length, height_length=height_length)
        self.cone_created += 1
        self.radius = radius_length
        self.height = height_length
        self.area = pi*self.radius*(self.radius + sqrt(self.radius**2 + self.height**2))
        self.volume = 1/3*(pi*self.radius**2*self.height)

    def __str__(self):
        return super(Cone, self).__str__()+\
        ";cone, radius: "+str(self.radius)+", height:"+str(self.height)

if __name__ == "__main__":
    co = Cone(7, 12)
    print(co)

#================================================================================================

