__author__ = 'jean'


import numpy as np


def simpsons(f, a, b, n):
    deltax = (b-a)/n
    points = np.linspace(a, b, n+1)
    print(points)
    fpoints = f(points)
    coeffs = np.zeros(n-1)
    coeffs[0::2] = 4
    coeffs[1::2] = 2
    res += np.sum(coeffs[0]*fpoints[1:-1]) +fpoints[-1]
    return deltax/3*res
#   res = fpoints[0] + 4*np.sum(fpoints[1:-1:2])+2*np.sum(fpoints[2:-1:2])+fpoints[-1]


def midpoint(f, a, b, n):
    deltax = (b-a)/n
    start = a+deltax/2
    end = b-deltax/2
    print(start, end)
    mids = np.linspace(start, end, n)
    print(mids)
    fsum = np.sum(fs)
    return deltax*sum



def trapezoid(f, a, b, n):
    deltax = (b-a)/n
    points = np.linspace(a, b ,n+1)
    print(points)
    fpoints = f(points)
    res = fpoints[0]+fpoints[-1]+fpoints[1:-1]
    return res*deltax/2


poly_coeffs = [2,3,5]

def f1(x):
    return 2*x**2 + 3*x + 5

pf1 = np.poly1d(poly_coeffs)
a, b = 0, 10

n = 100

print(simpsons(f1,a,b,n))
print(midpoint(f1,a,b,n))
print(trapezoid(f1,a,b,n))

pfi = pf1.integ()
print(pfi(b)-pfi(a))