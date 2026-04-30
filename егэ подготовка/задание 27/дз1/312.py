from math import *

clustersA = [[], []]
f1 = open('3_A.txt')
for s in f1:
    x, y = map(float, s.split())
    if y > 8:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

clustersB = [[], [], [], [], []]
f2 = open('3_B.txt')
for s in f2:
    x, y = map(float, s.split())
    if x > 12:
        clustersB[0].append([x, y])
    elif y > 14:
        clustersB[1].append([x, y])
    elif y > 10:
        clustersB[2].append([x, y])
    elif y > 6:
        clustersB[3].append([x, y])
    else:
        clustersB[4].append([x, y])


def center(kl):
    mini = 10 ** 20
    cords = []
    for p in kl:
        sm = 0
        for p1 in kl:
            sm += dist(p, p1)
        if sm < mini:
            mini = sm
            cords = p
    return cords


centersA = [center(kl) for kl in clustersA]
centersB = [center(kl) for kl in clustersB]

px1 = int(sum(p[0] for p in centersA) / 2 * 10000)
py1 = int(sum(p[1] for p in centersA) / 2 * 10000)

px2 = int(sum(p[0] for p in centersB) / 5 * 10000)
py2 = int(sum(p[1] for p in centersB) / 5 * 10000)

print(px1, py1)
print(px2, py2)