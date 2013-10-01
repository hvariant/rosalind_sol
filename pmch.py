import fasta

infile = "rosalind_pmch.txt"

with open(infile,"r") as f:
    rnas,key = fasta.read_fasta(f)
    rna = rnas[key[0]]

n = len(rna)
nA = len(filter(lambda x:x == "A",rna))
nG = len(filter(lambda x:x == "G",rna))

def fac(n):
    if n == 0:
        return 1
    return n*fac(n-1)

#print(nA,nG)
print(fac(nA)*fac(nG))
