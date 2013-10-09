import fasta

infile = "rosalind_tran.txt"

with open(infile,"r") as f:
    dnas,_ = fasta.read_fasta(f)
    dnas = dnas.values()

def trans(c1,c2):
    s = set([c1,c2])
    if s == set("AG") or s == set("TC"):
        return True

    return False

tv = 0
ts = 0
for i in range(len(dnas[0])):
    if dnas[0][i] != dnas[1][i]:
        if trans(dnas[0][i],dnas[1][i]):
            ts += 1
        else:
            tv += 1

print(float(ts)/float(tv))
