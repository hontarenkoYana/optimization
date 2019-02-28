from function import f0
from numpy import abs


def golden_section(a, b, eps):
    k = 0
    y = a + (3 - 5**(1 / 2)) / 2 * (b - a)
    z = a + b - y
    f_y = f0(y)
    f_z = f0(z)
    while abs(a - b) >= eps:
        if f_y <= f_z:
            b = z
            z = y
            y = a + b - y
        else:
            a = y
            y = z
            z = a + b - z
        k = k + 1
        f_y = f0(y)
        f_z = f0(z)
    return [(a + b) / 2, f0((a + b) / 2), k]
