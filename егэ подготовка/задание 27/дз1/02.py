clusterA = [[], []]
for s in open('4_A.txt'):
    x,y = map(float,s.split())
    if y < -1: clusterA[0].append([x,y])
    else: clusterA[1].append([x,y])

clusterB = [[], [], []]

for s in open('4_B.txt'):
    x,y = map(float,s.split())
    if x < -6: clusterB[0].append([x,y])
    elif y < -6: clusterB[1].append([x,y])
    else: clusterB[2].append([x,y])

from math import *

def center(cl):
    minsum = 10**15
    best = []
    for dot in cl:
        summ = sum(dist(dot,dot1) for dot1 in cl)
        if summ < minsum:
            minsum = summ
            best = dot
    return best


centerA = [center(cl) for cl in clusterA]
pxA = sum(dot[0] for dot in centerA)/len(centerA) * 10000
pyA = sum(dot[1] for dot in centerA)/len(centerA) * 10000

centerB = [center(cl) for cl in clusterB]
pxB = sum(dot[0] for dot in centerB)/ len(centerB) * 10000
pyB = sum(dot[1] for dot in centerB)/len(centerB) * 10000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))

