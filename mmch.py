import fasta

def fac(n):
    r = 1
    while n != 0:
        r *= n
        n -= 1

    return r

def P(m,n):
    return int(fac(m)/(fac(m-n)))

with open("rosalind_mmch.txt","r") as f:
    rnas,_ = fasta.read_fasta(f)
    rna = rnas.values()[0]

nA = rna.count("A")
nU = rna.count("U")
nG = rna.count("G")
nC = rna.count("C")


def compute(a,b):
    a,b = min(a,b),max(a,b)

    return P(b,a)

ans = compute(nA,nU) * compute(nG,nC)
print(ans)
