def enum(alphabet, s, n, ret):
    if len(s) == n:
        ret.add(s)
        return
    
    for a in alphabet:
        enum(alphabet,s + a,n,ret)

def solve(alphabet, N):
    ret = set()
    for i in range(1,N+1):
        enum(alphabet,"",i,ret)

    return ret

def strcmp(alphabet,x,y):
    order = {}
    val = 1
    for a in alphabet:
        order[a] = val
        val += 1

    L = min(len(x),len(y))
    for i in range(L):
        if x[i] != y[i]:
            return order[x[i]] - order[y[i]]

    return len(x) - len(y)

with open("rosalind_lexv.txt","r") as f:
    line = f.readline()
    line = line.strip()
    alphabet = line.split()
    N = int(f.readline())

    #print(alphabet,N)
    ret = solve(alphabet,N)

    print("\n".join(sorted(ret,cmp=lambda x,y: strcmp(alphabet,x,y))))
