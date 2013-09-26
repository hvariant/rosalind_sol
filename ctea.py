import fasta
from pdb import set_trace
import re
import sys

infile = "rosalind_ctea.txt"

with open(infile ,"r") as f:
    dnas,keys = fasta.read_fasta(f)

s,t = dnas[keys[0]],dnas[keys[1]]

M = 134217727

d = {}
d[-1,-1] = 0
ops = {}
ops[-1,-1] = 1

for i in range(len(s)):
    d[i,-1] = i+1
    ops[i,-1] = 1
    
for j in range(len(t)):
    d[-1,j] = j+1
    ops[-1,j] = 1

for i in range(len(s)):
    for j in range(len(t)):
        d[i,j] = d[i-1,j-1]
        if s[i] != t[j]:
            d[i,j] += 1

        ops[i,j] = ops[i-1,j-1]

        if d[i-1,j] + 1 < d[i,j]:
            d[i,j] = d[i-1,j] + 1
            ops[i,j] = ops[i-1,j]
        elif d[i-1,j] + 1 == d[i,j]:
            ops[i,j] = (ops[i,j] + ops[i-1,j]) % M

        if d[i,j-1] + 1 < d[i,j]:
            d[i,j] = d[i,j-1] + 1
            ops[i,j] = ops[i,j-1]
        elif d[i,j-1] + 1 == d[i,j]:
            ops[i,j] = (ops[i,j] + ops[i,j-1]) % M

print(d[len(s)-1,len(t)-1])
print(ops[len(s)-1,len(t)-1])

#print("\n"*4)
#print("d")
#for i in range(-1,len(s)):
    #line = ""
    #for j in range(-1,len(t)):
        #line += "\t%d" % d[i,j]

    #print(line)

#print("\n"*4)
#print("ops")
#for i in range(-1,len(s)):
    #line = ""
    #for j in range(-1,len(t)):
        #line += "\t%d" % ops[i,j]

    #print(line)

set_trace()
