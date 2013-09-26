import fasta
from pdb import set_trace
import re
import sys

def read_blosum62():
    with open("blosum62.txt","r") as f:
        lines = f.readlines()

    lines[0] = lines[0].strip()
    cols = re.split("[ \t]+",lines[0])
    lines = lines[1:]

    scores = {}
    for line in lines:
        line = line.strip()
        row = re.split("[ \t]+",line)
        col = row[0]
        row = row[1:]

        for i in range(len(row)):
            scores[col,cols[i]] = int(row[i])

    return scores

infile = "sample.txt"
scores = read_blosum62()
g = 5

with open(infile ,"r") as f:
    dnas,keys = fasta.read_fasta(f)

s,t = dnas[keys[0]],dnas[keys[1]]

d = {}
d[-1,-1] = 0
p = {}
for i in range(len(s)):
    d[i,-1] = -(i+1)*g
for j in range(len(t)):
    d[-1,j] = -(j+1)*g

for i in range(len(s)):
    for j in range(len(t)):
        d[i,j] = d[i-1,j-1] + scores[s[i],t[j]]
        p[i,j] = 1

        if d[i-1,j] - g > d[i,j]:
            d[i,j] = d[i-1,j] - g
            p[i,j] = 2

        if d[i,j-1] - g > d[i,j]:
            d[i,j] = d[i,j-1] - g
            p[i,j] = 3


print(s,t)
print(d[len(s)-1,len(t)-1])

i = len(s)-1
j = len(t)-1

a1 = ""
a2 = ""

while i >= 0 and j >= 0:
    if p[i,j] == 1:
        a1 = s[i] + a1
        a2 = t[j] + a2
        i -= 1
        j -= 1
    elif p[i,j] == 2:
        a1 = s[i] + a1
        a2 = "-" + a2
        i -= 1
    else:
        a1 = "-" + a1
        a2 = t[j] + a2
        j -= 1

if i >= 0:
    a1 = s[:i+1] + a1
    a2 = "-"*(i+1) + a2
elif j >= 0:
    a2 = t[:j+1] + a2
    a1 = "-"*(j+1) + a1

print(a1)
print(a2)

ans = 0
for i in range(len(a1)):
    if a1[i] == "-" or a2[i] == "-":
        ans -= g
    else:
        ans += scores[a1[i],a2[i]]

#print(ans)
