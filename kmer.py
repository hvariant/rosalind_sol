import fasta
from pdb import set_trace

infile = "rosalind_kmer.txt"
with open(infile,"r") as f:
    dnas,_ = fasta.read_fasta(f)
    dna = dnas.values()[0]

alpha = "ACGT"

def gen_perm(k):
    gen_perm.ret = []
    gen_perm.sol = []

    def iter(i):
        if i == k:
            gen_perm.ret.append("".join(gen_perm.sol))
            return

        for a in alpha:
            gen_perm.sol.append(a)
            iter(i+1)
            gen_perm.sol.pop()

    iter(0)
    return gen_perm.ret

k = 4
kmer = {}
perms = gen_perm(k)

#set_trace()

for p in perms:
    kmer.setdefault(p,0)

for i in range(len(dna)-k+1):
    mer = dna[i:i+k]
    kmer[mer] += 1

output = []
for p in perms:
    output.append(kmer[p])

print(" ".join([str(x) for x in output]))
