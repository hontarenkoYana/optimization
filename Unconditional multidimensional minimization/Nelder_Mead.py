from function import f_for_methods
import numpy as np


def Nelder_Mead(x1, x2, x3, eps):
    alpha = 1
    beta = 0.5
    hamma = 2
    k = 0

    lst = [[f_for_methods(x1), x1], [f_for_methods(x2), x2], [f_for_methods(x3), x3]]
    lst = sorted(lst)

    xl = np.array(lst[0][1])
    xs = np.array(lst[1][1])
    xh = np.array(lst[2][1])

    x4 = (1 / 2) * (xl + xs)
    sigma = ((1 / 3) * ((f_for_methods(x1) - f_for_methods(x4))**2 +
                        (f_for_methods(x2) - f_for_methods(x4))**2 +
                        (f_for_methods(x3) - f_for_methods(x4))**2))**(1 / 2)
    while sigma > eps:
        f = 0
        x5 = x4 + alpha * (x4 - xh)
        if f_for_methods(x5) <= f_for_methods(xl):
            x6 = x4 + hamma * (x5 - x4)
            if f_for_methods(x6) < f_for_methods(xl):
                xh = x6
            else:
                xh = x5
        elif f_for_methods(xs) < f_for_methods(x5) and f_for_methods(x5) <= f_for_methods(xh):
            x7 = x4 + beta * (xh - x4)
            xh = x7
        elif f_for_methods(xl) < f_for_methods(x5) and f_for_methods(x5) <= f_for_methods(xs):
            xh = x5
        else:
            x1 = xl + 0.5 * (x1 - xl)
            x2 = xl + 0.5 * (x2 - xl)
            x3 = xl + 0.5 * (x3 - xl)
            f = 1
        k = k + 1
        if f == 0:
            x1 = xh
            x2 = xs
            x3 = xl
        lst = [[f_for_methods(x1), x1], [f_for_methods(x2), x2], [f_for_methods(x3), x3]]
        lst = sorted(lst)
        xl = np.array(lst[0][1])
        xs = np.array(lst[1][1])
        xh = np.array(lst[2][1])
        x4 = (1 / 2) * (xl + xs)
        sigma = ((1 / 3) * ((f_for_methods(x1) - f_for_methods(x4))**2 +
                            (f_for_methods(x2) - f_for_methods(x4))**2 +
                            (f_for_methods(x3) - f_for_methods(x4))**2))**(1 / 2)

    return [xl, f_for_methods(xl), k]
