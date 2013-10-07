
infile = "rosalind_trie.txt"

class Node:
    tag = 1

    def __init__(self):
        self.tag = Node.tag
        self.children = {}
        Node.tag += 1
    
    def add_child(self,edge,child):
        self.children[edge] = child

    def get_adj_list(self,ret=None):
        if ret == None:
            ret = []

        for e,c in self.children.items():
            ret = c.get_adj_list(ret)
            ret.append((self.tag,c.tag,e))

        return ret

    def insert_string(self,s):
        if len(s) == 0:
            return

        if self.children.get(s[0],False):
            self.children[s[0]].insert_string(s[1:])
        else:
            n = Node()
            self.add_child(s[0],n)
            n.insert_string(s[1:])

root = Node()
with open(infile,"r") as f:
    for s in f.readlines():
        s = s.strip()
        root.insert_string(s)

for t1,t2,e in root.get_adj_list():
    print("%d %d %s" % (t1,t2,e))

