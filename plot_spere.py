__author__ = 'jean'
from pylab import *

from geom_formulae import *

# make functions able to operate on vectors
v_sphere_area = np.vectorize(sphere_area)
v_sphere_volume = np.vectorize(sphere_volume)

def sphere_plot_props(start, end):
    """
    Plot the area and volume of a sphere as a function of radius
    length, with radius length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end) # our side lengths
    A = v_sphere_area(S)  # the areas
    P = v_sphere_volume(S)  # the volume
    plot(S, A, '-r', label="Area")
    plot(S, P, ':b', label="volume")
    xlabel('radius length')
    ylabel('geo values')
    title('sphere Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    sphere_plot_props(0, 10)