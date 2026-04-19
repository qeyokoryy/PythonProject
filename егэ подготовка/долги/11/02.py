from math import *

for n in range(1, 10000):
    i = ceil(log2(n))
    ser = (i * 248 / 8)
    if 75600 * ser > 16 * 1024 * 1024:
        print(n)
        break