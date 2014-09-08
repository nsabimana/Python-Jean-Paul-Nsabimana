__author__ = 'jean'
from pylab import *

from geom_formulae import *

# make functions able to operate on vectors
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