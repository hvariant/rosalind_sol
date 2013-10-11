with open("rosalind_conv.txt","r") as f:
    ss = []
    for line in f.readlines():
        line = line.strip()
        ss.append([round(float(x),5) for x in line.split()])

S1 = ss[0]
S2 = ss[1]

S1_S2 = {}
for s1 in S1:
    for s2 in S2:
        k = round(s1-s2,5)
        S1_S2.setdefault(k,0)
        S1_S2[k] += 1

k = max(S1_S2.keys(),key = lambda x:S1_S2[x])

print(S1_S2[k])
print(k)

