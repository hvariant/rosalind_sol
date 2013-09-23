import random
import time
import sys

def geneticoptimize(domain,costf,popsize=50,
                    mutprob = 0.1,crossprob = 0.6,
                    elite=0.1,maxiter=1000,nv=1, field="i",step=0.3):

    def mutate(vec):
        i = random.randint(0,len(domain)-1)

        if field != "i":
            n = random.uniform(domain[i][0],domain[i][1])
            #if random.random() < 0.5:
                #n = vec[i] - random.uniform(0,step)
                #while n < domain[i][0]:
                    #n += (domain[i][1] - domain[i][0])

            #else:
                #n = vec[i] - random.uniform(0,step)
                #while n > domain[i][1]:
                    #n -= (domain[i][1] - domain[i][0])
        else:
            n = random.randint(domain[i][0],domain[i][1])

        return vec[0:i]+ [n] +vec[i+1:]

    def crossover(r1,r2):
        i = random.randint(1,len(domain)-1)
        return r1[0:i]+r2[i:],r2[0:i]+r1[i:]

    pop = []
    for i in range(popsize):
        if field == "i":
            vec = [random.randint(domain[i][0],domain[i][1])
                   for i in range(len(domain))]
        else:
            vec = [random.uniform(domain[i][0],domain[i][1])
                   for i in range(len(domain))]

        pop.append(vec)

    topelite = int(elite*popsize)
    nobetter = 0
    best = costf(pop[0])
    best_v = pop[0]
    for i in range(maxiter):
        #print("Generation %d(%d)" % (i,best))
        sys.stdout.write(">")
        sys.stdout.flush()

        if (i+1) % 10 == 0:
            print("[%d]" % best)

        #checkpoint = 0
        #print("checkpoint%d:%f" % (checkpoint,time.time()))
        #checkpoint += 1

        scores = [(costf(v),v) for v in pop]
        scores.sort()
        ranked = [v for (s,v) in scores]

        #print("checkpoint%d:%f" % (checkpoint,time.time()))
        #checkpoint += 1

        #mutate
        for i in range(len(pop)):
            if random.random() < mutprob:
                pop[i] = mutate(pop[i])

        for i in range(len(pop)):
            for j in range(i+1,len(pop)):
                if random.random() < crossprob:
                    pop[i],pop[j] = crossover(pop[i],pop[j])

        newpop = ranked[0:topelite]

        #print("checkpoint%d:%f" % (checkpoint,time.time()))
        #checkpoint += 1

        k = 2

        newscores = [costf(v) for v in pop]

        #print("checkpoint%d:%f" % (checkpoint,time.time()))
        #checkpoint += 1

        while len(newpop)<popsize:
            #selection method: tournament
            candidates = []
            for i in range(k):
                candidates.append(pop[random.randint(0,len(pop)-1)])

            bc = 0
            for i in range(1,k):
                if newscores[i] < newscores[bc]:
                    bc = i

            newpop.append(candidates[bc])

        pop = newpop

        #print("checkpoint%d:%f" % (checkpoint,time.time()))
        #checkpoint += 1

        if scores[0][0] < best:
            best = scores[0][0]
            best_v = scores[0][1]
            nobetter = 0
        else:
            nobetter = nobetter + 1

        if nobetter >= int(maxiter / 10):
            break

        if best < nv: #cannot optimize further
            break

    print("")

    return best,best_v
