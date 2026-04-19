from math import *
for l in range(1000,0,-1):
    n = 10 + 52 + 1988
    i = ceil(log2(n))
    ser = ceil(i * l/8)
    if 1974 * ser <= 579 * 1024:
        print(l)
        break
