from function import f0
from numpy import abs


def method_of_dichotomy(a, b, delta, eps):
    k = 0
    y = (a + b - delta) / 2
    z = (a + b + delta) / 2
    f_y = f0(y)
    f_z = f0(z)
    while abs(b - a) >= eps:
        if f_y <= f_z:
            b = z
        else:
            a = y
        y = (a + b - delta) / 2
        z = (a + b + delta) / 2
        f_y = f0(y)
        f_z = f0(z)
        k = k + 1
    return [(a + b) / 2, f0((a + b) / 2), k]
