from math import *
for n in range(1000,0,-1):
    i = ceil(log2(n)) #бит на пиксель

    pic1 = 486 * 720 * i
    pic2 = pic1 * 0.85
    if pic2 <= 80 * 8 * 1024:
        print(n)
        break