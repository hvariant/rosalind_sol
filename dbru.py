
infile = "rosalind_dbru.txt"

with open(infile,"r") as f:
    mers = []
    for l in f.readlines():
        mers.append(l.strip())

complement = {"A":"T","T":"A","G":"C","C":"G"}
def rc(dna):
    ret = ""
    for i in range(len(dna)):
        ret = complement[dna[i]] + ret

    return ret

edges = set()

for k1mer in mers:
    rk1mer = rc(k1mer)
    edges.add(k1mer)
    edges.add(rk1mer)

for edge in edges:
    print("(%s, %s)" % (edge[:-1],edge[1:]))
            

