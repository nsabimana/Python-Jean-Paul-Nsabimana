__author__ = 'jean'
from pylab import *

from geom_formulae import *

V_trapezoid_area = np.vectorize(trapezoid_area)

S = np.linspace(0,10)

B = 3
D = 6
A = V_trapezoid_area(S, B, D)# area


plot(S, A, '-r', label="Area")



xlabel('height length, small_base=3, large_base=6')
ylabel('geo value')
title('trapezoid Geo properties')
legend(loc='upper right')

show()


if __name__ == "__main__":
    plot_trapezoid(0,10)