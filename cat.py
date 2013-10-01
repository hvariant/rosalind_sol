import fasta
from pdb import set_trace

infile = "rosalind_cat.txt"
#infile = "sample.txt"

with open(infile,"r") as f:
    dnas,_ = fasta.read_fasta(f)
    dna = dnas.values()[0]

def complement(c1,c2):
    s = set([c1,c2])
    if s == set("AU") or s == set("GC"):
        return True

    return False

dp = {} #dp[i,j]: number of perfect matchings beginning at i and ending at j
dp2 = {} #dp2[i,j]: number of perfect matchings with i matched with j beginning at i and ending at j

for i in range(len(dna)):
    dp[i,i] = 0
    dp2[i,i] = 0

for i in range(len(dna)-1):
    if complement(dna[i],dna[i+1]):
        dp[i,i+1] = 1
        dp2[i,i+1] = 1
    else:
        dp[i,i+1] = 0
        dp2[i,i+1] = 0

for k in range(2,len(dna)):
    for i in range(len(dna)-k):
        if complement(dna[i],dna[i+k]):
            dp[i,i+k] = dp[i+1,i+k-1]
            dp2[i,i+k] = dp[i+1,i+k-1]
        else:
            dp[i,i+k] = 0
            dp2[i,i+k] = 0

        for j in range(1,k-1):
            dp[i,i+k] += dp2[i,i+j] * dp[i+j+1,i+k]

best = dp[0,len(dna)-1]

nA = len(filter(lambda x:x == "A",dna))
nG = len(filter(lambda x:x == "G",dna))

print(best,len(dna)/2)
print(best % 1000000)
        
set_trace()
