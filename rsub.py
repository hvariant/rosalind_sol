import newick
import fasta

def find_rev(t,dnas):
    r = []
    for i in range(len(dnas[t.u])):
        r += [(p[0],p[-1],i,dnas[p[0].u][i]) for p in t.find_rev(dnas,i)]

    return r

infile = "rosalind_rsub.txt"
with open(infile,"r") as f:
    nw = f.readline()
    nw.split()

    tree = newick.newick_parse(nw)
    fst = f.read()
    dnas,_ = fasta.parse_fasta(fst)

nodes = tree.nodes()
for node in nodes:
    revs = find_rev(node,dnas)
    #print("="*10)
    for fc,dest,pos,mid in revs:
        print("%s %s %d %s->%s->%s" %
              (fc.u,dest.u,pos+1,dnas[node.u][pos],mid,dnas[dest.u][pos]))

        #test
        assert(dnas[node.u][pos] == dnas[dest.u][pos])


