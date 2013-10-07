
def read_iso_tab():
    ret = {}
    with open("monoisotopic_mass_table.txt","r") as f:
        for line in f.readlines():
            pair = line.split()
            prot = pair[0]
            mass = float(pair[1])
            ret[prot] = mass

    return ret

water_mass = 18.01056

#with open("rosalind_prtm.txt","r") as f:
    #line = f.readline()
    #prot = line.strip()

#table = read_iso_tab()
#ans = 0
#for a in prot:
    #ans += table[a]

#print(ans)
