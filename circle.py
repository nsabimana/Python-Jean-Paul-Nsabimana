__author__ = 'jean'


def circle_area(radius):
    """
    Calculate the area of circle with radius r
    :param radius: radius of the circle
    :return:area of circle
    >>> circle_area(5)
    78.53981633974483

    """
    if (dim_validate(radius)):
        return pi*radius*radius
    else:
        raise ValueError("radius is less than 0: "+str(radius))

    def dim_type(dim):

#=============================Rectangle===========================================

def dim_validate(width, height):
    """
    Test if width or height are number and >= o.
    :param width: length of width
    :param height: length of height
    :return: area

    >>> dim_validate(3, 5)
    True
    >>>dim_validate(3, -5)
    False
    >>> dim_validate(-3, 5)
    False
    >>> dim_validate(-3, -5)
    false
    >>> dim_validate("a string")
    False
    """
