import requests
import fasta
from pdb import set_trace
import string

def get_prot(uniprot_id):
    url = "http://www.uniprot.org/uniprot/%s.fasta" % uniprot_id
    resp = requests.get(url)
    return fasta.parse_fasta(resp.content)[0].values()[0]


def find_motif(prot,motif):
    def motif_len(motif):
        r = 0
        i = 0
        while i < len(motif):
            if motif[i] in string.ascii_letters:
                r += 1
                i += 1
            else:
                r += 1
                i += 1
                while motif[i] in string.ascii_letters:
                    i += 1
                i += 1

        return r

    def motif_match(motif,pos,amino):
        if motif[pos] in string.ascii_letters:
            return (motif[pos] == amino,pos+1)

        left = motif[pos]
        rpos = pos+1
        while motif[rpos] in string.ascii_letters:
            rpos += 1

        charset = motif[pos+1:rpos]
        if left == "[":
            return (amino in charset,rpos+1)
        else:
            return (not amino in charset,rpos+1)

    ret = []
    L = motif_len(motif)
    for i in range(len(prot)-L):
        pos = 0
        success = True
        for j in range(i,i+L):
            r,pos = motif_match(motif,pos,prot[j])
            if not r:
                success = False
                break

        if success:
            ret.append(i)

            
    return ret

motif = "N{P}[ST]{P}"
prots = {}
with open("rosalind_mprt.txt","r") as f:
    for prot_id in f.readlines():
        prot_id = prot_id.strip()
        prot = get_prot(prot_id)
        prots[prot_id] = prot

for prot_id in prots:
    r = find_motif(prots[prot_id],motif)
    if len(r) > 0:
        print(prot_id)
        print(" ".join([str(x+1) for x in r]))

