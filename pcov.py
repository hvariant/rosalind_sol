from pdb import set_trace

infile = "rosalind_pcov.txt"

with open(infile,"r") as f:
    dnas = []
    for dna in f.readlines():
        dnas.append(dna.strip())

def adj(s1,s2):
    return s1[1:] == s2[:-1]

def search(dnas):
    ans = []
    success = False

    stack = []
    stack.append(([],set([])))

    while len(stack) > 0 and not success:
        path,vs = stack.pop()

        if len(path) == len(dnas): # circle
            success = True
            ans = list(path)
            break
            
        for dna in dnas:
            if not dna in vs and (len(path) == 0 or adj(path[-1],dna) ):
                stack.append((path + [dna],vs.union(set(dna))))

    if success:
        return ans

#print(dnas)

r = search(dnas)
output = ""
for i in range(len(r)):
    output += r[i][0]

print(output)
assert(len(output) == len(dnas))

