from math import *
for x in range(10000,0,-1):
    n = 10 + 52 + x
    i = ceil(log2(n))
    ser = ceil(i * 40/8)
    if ser * 1000 <= 60 * 1024:
        print(x)
        break
