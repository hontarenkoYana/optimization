def f_for_methods(x):
    return 4 * (x[0] - 5)**2 + (x[1] - 6)**2


def f_for_plot(x, y):
    return 4 * (x - 5)**2 + (y - 6)**2


def df(x):
    from numpy import array
    return array([8 * (x[0] - 5), 2 * (x[1] - 6)])
