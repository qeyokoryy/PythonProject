from functools import *



@lru_cache(None)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1) + 1

for i in range(3304):
    f(i)
print(f(3003)//f(3300))

