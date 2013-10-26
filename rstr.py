from pdb import set_trace
import math

infile = "rosalind_rstr.txt"
#infile = "sample.txt"

def fac(n):
    r = 1
    while n != 0:
        r *= n
        n -= 1

    return r

def C(n,k):
    return int(fac(n)/(fac(n-k)*fac(k)))

with open(infile,"r") as f:
    line = f.readline()
    line = line.strip()
    N,x = line.split()
    N = int(N)
    x = float(x)
    line = f.readline()
    dna = line.strip()
    
nGC = len(filter(lambda x:x=='G' or x == 'C',dna))
nTA = len(filter(lambda x:x=='A' or x == 'T',dna))

pGC = x/2
pTA = (1-x)/2

ln_pEQ = math.log(pGC)*nGC + math.log(pTA)*nTA

ans = 1 - (1-math.exp(ln_pEQ))**N

print(ans)
