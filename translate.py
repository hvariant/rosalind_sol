import re

def codon_table():
    f = open("codon_table.txt","r")
    table = {}
    for line in f.readlines():
        line = line.strip()
        pairs = re.split("[ \t]+",line)
        for i in range(len(pairs)/2):
            table[pairs[2*i]] = pairs[2*i+1]

    f.close()

    rtable = {}
    for k,v in table.items():
        rtable.setdefault(v,set([]))
        rtable[v].add(k)

    return table,rtable

def translate(s,type="DNA"):
    table,rtable = codon_table()

    if type == "DNA":
        rna = s.replace("T","U")
    else:
        rna = s

    protein = ""
    complete = False
    for i in range(len(rna)/3):
        if 3*i + 3 <= len(rna):
            amino = table[rna[3*i:3*i+3]]
            if amino == "Stop":
                complete = True
                break

            protein += amino
    
    return protein,complete


##print("the codon table")
##for k,v in table.items():
    ##print(k,v)

#f = open("rosalind_prot.txt","r")
##rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
#rna = f.read()
#rna = rna.strip()

#protein = ""
#for i in range(len(rna)/3):
    #if 3*i + 3 <= len(rna):
        #amino = table[rna[3*i:3*i+3]]
        #if amino == "Stop":
            #break

        #protein += amino

#print(protein)

#with open("rosalind_mrna.txt","r") as f:
    #protein = f.read()
    #protein = protein.strip()

#r = 1
#for v in protein:
    #r = (r*len(rtable[v])) % 1000000
#r = (r*len(rtable["Stop"])) % 1000000

#print(r)

