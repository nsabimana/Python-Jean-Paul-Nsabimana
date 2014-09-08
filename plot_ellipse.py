__author__ = 'jean'
from pylab import *

from geom_formulae import *


V_ellipse_area = np.vectorize(ellipse_area)
def ellipse_plot_props(start, end):
      S = np.linspace(start, end) # our semi_major axis lengths

      B = 2
      A = V_ellipse_area(S, B)# area
      plot(S, A, '-r', label="Area")
      xlabel('semi_major_axis, semi_minor_axis=4')
      ylabel('geo value')
      title('ellipse Geo properties')
      legend(loc='upper right')

      show()

if __name__ == "__main__":
    ellipse_plot_props(0, 10)