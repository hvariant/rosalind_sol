import fasta
from pdb import set_trace
from pprint import pprint

def hamm(s1,s2):
    r = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            r += 1

    return r

complement = {"A":"T","T":"A","G":"C","C":"G"}

def revcomp(s):
    r = ""
    for i in range(len(s)):
        r = complement[s[i]] + r

    return r

infile = "rosalind_corr.txt"
with open(infile,"r") as f:
    dnas,_ = fasta.read_fasta(f)
    count = {}
    for s in dnas.values():
        if count.get(revcomp(s),0) != 0:
            count[revcomp(s)] += 1
        else:
            count.setdefault(s,0)
            count[s] += 1

adjs = {}
for s in count.keys():
    adjs[s] = set()
    for s2 in count.keys():
        if s == s2:
            continue

        if hamm(s,s2) == 1 or hamm(s,revcomp(s2)) == 1 or hamm(revcomp(s),s2) == 1:
            adjs.setdefault(s2,set())
            adjs[s].add(s2)
            adjs[s2].add(s)

#pprint(count)
#pprint(adjs)
            
for s in count.keys():
    if count[s] >= 2:
        continue

    #print(s)
    #set_trace()

    if count[s] == 1 and len(adjs[s]) > 0:
        for s2 in adjs[s]:
            if count[s2] >= 2:
                if hamm(s,s2) == 1:
                    print("%s->%s" % (s,s2))
                else:
                    print("%s->%s" % (s,revcomp(s2)))

                break

#set_trace()
