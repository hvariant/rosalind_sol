n = 96
m = 18

stages = [1] + [0]*(m-1)

for dummy in range(n-1):
    print(stages)

    newstages = [0]*m

    for i in range(1,m):
        newstages[i] = stages[i-1]
    newstages[0] = sum(stages[1:])

    stages = newstages

print(sum(stages))
