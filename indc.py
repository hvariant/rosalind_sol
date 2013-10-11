from scipy.misc import comb
from numpy import log10,power
import decimal

decimal.getcontext().prec = 100

n = 47
output = ""

ps = []
for k in range(2*n+1):
    ps.append(log10(comb(2*n,k)) + 2*n*log10(0.5))

for k in range(1,2*n+1):
    p = 0.0
    for l in range(k,2*n+1):
        p += 10 ** ps[l]

    output += "%f " % log10(p)

print(output)
