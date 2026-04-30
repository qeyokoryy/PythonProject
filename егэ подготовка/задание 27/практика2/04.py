clusterA = [[],[]]
for s in open('4A.txt'):
    s = s.replace(',', '.')
    x,y = map(float, s.split())
    if x >50: clusterA[0].append([x,y])
    else: clusterA[1].append([x,y])

clusterB = [[],[],[]]

for s in open('4B.txt'):
    s = s.replace(',','.')
    x,y = map(float,s.split())
    if 15 < x < 35:
        if y < 32: clusterB[0].append([x,y])
        elif y > 42: clusterB[1].append([x,y])
        else: clusterB[2].append([x,y])

from math import dist
def center(cl):
    minsum = 10 ** 15
    best = []
    for dot in cl:
        summa = sum(dist(dot,dot1) for dot1 in cl)
        if summa < minsum:
            minsum = summa
            best = dot
    return best



clusterA.sort(key=len)
centersA = [center(cl) for cl in clusterA]
p1 = (centersA[0][0] + centersA[0][1])*10000
p2 = (centersA[1][0] + centersA[1][1])*10000
print(abs(int(p1)), abs(int(p2)))

centerB = [center(cl) for cl in clusterB]
# print(dist(p,[0,0]) for p in centerB)
#38 51 44

qx = centerB[1][0] * 10000
qy = centerB[0][1] * 10000

print(abs(int(qx)), abs(int(qy)))
