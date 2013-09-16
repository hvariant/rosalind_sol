import fasta
import translate
import sys,os
import re
import math
import string
from pdb import set_trace

#infile = sys.argv[1]

#f = open(infile,"r")
#string = f.read()[::-1]
#string = string.strip()

#complement = {}
#complement["A"] = "T"
#complement["T"] = "A"
#complement["G"] = "C"
#complement["C"] = "G"

#output = ""
#for i in range(len(string)):
    #output += complement[string[i]]

#print(output)

#===============================

#s = "17028 17476 16849 19981 19283 19389"

#n1,n2,n3,n4,n5,n6 = [float(n) for n in s.split(" ")]

#ans = 2*(n1 + n2 + n3 + n4*0.75 + n5*0.5)
#print(ans)

#=================================

#f = open("rosalind_subs.txt","r")
#s = f.readline()
#t = f.readline()

#f.close()

#s = s.strip()
#t = t.strip()

#print(s)
#print(t)

##s = "GATATATGCATATACTT"
##t = "ATAT"

#output = ""
#for i in range(len(s) - len(t)):
    #if s[i:i+len(t)] == t:
        #if output == "":
            #output = str(i+1)
        #else:
            #output += " %d" % (i+1)

#print(output)

#============================

#n = 29
#k = 4

#young = 1
#mature = 0
#for i in range(n-1):
    #young,mature = mature*k,young + mature
    ##print(mature + young)

#print(mature + young)

#============================

#f = open("rosalind_hamm.txt","r")
#s = f.readline()
#t = f.readline()
#f.close()

#s = s.strip()
#t = t.strip()

##s = "GAGCCTACTAACGGGAT"
##t = "CATCGTAATGACGGCCT"

#ans = 0
#for i in range(len(s)):
    #if s[i] != t[i]:
        #ans += 1

#print(ans)

#=======================================

#infile = "rosalind_grph.txt"
#k = 3

#f = open(infile,"r")
#dnas,_ = fasta.read_fasta(f)
#f.close()

#nodes = dnas.keys()
#adjs = {}
#for node in nodes:
    #adjs[node] = set()

#for nA in nodes:
    #for nB in nodes:
        #if dnas[nA] == dnas[nB]:
            #continue

        #if dnas[nA][-k:] == dnas[nB][:k]:
            #adjs[nA].add(nB)

#for nA in nodes:
    #for nB in adjs[nA]:
        #print("%s %s" % (nA,nB))


#=========================================

#infile = "rosalind_cons.txt"

#f = open(infile,"r")
#dnas,_ = fasta.read_fasta(f)
#f.close()

#length = len(dnas[dnas.keys()[0]])

#profile = []
#for i in range(length):
    #profile.append({})
    #profile[i]["A"] = profile[i]["G"] = profile[i]["T"] = profile[i]["C"] = 0

#for k,v in dnas.items():
    #for i in range(len(v)):
        #profile[i][v[i]] += 1

#output = ""
#for i in range(length):
    #msym = "A"
    #for sym in ["A","C","G","T"]:
        #if profile[i][msym] < profile[i][sym]:
            #msym = sym

    #output += msym

#print(output)

#for symbol in ["A","C","G","T"]:
    #output = "%s:" % symbol
    #for i in range(length):
        #output += " %d" % profile[i][symbol]

    #print(output)

#=========================================

#n = 6

#def generate_perm(A):
    #if len(A) == 0:
        #return [[]]

    #ret = []
    #for a in A:
        #A.remove(a)
        #r = generate_perm(A)
        #ret += [[a] + s for s in r]
        #A.add(a)

    #return ret

#r = generate_perm(set(range(1,n+1)))
#print(len(r))
#for perm in r:
    #print(" ".join(map(lambda x:str(x),perm)))

#========================================

#s = "AACGACTCCAGGTCATCACTGAGACTGTGTAAGATCCAATTCACTCCGCTATCCTCTGGGCTCGCAAAAGTGATAGCGGACAGGCTTT"
#Astr = "0.084 0.146 0.184 0.266 0.310 0.401 0.444 0.479 0.578 0.603 0.663 0.732 0.800 0.836 0.928"
#A = [float(n) for n in Astr.split(" ")]

#B = []
#for x in A:
    #r = 0
    #for sym in s:
        #if sym == "A" or sym == "T":
            #p = (1-x)/2.0
        #else:
            #p = x/2.0

        #r += math.log(p,10)

    #B.append(r)

#print(" ".join(map(lambda x:str(x),B)))

#======================================

#infile = "rosalind_cstr.txt"

#dnas = []
#with open(infile,"r") as f:
    #for dna in f.readlines():
        #dna = dna.rstrip()
        #dnas.append(dna)

