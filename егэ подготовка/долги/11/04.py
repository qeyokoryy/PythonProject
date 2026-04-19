from math import *
for n in range(100000, 0, -1):
    i = ceil(log2(n))
    ser = ceil(23 * i/8)
    if ser * 500000 <= 21 * 1024 * 1024:
        print(n)
        break