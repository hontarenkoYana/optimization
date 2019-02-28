from function import f_for_methods

import numpy as np


def huk(x0, eps):
    n = len(x0)

    lamb = 1
    alpha = 2
    delta = 0.5

    x1 = np.ones(n, dtype=np.float)
    k = 1

    while delta > eps:
        y1 = np.ones(n, dtype=np.float)
        for i in range(0, n):
            y0 = x0.copy()
            y0[i] = y0[i] + delta
            if f_for_methods(y0) < f_for_methods(x0):
                y1[i] = y0[i]
            else:
                y0[i] = y0[i] - 2 * delta
                if f_for_methods(y0) < f_for_methods(x0):
                    y1[i] = y0[i]
                else:
                    y1[i] = x0[i]
        if f_for_methods(y1) < f_for_methods(x0):
            x1 = y1 + lamb * (y1 - x0)
            x0 = x1.copy()
        else:
            delta = delta / alpha
        k = k + 1

    return [x1, f_for_methods(x1), k]
