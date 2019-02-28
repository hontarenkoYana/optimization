from math import log


def f0(x):
    return x**3 - 27 * x + 5


def f1(x):
    return (x**2 - 2 * x) * log(x) - (3 / 2) * x**2 + 4 * x


def df1(x):
    return 2 * (x - 1) * (log(x) - 1)


def d2f1(x):
    return 2 * log(x) - 2 / x