import fasta

with open("rosalind_lcsq.txt","r") as f:
    dnas,_ = fasta.read_fasta(f)

s,t = dnas.values()

f = {}
f[-1,-1] = 0
for i in range(len(s)):
    f[i,-1] = 0
for j in range(len(t)):
    f[-1,j] = 0

p = {}

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            f[i,j] = f[i-1,j-1] + 1
            p[i,j] = 1

            if f[i-1,j] > f[i,j]:
                f[i,j] = f[i-1,j]
                p[i,j] = 2

            if f[i,j-1] > f[i,j]:
                f[i,j] = f[i,j-1]
                p[i,j] = 3

        else:
            f[i,j] = f[i-1,j]
            p[i,j] = 2

            if f[i,j-1] > f[i,j]:
                f[i,j] = f[i,j-1]
                p[i,j] = 3

print(f[len(s)-1,len(t)-1])

i = len(s)-1
j = len(t)-1

ans = ""
while i >= 0 and j >= 0:
    if p[i,j] == 1:
        ans = s[i] + ans
        i -= 1
        j -= 1

    elif p[i,j] == 2:
        i -= 1
    else:
        j -= 1

print(ans)


