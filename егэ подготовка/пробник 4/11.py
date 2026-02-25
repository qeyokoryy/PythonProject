from math import *
n =  10 + 256
i = ceil(log2(n))

idd = ceil(73*i/8)

ans = 29696 * idd /1024

print(ans)