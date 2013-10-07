N = 19
k = 6

def fac(n):
    r = 1
    while n != 0:
        r *= n
        n -= 1

    return r


def C(n,k):
    return int(fac(n)/(fac(n-k)*fac(k)))
    

def P(k,n):
    return C(2**k,n) * 0.25**n * 0.75 **(2**k-n)

p = 0.0
for i in range(N):
    p += P(k,i)
p = 1-p

print(p)


