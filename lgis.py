

with open("rosalind_lgis.txt","r") as f:
    ns = f.readline()
    n = int(ns.strip())
    
    ps = f.readline()
    ps = ps.strip()
    ps = [int(i) for i in ps.split()]

#print(n)
#print(ps)

def print_seq(pre,l,ps):
    r = [l]
    while pre[l] != l:
        r.append(pre[l])
        l = pre[l]

    print(" ".join([str(ps[x]) for x in reversed(r)]))

dp = {}
dp2 = {}
pre = {}
pre2 = {}
l = 0
l2 = 0
for i in range(len(ps)):
    dp[i] = 1
    pre[i] = i

    dp2[i] = 1
    pre2[i] = i

    for j in range(i):
        if dp[j] + 1 > dp[i] and ps[i] > ps[j]:
            dp[i] = dp[j] + 1
            pre[i] = j

        if dp2[j] + 1 > dp2[i] and ps[i] < ps[j]:
            dp2[i] = dp2[j] + 1
            pre2[i] = j

    if dp[i] > dp[l]:
        l = i
    if dp2[i] > dp2[l2]:
        l2 = i

print_seq(pre,l,ps)
print_seq(pre2,l2,ps)
