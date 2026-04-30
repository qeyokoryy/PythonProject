clusterA = [[], []]
for s in open('1_A.txt'):
    x,y = map(float,s.split())
    if y < -1: clusterA[0].append([x,y])
    else: clusterA[1].append([x,y])

clusterB = [[], [], []]
for s in open('1_B.txt'):
    x,y = map(float,s.split())
    if x < -6: clusterB[0].append([x,y])
    elif y < -7: clusterB[1].append([x,y])
    else: clusterB[2].append([x,y])

from math import *

def center(cl):
    best = []
    minsum = 10**20
    for dot in cl:
        summ = sum(dist(dot,dot1) for dot1 in cl)
        if summ < minsum:
            minsum = summ
            best = dot
    return best

centerA = [center(cl) for cl in clusterA]
centerB = [center(cl) for cl in clusterB]

pxA = abs(sum(dot[0] for dot in centerA)/len(centerA)* 10000)
pyA = abs(sum(dot[1] for dot in centerA)/len(centerA) * 10000)

print(int(pxA), int(pyA))

pyB = abs(sum(dot[0] for dot in centerB)/len(centerB) *10000)
pxB = abs(sum(dot[1] for dot in centerB)/len(centerB) * 10000)

print(int(pyB), int(pxB) )