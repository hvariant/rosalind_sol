from common import *

n = 927
M = 1000000

B = [0]*(n+1)
B[1] = B[2] = 1

for i in range(3,n+1):
    if i % 100 == 0:
        print("iter:%d" % i)

    for j in range(1,int((i-1)/2)+1):
        B[i] = (B[i] + C(i,j) * B[j] * B[i-j]) % M

    if i % 2 == 0:
        B[i] = (B[i] + int(C(i,int(i/2)) * B[int(i/2)] * B[int(i/2)] / 2)) % M

print(B[n])
