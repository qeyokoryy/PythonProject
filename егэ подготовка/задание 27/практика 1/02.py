

clustersA = [[],   []]

for s in open('2A.txt'):
    x,y = map(float,s.split())
    if y > 10: clustersA[0].append([x,y])
    else: clustersA[1].append([x,y])


clustersB = [[], [], []]

for s in open('2B.txt'):
    x,y = map(float, s.split())
    if y > 10: clustersB[0].append([x,y])
    elif y < -5: clustersB[1].append([x,y])
    else: clustersB[2].append([x,y])

from math import *

def center(cl):

    best = []
    minsum = 10**15
    for dot in cl:
        summ = sum(dist(dot,dot1) for dot1 in cl)
        if summ < minsum:
            minsum = summ
            best = dot
    return best

centerA = [center(cl) for cl in clustersA]
pxA = sum(dot[0] for dot in centerA)/len(centerA) * 10000
pyA = sum(dot[1] for dot in centerA)/len(centerA) * 10000

centerB = [center(cl) for cl in clustersB]
pxB = sum(dot[0] for dot in centerB)/len(centerB)*10000
pyB = sum(dot[1] for dot in centerB)/len(centerB)*10000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))