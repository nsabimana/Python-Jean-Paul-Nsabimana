__author__ = 'jean'

import turtle
from numpy import *
import math
#===========================Circle=========================================================
class Circle(object):
    """a class representation of square"""
    circle_created = 0

    def __init__(self, radius_length: (int,float)):
        self.circle_created += 1
        self.radius_length = radius_length
        self.area = self.radius_length**2 * pi
        self.circumference = self.radius_length*4*pi

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

cir = Circle(100)
if __name__ == '__main__':
    circle = Circle(5)
    print(cir, cir.area, cir.circumference)
    cir.draw()
#==============================rectangle_shape======================================

class Rectangle(object):
    """a class representation of square"""
    rectangle_created = 0
    def __init__(self, base:(int,float), height: (int,float)):
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
           turtle.forward(200)
           turtle.left(90)
           turtle.forward(150)
           turtle.left(90)
           i = i+1
        turtle.done()

rec = Rectangle(200, 150)

if __name__ == '__main__':
    rec = Rectangle(200, 150)
    print(rec, rec.area, rec.perimeter)
    rec.draw()

#========================================Triangle============================


class Triangle(object):
    """a class representation of Triangle"""
    triangle_created = 0
    def __init__(self, side1_length: (int, float), side2_length: (int, float), side3_length: (int, float)):
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
        for i in range(0,2):
            turtle.forward(200)
            turtle.left(120)
            turtle.forward(200)
            turtle.left(120)
            i = i + 1
        turtle.done()

tr = Triangle(200, 200, 200)

if __name__ == '__main__':
#    tr = Triangle(200, 200, 200)
    print(tr, tr.area, tr.perimeter)
    tr.draw()


#=========================Parallelogram===============================================================

class Parallelogram(object):
    """a class representation of circles"""
    parallelogram_created = 0

    def __init__(self, base_length: (int, float), height_length: (int, float), leg_length: (int,float)):
        super(Parallelogram, self).__init__(base_length=base_length, height_length=height_length, leg_length=leg)
        self.parallelogram_created += 1
        self.base = base_length
        self.height = height_length
        self.leg = leg_length
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
        while i in range(0,2):
              turtle.forward(120)
              turtle.left(45)
              turtle.forward(80)
              turtle.left(135)
              i = i+1
        turtle.done()

if __name__ == '__main__':
    par = Parallelogram(120, 80, 60)
    print(par, par.area, par.perimeter)
    par.draw()

#=============================Trapezoid====================================================

class Trapezoid(object):
    """a class representation of trapezoid"""
    trapezoid_created = 0

    def __init__(self, lower_length: (int, float), leg_length: (int, float), upper_length: (int,float)):

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
        turtle.forward(250)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(60)
        turtle.forward(150)
        turtle.left(60)
        turtle.forward(100)
        turtle.done()

if __name__ == '__main__':
    trap = Trapezoid(250, 150, 100)
    print(trap, trap.area, trap.perimeter)
    trap.draw()


#=============Solid====================================================================