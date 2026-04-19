clustersA = [[],   []]

for s in open('1A.txt'):
    #s=s.replace(',' , '.') если не менял в файле запятые на точки
    x,y = map(float,s.split())

    if y > 3:  clustersA[0].append([x,y])
    else:   clustersA[1].append([x,y])

clustersB = [[], [], []]

for s in open('1B.txt'):
    x,y = map(float,s.split())
    if y < 3: clustersB[0].append([x,y])
    elif x> 5: clustersB[1].append([x,y])
    else: clustersB[2].append([x,y])

from math import *

def center(cl):
    best = []
    minsum = 10**15
    for dot in cl:
        summ = sum(dist (dot,dot1) for dot1 in cl)
        if summ < minsum:
            minsum = summ
            best = dot
    return best


centerA = [center(cl) for cl in clustersA]
centerB = [center(cl) for cl in clustersB]


pxA = sum(dot[0] for dot in centerA)/2 * 10000
pyA = sum(dot[1] for dot in centerA)/2 * 10000

pxB = sum(dot[0] for dot in centerA)/3 * 10000
pyB = sum(dot[1] for dot in centerA)/3 * 10000

print(int(pxA), int(pyA))
print(int(pxB), int(pyB))

