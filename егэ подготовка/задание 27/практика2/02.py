clusterA = [[],[]]
for s in open('2A.txt'):
    s = s.replace(',','.')
    x,y = map(float, s.split())
    if y < 15: clusterA[0].append([x,y])
    else: clusterA[1].append([x,y])

clusterB = [[],[],[]]

for s in open('2B.txt'):
    s = s.replace(',','.')
    x,y = map(float, s.split())
    if 0<x<30:
        if x < 10: clusterB[0].append([x,y])
        elif x < 20: clusterB[1].append([x,y])
        else: clusterB[2].append([x,y])

from math import *
def center(cl):
    minsumm = 10 ** 15
    best = []
    for dot in cl:
        summa = sum(dist(dot,dot1) for dot1 in cl)
        if summa < minsumm:
            minsumm = summa
            best = dot
    return best

centerA = [center(cl) for cl in clusterA]
px = (centerA[0][0] + centerA[1][0]) * 10000
py = (centerA[0][1] + centerA[1][1]) * 10000
print(abs(int(px)), abs(int(py)))


centerB = [center(cl)for cl in clusterB]
ddd = [dist(centerB[0], centerB[1]),
       dist(centerB[1], centerB[2]),
       dist(centerB[0], centerB[2])]

q1 = int(min(ddd) * 10000)
q2 =  int(max(ddd) * 10000)

print(q1,q2)