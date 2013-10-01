import fasta
from pdb import set_trace
import copy

infile = "rosalind_long.txt"

S = 0
T = -1

with open(infile,"r") as f:
    dnas,_ = fasta.read_fasta(f)

taxon = dnas.keys()
dnas[S] = ""
dnas[T] = ""

def compute_distance(s1,s2):
    if len(s2) == 0:
        return 0

    pos = 0
    while pos != -1:
        l = len(s1) - pos
        if s1[pos:] == s2[:l]:
            return len(s2) - l

        pos = s1.find(s2[0],pos+1)

    return len(s2)

mat = {}
for k1 in dnas.keys():
    for k2 in dnas.keys():
        mat[k1,k2] = compute_distance(dnas[k1],dnas[k2])
        if k1 != S and k2 != T and k1 != T and k2 != T:
            if mat[k1,k2] > len(dnas[k1])/2 or mat[k1,k2] > len(dnas[k2])/2: # see problem description
                del mat[k1,k2]

del mat[S,T]

#initialize
best = None
best_path = None
path = []

def solve():
    global path,best,best_path

    def iter(cur_dis,vs):
        global path,best,best_path

        assert(best_path == None or len(best_path) == len(taxon))

        if len(vs) == len(taxon):
            if best == None or cur_dis < best:
                best = cur_dis
                best_path = list(path)

                print("best:%d" % best)

            return

        if best != None and cur_dis > best:
            return

        for i in range(len(taxon)):
            if not i in vs and mat.get((taxon[path[-1]],taxon[i]),None) != None:
                r = cur_dis + mat[taxon[path[-1]],taxon[i]]

                vs.add(i)
                path.append(i)
                iter(r,vs)
                vs.remove(i)
                path.pop()

    for i in range(len(taxon)):
        path = [i]
        iter(mat[S,taxon[i]],set([i]))

solve()

print(best)
print(best_path)

def reconstruct(path):
    ret = dnas[taxon[path[0]]]
    for i in range(len(path)-1):
        dna = dnas[taxon[path[i+1]]]
        l = mat[taxon[path[i]], taxon[path[i+1]]]
        ret += dna[len(dna)-l:]

    return ret

print(reconstruct(best_path))

