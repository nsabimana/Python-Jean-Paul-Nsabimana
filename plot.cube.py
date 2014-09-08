__author__ = 'jean'
from pylab import *

from geom_formulae import *

# make functions able to operate on vectors
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