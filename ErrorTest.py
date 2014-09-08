__author__ = 'jean'
from validate_geom_formulae import *

#============================Circle_ErrorTest==============================================
def circle_try(n=0):
    try: # steps you think might produce an error
        s = float(input("Provide a circle radius:"))
    except ValueError as err: # how you want to handle that error
        print("You did not enter a number, try again. Error:", err)
        circle_try(n+1)
    else: # what to do if there was no error
        print("the area of circle is =: ", circle_area(s))
        print("The circumference of circle is = ", circle_circumference(s))
    finally: # what to always do, errors or not
        print("exiting attempt",n+1)

if __name__ == "__main__":
    circle_try()
#===========================Rectangle_ErrorTest=============================================
def rectangle_area_try(n=0):
    try:
        s = float(input("provide a rectangle width: "))
        t = float(input("provide a rectangle height: "))
    except ValueError as err:
        print("You did not enter a number,", err)
        rectangle_area_try(n+1)
    else:
        print("the area of rectangle is =", rectangle_area(s, t))
    finally: # what to always do, errors or not
        print("exiting attempt", n+1)

if __name__ == "__main__":
    rectangle_area_try()
#=============================================================================================


def triangle_area_try(n=0):
    try:
       s = float(input("provide a triangle side1:"))