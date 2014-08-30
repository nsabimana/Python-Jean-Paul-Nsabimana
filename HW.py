__author__ = 'jean'
print("HELLO WORLD")
print("AIMS GHANA")
print("Hello Ghana")
print("Good program")
print("even more changes2")

# Area of a triangle
from numpy import *
def triangle (a,b,c):
    s=(a+b+c)/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is:",area,"sq. unit")
triangle(3,4,5)
# divide two numbers
def divide(a,b):
    c= a/b
    print (c)
divide(100,5)

#......Circle with radius r
def circle(r):
    circumference =2*r*pi
    print("circumference=", circumference,"leng. units")
    return circumference
    area = pi*r*r
    print("area=",area,"sq.units")
    return area
circle(5)


# ....Square
def square(side):
    perimeter=4*side
    print("perimeter =",perimeter,"leng. units")
    area=side*side
    print("area =",area,"sq. units")
square(5)    