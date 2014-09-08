__author__ = 'jean'

def secant(base, exp=2, it=20):
    def f(x):
        return x**exp - base
    x1 = base /(exp**2)
    xnm1 = x1 - 5
    xnm2 = x1 + 5
    xn = 0
    for n in range(it):
        q = (xnm1-xnm2)/(f(xnm1)-f(xnm2))
        xn = xnm1 - (f(xnm1)*q)
        xnm1, xnm2 = xn, xnm1
    return xn

print(secant(2, 2))
