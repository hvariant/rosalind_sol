import re

def parse(s):
     s = s.strip()
     s = s.strip("{")
     s = s.strip("}")
     return set(re.split("[ \t,]+",s))

def output(s):
     return "{" + ", ".join(s) + "}"

with open("rosalind_seto.txt","r") as f:
    n = int(f.readline())
    s1 = parse(f.readline())
    s2 = parse(f.readline())

print(output(s1.union(s2)))
print(output(s1.intersection(s2)))
print(output(s1.difference(s2)))
print(output(s2.difference(s1)))
x = set(map(lambda x:str(x),range(1,n+1)))
print(output(x.difference(s1)))
print(output(x.difference(s2)))

