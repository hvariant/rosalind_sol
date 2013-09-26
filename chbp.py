from pdb import set_trace
import newick

infile = "rosalind_chbp.txt"
#infile = "sample.txt"
internals = []

class Node:
    def __init__(self,taxon=None):
        self.adjs = set()

        for adj in self.adjs:
            adj.add_adj(self)

        self.taxon = taxon

    def add_adj(self,branch):
        self.adjs.add(branch)
        if not branch.is_adj(self):
            branch.add_adj(self)

    def prune(self,branchs):
        self.adjs = self.adjs.difference(set(branchs))
        for branch in branchs:
            if branch.is_adj(self):
                branch.prune([self])

    def fold(self,par=None):
        if self.taxon == None: # internal node
            ret = ",".join([adj.fold(self) for adj in self.adjs if adj != par])
            if ret != "":
                ret = "(" + ret + ")"
        else: # taxon node
            ret = self.taxon

        return ret

    def taxa(self,par=None,ret=None):
        if ret == None:
            ret = set()

        if self.taxon != None:
            ret.add(self.taxon)

        for adj in self.adjs:
            if adj != par:
                ret = adj.taxa(self,ret)

        return ret
    
    def split(self,cat):
        branches = set()
        bcat = set()

        for adj in self.adjs:
            subtaxa = adj.taxa(self)
            if subtaxa.issubset(cat):
                branches.add(adj)
                bcat = bcat.union(subtaxa)
            elif len(subtaxa.intersection(cat)) > 0:
                return False

        if bcat == cat:
            ni = Node()
            internals.append(ni)

            self.prune(branches)
            self.add_adj(ni)
            for b in branches:
                ni.add_adj(b)

            return True

        return False

    def is_internal(self):
        return self.taxon == None

    def is_adj(self,branch):
        return branch in self.adjs

    def __str__(self):
        if self.is_internal():
            return str([adj.taxon for adj in self.adjs])

        return str(self.taxon)

    def __repr__(self):
        return "taxon:" + str(self)

    def check_struct(self):
        for adj in self.adjs:
            assert(self in adj.adjs)


def initialize(taxa):
    root = Node()

    internals.append(root)
    for taxon in taxa:
        root.add_adj(Node(taxon))

def split(char,taxa):
    cat = set()
    for i in range(len(taxa)):
        if char[i] == "0":
            cat.add(taxa[i])

    success = False
    for n in internals:
        if n.split(cat):
            success = True
            break

    assert(success)

#utils
def invert(s):
    ret = ""
    for i in range(len(s)):
        if s[i] == "0":
            ret += "1"
        else:
            ret += "0"

    return ret

def gen_char(cat,taxa):
    ret = ""
    for i in range(len(taxa)):
        if taxa[i] in cat:
            ret += "1"
        else:
            ret += "0"

    return ret

with open(infile,"r") as f:
    line = f.readline()
    line = line.strip()
    taxa = line.split()

    initialize(taxa)
    #print(taxa)

    chars = []

    char = f.readline()
    char = char.strip()
    while char != "":
        split(char,taxa)
        chars.append(char)

        char = f.readline()
        char = char.strip()

        #print("="*10)

    r = internals.pop()
    ans = r.fold() + ";"

    t = newick.newick_parse(ans)
    r = newick.edge_splits(t,taxa)
    for char in chars:
        assert(char in r or invert(char) in r)

    print(ans)
