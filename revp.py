import fasta
from pdb import set_trace

infile = "rosalind_revp.txt"
with open(infile,"r") as f:
    dnas,_ = fasta.read_fasta(f)
    dna = dnas.values()[0]

comp = {"A":"T",
        "T":"A",
        "G":"C",
        "C":"G"}

def complement(s):
    r = ""
    for i in range(len(s)):
        r += comp[s[i]]

    return r
    
def revp(s):
    rs = "".join(list(reversed(s)))
    return complement(rs) == s

for i in range(len(dna)):
    for l in range(4,min(len(dna)-i,12)+1):
        sub = dna[i:i+l]
        if revp(sub):
            print("%d %d" % (i+1,l))
            

#set_trace()
