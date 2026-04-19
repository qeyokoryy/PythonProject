from math import *

n = 10 + 4080
i  = ceil(log2(n))

id = ceil(i * 256/8) # в байтах

ans = id * 65536 /1024/1024
print(ans)



