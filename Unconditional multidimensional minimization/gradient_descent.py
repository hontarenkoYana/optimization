import numpy as np
from scipy.linalg import norm

from function import f_for_methods, df


def gradient_descent(x0, eps1, eps2, M):
    k = 0
    g = df(x0)
    t = 0.5
    while norm(g) > eps1 and k < M:
        x1 = x0 - t * g
        if (f_for_methods(x1) - f_for_methods(x0)) >= 0:
            t = t / 2
        else:
            if norm(x1 - x0) > eps2 or np.abs(f_for_methods(x1) - f_for_methods(x0)) > eps2:
                k += 1
                x0 = np.array(x1.copy())
                g = df(x0)
            else:
                k = M + 1
    return x1, k
