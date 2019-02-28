from function import f_for_methods
from numpy.linalg import norm
import numpy as np


def Dichotomy(x, i, eps):
    delta = eps / 10.
    a = -10
    b = 10
    xl = x.copy()
    xr = x.copy()
    while abs(b - a) > eps:
        xl[i] = (a + b - delta) / 2
        xr[i] = (a + b + delta) / 2
        if f_for_methods(xl) < f_for_methods(xr):
            b = xr[i]
        else:
            a = xl[i]
    return (a + b) / 2


def Coordinate(x0, eps):
    n = len(x0)
    x1 = np.zeros(n, dtype=np.float)
    for i in range(0, n):
        x1[i] = Dichotomy(x0, i, eps)
    k = 1
    while norm(x1 - x0) > eps:
        x0 = x1.copy()
        for i in range(0, n):
            x1[i] = Dichotomy(x0, i, eps)
        k = k + 1

    return [x1, f_for_methods(x1), k]
