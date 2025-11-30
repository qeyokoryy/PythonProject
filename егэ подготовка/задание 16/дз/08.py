from functools import lru_cache
@lru_cache(None)
def f(n):
    return g(n-1)+g(n-3)
@lru_cache(None)
def g(n):
    if n <= 9: return 3 * n
    return g(n-4)+2
for i in range(100000):
    f(i)
print(f(42999))