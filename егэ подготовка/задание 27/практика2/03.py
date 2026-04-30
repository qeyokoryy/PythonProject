clusterA = [[],[]]
for s in open('3A.txt'):
    s = s.replace(',', '.')
    x,y = map(float, s.split())
    if y < 10: clusterA[0].append([x,y])
    else: clusterA[1].append([x,y])

clusterB = [[],[],[]]

for s in open('3B.txt'):
    s = s.replace(',','.')
    x,y = map(float,s.split())
    if 10 < x < 30:
        if x > 22: clusterB[0].append([x,y])
        elif y > 15: clusterB[1].append([x,y])
        else: clusterB[2].append([x,y])

from math import dist
def center(cl):
    minsum = 10 * 15
    best = []
    for dot in cl:
        summa = sum(dist(dot,dot1) for dot1 in cl)
        if summa < minsum:
            minsum = summa
            best = dot
    return best


centerA = [center(cl) for cl in clusterA]
px = abs(int(sum(p[0] for p in centerA) * 10000))
py = abs(int(sum(p[1] for p in centerA) * 10000))
print( px, py)

ddd =   [dist(p1,p2) for p1 in clusterB[0] for p2 in clusterB[1]] + \
        [dist(p1,p2) for p1 in clusterB[1] for p2 in clusterB[2]]+ \
        [dist(p1,p2) for p1 in clusterB[0] for p2 in clusterB[2]]

q1 = int(min(ddd) * 10000)
q2 = int(max(ddd) * 10000)
print(q1, q2)
