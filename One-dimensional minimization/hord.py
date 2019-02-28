from function import f1, df1


def hord(a, b, eps):
    k = 0
    x = a - (df1(a) / (df1(a) - df1(b)) * (a - b))
    d_f = df1(x)
    while abs(d_f) > eps:
        if d_f > 0:
            b = x
            k = k + 1
        else:
            a = x
            k = k + 1
        x = a - (df1(a) / (df1(a) - df1(b)) * (a - b))
        d_f = df1(x)
    return [x, f1(x), k]
