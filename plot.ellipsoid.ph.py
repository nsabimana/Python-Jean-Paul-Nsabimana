__author__ = 'jean'
from pylab import *

from geom_formulae import *

# make functions able to operate on vectors
v_ellipsoid_volume = np.vectorize(ellipsoid_volume)

def ellipsoid_plot_props(start, end):
    """
    Plot the volume of an ellipsoid as a function of radius1 and radius2
    length, with radius3 length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end) # our radius3 lengths
    A = v_ellipsoid_volume(S)  # the volume
    B = 3
    C = 4
    plot(S, A, '-r', label="volume")
    xlabel('radius3, radius1=3,radius2=4 length')
    ylabel('geo values')
    title('ellipsoid Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    ellipsoid_plot_props(0, 10)