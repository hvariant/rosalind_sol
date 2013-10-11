from math import sqrt

infile = "rosalind_afrq.txt"

with open(infile,"r") as f:
    line = f.readline()
    line = line.strip()
    hqs = [float(x) for x in line.split()]

ans = [1 - pow(1 - sqrt(hq),2) for hq in hqs]

print(" ".join([str(x) for x in ans]))
