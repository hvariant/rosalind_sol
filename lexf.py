
alpha = "TBGJPNAKO"
n = 3

def output(s):
    print("".join([alpha[i] for i in s]))

def enum(alpha,n):
    enum.s = []
    def recur(cur):
        if cur == n:
            output(enum.s)
            return

        for i in range(len(alpha)):
            enum.s.append(i)
            recur(cur+1)
            enum.s.pop()

    recur(0)

enum(alpha,n)
