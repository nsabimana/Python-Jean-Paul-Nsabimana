__author__ = 'jean'
from pylab import *

from geom_formulae import *

# make functions able to operate on vectors

v_cylinder_volume = np.vectorize(cylinder_volume)

def cylinder_plot_props(start, end):
    """
    Plot the volume of cylinder  as a function of height
    length, with radius length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end) # our height lengths
    C = 5
    A = v_cylinder_volume(S,C)  # the volume
    plot(S, A, '-r', label="volume")
    xlabel('radius length')
    ylabel('geo values')
    title('cylinder Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    cylinder_plot_props(0, 10)