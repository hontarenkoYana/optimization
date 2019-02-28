from function import f1, df1, d2f1


def Nyuton(x0, eps):
    d_f = df1(x0)
    if abs(d_f) <= eps:
        return [x0, f1(x0), 0]
    k = 0
    d_2f = d2f1(x0)
    x = x0 - (d_f / d_2f)
    d_f = df1(x)
    while abs(d_f) > eps:
        k = k + 1
        x0 = x
        d_2f = d2f1(x0)
        x = x0 - (d_f / d_2f)
        d_f = df1(x)
    return [x, f1(x), k]
