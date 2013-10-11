n = 1876
m = 780

def fac(n):
    r = 1
    while n != 0:
        r *= n
        n -= 1

    return r


def C(n,k):
    return int(fac(n)/(fac(n-k)*fac(k)))
    
r = 0
M = 1000000
for k in range(m,n+1):
    r = (r + C(n,k))%M

print(r)

