def fac(n):
    r = 1
    while n != 0:
        r *= n
        n -= 1

    return r


def C(n,k):
    return int(fac(n)/(fac(n-k)*fac(k)))
