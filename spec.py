import prtm
from pprint import pprint

table = prtm.read_iso_tab()

def find_by_value(v_):
    for k,v in table.items():
        if abs(v - v_) < 0.001:
            return k

    return None

ws = []
with open("rosalind_spec.txt","r") as f:
    for line in f.readlines():
        ws.append(float(line.strip()))

ws.sort()

ss = ""
for i in range(len(ws)-1):
    s = find_by_value(ws[i+1]-ws[i])
    assert(s != None)
    ss += s

print(ss)
