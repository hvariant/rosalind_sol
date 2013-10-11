import decimal

#N = 7
#m = 10
#g = 6
#k = 5

line = "5 9 5 7"
N,m,g,k = [int(x) for x in line.split()]

P = [0 for _ in range(2*N+1)]
P[m] = 1

def fac(n):
    r = 1
    while n != 0:
        r *= n
        n -= 1

    return r


def C(n,k):
    return int(fac(n)/(fac(n-k)*fac(k)))

def Bin(N,k,p):
    return C(N,k) * p**k * (1-p)**(N-k)

for _ in range(g):
    nP = [0 for _ in range(2*N+1)]
    for i in range(2*N+1):
        for j in range(2*N+1):
            nP[i] += P[j] * Bin(2*N,i,j/float(2*N))

    P = nP

r = sum(P[:(2*N-k)+1])
print(r)
