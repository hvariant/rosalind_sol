import translate
import fasta
from pdb import set_trace

complement = {"A":"T",
              "G":"C",
              "C":"G",
              "T":"A"}

infile = "rosalind_orf.txt"

with open(infile) as f:
    dnas,_ = fasta.read_fasta(f)
    dna = dnas.values()[0]

cdna = "".join(reversed(map(lambda x:complement[x],dna)))
ans = set()

for i in range(len(dna)):
    if dna[i:i+3] == "ATG":
        #print("dna %d" % i)

        pro,c = translate.translate(dna[i:])
        if c:
            ans.add(pro)

for i in range(len(cdna)):
    if cdna[i:i+3] == "ATG":
        #print("cdna %d" % i)

        pro,c = translate.translate(cdna[i:])
        if c:
            ans.add(pro)

print("\n".join(ans))


