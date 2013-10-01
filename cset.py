import chbp
import sys

infile = "rosalind_cset.txt"

with open(infile,"r") as f:
    chars = f.read()
    chars = chars.strip()
    chars = chars.split()

taxa = [str(n) for n in range(len(chars[0]))]
for i in range(len(chars)):
    nchars = chars[:i] + chars[i+1:]
    sys.stderr.write("%d\n" % i)
    
    if chbp.consistent(nchars,taxa):
        print("\n".join(nchars))
        break

    


