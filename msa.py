import fasta

infile = "rosalind_mult.txt"
with open(infile,"r") as f:
    dnas,keys = fasta.read_fasta(f)

ss = []
for k in keys:
    ss.append(dnas[k])

d = {}
p = {}

INF = 10000000

print(ss)

def score(c):
    r = 0
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            if c[i] != c[j]:
                r -= 1

    return r


for i0 in range(-1,len(ss[0])):
    for i1 in range(-1,len(ss[1])):
        for i2 in range(-1,len(ss[2])):
            for i3 in range(-1,len(ss[3])):
                if i0 == -1 and i1 == -1 and i2 == -1 and i3 == -1:
                    d[i0,i1,i2,i3] = 0
                    continue

                cd = -INF
                cp = -1

                for patt in range(1,16):
                    pi0,pi1,pi2,pi3 = i0,i1,i2,i3
                    c = ["-"]*4

                    if patt & 1 != 0:
                        pi0 = i0 - 1
                        c[0] = ss[0][i0]
                    if patt & 2 != 0:
                        pi1 = i1 - 1
                        c[1] = ss[1][i1]
                    if patt & 4 != 0:
                        pi2 = i2 - 1
                        c[2] = ss[2][i2]
                    if patt & 8 != 0:
                        pi3 = i3 - 1
                        c[3] = ss[3][i3]

                    if pi0 < -1 or pi1 < -1 or pi2 < -1 or pi3 < -1:
                        continue

                    r = d[pi0,pi1,pi2,pi3] + score(c)
                    if r > cd:
                        cd = r
                        cp = patt

                d[i0,i1,i2,i3] = cd
                p[i0,i1,i2,i3] = cp


nss = [""]*4
i0 = len(ss[0])-1
i1 = len(ss[1])-1
i2 = len(ss[2])-1
i3 = len(ss[3])-1

print(d[i0,i1,i2,i3])

while i0 >= 0 or i1 >= 0 or i2 >= 0 or i3 >= 0:
    patt = p[i0,i1,i2,i3]
    if patt & 1 != 0:
        nss[0] = ss[0][i0] + nss[0]
        i0 -= 1
    else:
        nss[0] = "-" + nss[0]

    if patt & 2 != 0:
        nss[1] = ss[1][i1] + nss[1]
        i1 -= 1
    else:
        nss[1] = "-" + nss[1]

    if patt & 4 != 0:
        nss[2] = ss[2][i2] + nss[2]
        i2 -= 1
    else:
        nss[2] = "-" + nss[2]

    if patt & 8 != 0:
        nss[3] = ss[3][i3] + nss[3]
        i3 -= 1
    else:
        nss[3] = "-" + nss[3]

print("\n".join(nss))
