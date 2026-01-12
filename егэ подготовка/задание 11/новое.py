from math import *
for x in  range(100000, 0, -1):
    n = 33 * 2 + x
    i = ceil(log2(n))
    ser = ceil(21*i/8)
    if 1300 * ser <= 25 * 1024:
        print(x)
        break