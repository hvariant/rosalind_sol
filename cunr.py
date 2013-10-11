from pdb import set_trace

def fac(n):
    r = 1
    while n != 0:
        r *= n
        n -= 1

    return r


def C(n,k):
    return int(fac(n)/(fac(n-k)*fac(k)))

bs = [1,1,1,1]
N = 884
M = 1000000
for n in range(4,N+1):
    print("computing bs[%d]" % n)

    b = (n-1)*bs[n-1] % M
    for k in range(2,int((n-1)/2)+1):
        coef = C(n-1,k)
        if 2*k == n-1:
            coef /= 2

        b = (b + coef * bs[k+1] * bs[n-k]) % M

    if n-1 % 2 == 0:
        k = int((n-1)/2)
        b = (b + int(C(n-1,k)/2) * bs[k+1] * bs[n-k]) % M

    bs.append(b)

print(bs[N])

