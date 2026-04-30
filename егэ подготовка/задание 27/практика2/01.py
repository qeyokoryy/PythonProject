clusterA = [[],[]]
for s in open('1A.txt'):
    s = s.replace(',', '.')
    x,y = map(float, s.split())
    if y < 10: clusterA[0].append([x,y])
    else: clusterA[1].append([x,y])

clusterB = [[], [], []]
for s in open('1B.txt'):
    s = s.replace(',', '.')
    x, y = map(float, s.split())
    if 0<x<20: #убираем аномалии
        if y < 10: clusterB[0].append([x,y])
        elif y > 21: clusterB[1].append([x,y])
        else: clusterB[2].append([x,y])

from math import *
def center(cl):
    minsum = 10 ** 15
    best = []
    for dot in cl:
        summa = sum(dist(dot,dot1) for dot1 in cl)
        if summa < minsum:
            minsum = summa
            best = dot
    return best

centersA = [center(cl) for cl in clusterA]
pxA = abs(int(max(dot[0] for dot in centersA) * 10000))
pyA = abs(int(max(dot[1] for dot in centersA) * 10000))
print(pxA, pyA)

clusterB.sort(key=len)# сортим по количеству точек
centersB = [center(cl) for cl in clusterB]
qx = (centersB[2][0] - centersB[0][0])* 10000
qy = (centersB[2][1] - centersB[0][1]) * 10000
print(abs(int(qx)), abs(int(qy)))