#splits = []
#for i in range(len(dnas[0])):
    #s = ""
    #count = 0

    #s1 = dnas[0][i]

    #for j in range(len(dnas)):
        #if dnas[j][i] == s1:
            #count += 1
            #s += "1"
        #else:
            #s += "0"

    #if count <= 1 or count >= len(dnas)-1:
        #continue

    #print(s)

#=====================================

#def generate_substrings(s):
    #ret = set()
    #for i in range(len(s)):
        #for j in range(1,len(s)-i):
            #ret.add(s[i:i+j])

    #return list(ret)

#with open("rosalind_lcsm.txt","r") as f:
    #dnas,_ = fasta.read_fasta(f)

#dnas = dnas.values()
#dnas.sort(key = lambda x:len(x))

#min_dna = dnas[0]
#substrings = generate_substrings(min_dna)
#substrings.sort(key = lambda x:-len(x))

#i = 0
#while i < len(substrings):
    #match = True

    #if i % 1000 == 0:
        #print("%d/%d %d" % (i,len(substrings),len(dnas)))

    #for j in range(1,len(dnas)):
        #if not substrings[i] in dnas[j]:
            #match = False
            #break

    #if match:
        #break

    #i += 1

#print(substrings[i])

#========================================

#def eliminate_intron(DNA,s):
    #k = DNA.find(s)
    #while k != -1:
        #print(DNA,DNA[:k],DNA[k+len(s):],DNA[k:k+len(s)])
        #DNA = DNA[:k] + DNA[k+len(s):]

        #k = DNA.find(s)

    #return DNA

#with open("rosalind_splc.txt","r") as f:
    #dnas,_ = fasta.read_fasta(f)

#mk = dnas.keys()[0]
#for k,v in dnas.items():
    #if len(dnas[mk]) < len(v):
        #mk = k

#DNA = dnas[mk]
#del dnas[mk]

#for intron in dnas.values():
    #print(DNA,intron)
    #DNA = eliminate_intron(DNA,intron)

#print(len(DNA),translate.translate(DNA))

#========================================

#with open("rosalind_sseq.txt","r") as f:
    #dnas,_ = fasta.read_fasta(f)

#s,t = dnas.values()
#if len(s) < len(t):
    #s,t = t,s

#i = s.find(t[0])
#output = str(i+1)

#k = i
#sub = True
#for j in range(1,len(t)):
    #k = s.find(t[j],k+1)
    #output += " %d" % (k+1)
    #if k == -1:
        #sub = False
        #break

#print(output)

#if not sub:
    #print("t is not a sub sequence of s")

#========================================


#with open("rosalind_lcsq.txt","r") as f:
    #dnas,_ = fasta.read_fasta(f)

#s,t = dnas.values()

#f = {}
#f[-1,-1] = 0
#for i in range(len(s)):
    #f[i,-1] = 0
#for j in range(len(t)):
    #f[-1,j] = 0

#p = {}

#for i in range(len(s)):
    #for j in range(len(t)):
        #if s[i] == t[j]:
            #f[i,j] = f[i-1,j-1] + 1
            #p[i,j] = 1

            #if f[i-1,j] > f[i,j]:
                #f[i,j] = f[i-1,j]
                #p[i,j] = 2

            #if f[i,j-1] > f[i,j]:
                #f[i,j] = f[i,j-1]
                #p[i,j] = 3

        #else:
            #f[i,j] = f[i-1,j]
            #p[i,j] = 2

            #if f[i,j-1] > f[i,j]:
                #f[i,j] = f[i,j-1]
                #p[i,j] = 3

#print(f[len(s)-1,len(t)-1])

#i = len(s)-1
#j = len(t)-1

#ans = ""
#while i >= 0 and j >= 0:
    #if p[i,j] == 1:
        #ans = s[i] + ans
        #i -= 1
        #j -= 1

    #elif p[i,j] == 2:
        #i -= 1
    #else:
        #j -= 1

#print(ans)

#==========================================


#with open("rosalind_edit.txt","r") as f:
    #dnas,_ = fasta.read_fasta(f)

#s,t = dnas.values()

#d = {}
#d[-1,-1] = 0
#for i in range(len(s)):
    #d[i,-1] = i+1
#for j in range(len(t)):
    #d[-1,j] = j+1

#for i in range(len(s)):
    #for j in range(len(t)):
        #if s[i] != t[j]:
            #d[i,j] = d[i-1,j-1] + 1
        #else:
            #d[i,j] = d[i-1,j-1]

        #if d[i-1,j] + 1 < d[i,j]:
            #d[i,j] = d[i-1,j] + 1

        #if d[i,j-1] + 1 < d[i,j]:
            #d[i,j] = d[i,j-1] + 1


#print(d[len(s)-1,len(t)-1])
