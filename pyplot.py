__author__ = 'jean'

from pylab import *

from numbers import Num

def square_perimeter(side : Number) -> Number:
    """
    Calculate perimeter of a square from side length.

    @param side: the side length
    @return: the perimeter (same units as side length)

    >>> square_perimeter(4)
    16
    """
    return 4*side


def square_area(side):
    """
    Calculate area of a square from side length.
    @param side: the side length
    @return: the area (units^2 from side)
    >>> square_area(4)
    16
    """
    return side*side


v_square_area = np.vectorize(square_area)
v_square_perimeter = np.vectorize(square_perimeter)

S = np.linspace(0,10) # our side lengths

A = v_square_area(S)  # the areas
P = v_square_perimeter(S)  # the perimeters

plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()