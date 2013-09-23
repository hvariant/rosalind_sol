from __future__ import division

def read_fasta(f):
    line = f.readline()
    dnas = {}
    ckey = ""
    key_seq = []

    while line != '':
        line = line.strip()

        if line[0] == ">":
            ckey = line[1:]
            key_seq.append(ckey)
            dnas[ckey] = ""
        else:
            dnas[ckey] += line

        line = f.readline()

    return dnas,key_seq

def parse_fasta(s):
    s = s.strip()
    lines = s.split()
    dnas = {}
    ckey = ""
    key_seq = []

    for line in lines:
        if line[0] == ">":
            ckey = line[1:]
            key_seq.append(ckey)
            dnas[ckey] = ""
        else:
            dnas[ckey] += line

    return dnas,key_seq

def kmp_preprocess(p):
    m = len(p)
    b = []

    i = 0
    j = -1

    b.append(j) # b[i] = j
    while i<m:
        while j>=0 and p[i]!=p[j]: 
            j=b[j]

        i += 1
        j += 1
        b.append(j) # b[i] = j

    return b

#with open("rosalind_kmp.txt","r") as f:
    ##dna = "CAGCATGGTATCACAGCAGAG"
    #dna = read_fasta(f)["Rosalind_4800"]

#print(" ".join(map(lambda x:str(x),kmp_preprocess(dna)[1:])))
