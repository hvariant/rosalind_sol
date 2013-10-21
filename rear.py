from collections import deque
from pdb import set_trace
from time import time

from pickle import dump,load

from os import system

#infile = "sample.txt"
infile = "rosalind_rear.txt"

#def rev_dis(p1,p2):
    #def encode(p):
        #return ",".join(map(str,p))

    #queue = deque()
    #queue.append((p1,0))
    #vs = set([encode(p1)])

    #iteration = 0
    #while len(queue) > 0:
        #iteration += 1
        #if iteration % 10000 == 0:
            #print(iteration,len(vs))

        #cp,cd = queue.popleft()

        #if cp == p2:
            #return cd
        
        ##branch
        #for i in range(len(cp)):
            #for j in range(i+1,len(cp)):
                #np = cp[:i] + list(reversed(cp[i:j+1])) + cp[j+1:]

                #inp = encode(np)
                #if not inp in vs:
                    #vs.add(inp)
                    #queue.append((np,cd+1))

    ##fuck
    #return -1

def get_perm(p1,p2):
    ret = []
    for i in range(len(p1)):
        ret.append(p1.index(p2[i])+1)

    return ret

dis = {}
pre = {}
first = True
pick = True

def fac(n):
    r = 1
    while n != 0:
        r *= n
        n -= 1

    return r

def encode(p):
    cache = range(1,len(p)+1)

    #print("="*10)

    r = 0
    b = fac(len(p)-1)
    for i in range(len(p)):
        j = cache.index(p[i])
        r += j * b

        #print(j,b)

        cache.remove(p[i])
        if len(p)-i-1 != 0:
            b = int(b/(len(p)-i-1))

    #print(p,r,fac(len(p)))

    return r

def rev(p):
    global dis,pre,first

    assert(encode(range(1,len(p)+1)) == 0)
    assert(encode(range(len(p),0,-1)) == fac(len(p))-1)

    ip = encode(p)

    if not first:
        return dis[ip]

    first = False

    if pick:
        print("reading from pickle dump")

        with open("dis.data","r") as f:
            dis = load(f)
        with open("pre.data","r") as f:
            pre = load(f)

        return rev(p)

    queue = deque()
    queue.append((range(1,len(p)+1),0))
    dis[0] = 0

    start_time = time()

    iteration = 0
    while len(queue) > 0:
        iteration += 1
        if iteration % 10000 == 0:
            print(iteration,len(dis.keys()),time() - start_time)
        
        cp,cd = queue.popleft()
        icp = encode(cp)

        for i in range(len(cp)):
            for j in range(i+1,len(cp)+1):
                np = cp[:i] + list(reversed(cp[i:j])) + cp[j:]
                assert(len(np) == len(cp))
                inp = encode(np)

                if dis.get(inp,None) == None:
                    dis[inp] = cd + 1
                    queue.append((np,cd+1))
                    pre[inp] = (i,j)


    assert(dis[0] == 0)
    assert(len(dis.keys()) == fac(len(p)))
    #set_trace()

    with open("dis.data","w") as f:
        dump(dis,f)
    with open("pre.data","w") as f:
        dump(pre,f)

    return rev(p)

def solve(line,line2):
    p1 = map(int,line.split())
    p2 = map(int,line2.split())

    perm = get_perm(p1,p2)
    print(perm)
    
    rd = rev(perm)

    return rd


ans = []
with open(infile,"r") as f:
    line = f.readline()
    while line != '':
        if line == "\n":
            line = f.readline()
            continue

        line2 = f.readline()
        line = line.strip()
        line2 = line2.strip()

        rd = solve(line,line2)
        print(line,line2,rd)
        ans.append(rd)

        line = f.readline()

print(" ".join(map(str,ans)))

system("terminal-notifier -message \"computation/loading completed.\"")
set_trace()
