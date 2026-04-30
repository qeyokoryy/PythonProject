clusterA = [[], []]
for s in open('5а.txt'):
    s = s.replace(',', '.')
    x,y = map(float,s.split())

    if y < 8: clusterA[0].append([x,y])
    else: clusterA[1].append([x,y])

clusterB = [[], [], [], [], []]
for s in open('5а.txt'):
    s = s.replace(',', '.')
    x,y = map(float, s.split())
    if x > 12:
        clusterB[0].append([x, y])
    elif y > 14:
        clusterB[1].append([x, y])
    elif y > 10:
        clusterB[2].append([x, y])
    elif y > 6:
        clusterB[3].append([x, y])
    else:
        clusterB[4].append([x, y])

from math import *

def center(cl):
    minsum = 10**20
    best = []
    for dot in cl:
        summ = sum(dist(dot, dot1) for dot1 in cl)
        if summ < minsum:
            minsum = summ
            best = dot
    return best
centerA = [center(cl) for cl in clusterA]
centerB = [center(cl) for cl in clusterB]

pxA = sum(dot[0] for dot in centerA)/len(centerA) * 10000
pyA = sum(dot[1] for dot in centerA)/len(centerA) * 10000

pxB = sum(dot[0] for dot in centerB)/len(centerB) * 10000
pyB = sum(dot[1] for dot in centerB)/len(centerB) * 10000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))
