from collections import deque
from pdb import set_trace
from time import time

from pickle import dump,load

from os import system

#infile = "sample.txt"
infile = "rosalind_sort.txt"

def get_perm(p1,p2):
    ret = []
    for i in range(len(p1)):
        ret.append(p1.index(p2[i])+1)

    return ret

dis = {}
pre = {}
first = True

def fac(n):
    r = 1
    while n != 0:
        r *= n
        n -= 1

    return r

def encode(p):
    cache = range(1,len(p)+1)

    r = 0
    b = fac(len(p)-1)
    for i in range(len(p)):
        j = cache.index(p[i])
        r += j * b

        cache.remove(p[i])
        if len(p)-i-1 != 0:
            b = int(b/(len(p)-i-1))

    return r


def rev(p):
    global dis,pre,first

    assert(encode(range(1,len(p)+1)) == 0)
    assert(encode(range(len(p),0,-1)) == fac(len(p))-1)

    ip = encode(p)

    if not first:
        return dis[ip]

    first = False

    with open("dis.data","r") as f:
        dis = load(f)
    with open("pre.data","r") as f:
        pre = load(f)

    return rev(p)


ans = []
with open(infile,"r") as f:
    line = f.readline()
    line2 = f.readline()
    line = line.strip()
    line2 = line2.strip()

    print(line,line2)
    p1 = map(int,line.split())
    p2 = map(int,line2.split())
    perm = get_perm(p1,p2)

    rd = rev(perm)

    print(rd)

    ops = []
    tp = perm
    p0 = range(1,len(perm)+1)
    while tp != p0:
        op = pre[encode(tp)]
        ops.append(op)

        i,j = op
        tp = tp[:i] + list(reversed(tp[i:j])) + tp[j:]
        assert(len(tp) == len(perm))

print(rd)
print("\n".join(map(lambda (x,y): "%d %d" % (x+1,y),reversed(ops))))
