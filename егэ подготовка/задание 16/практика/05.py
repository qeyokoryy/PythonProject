# from functools import *
# @lru_cache(None)
# def f(n):
#     if n<=5: return 1
#     if n > 5: return n + f(n-2)
# for i in range(3000):
#     f(i)
# print(f(2126)-f(2122))

from sys import *
setrecursionlimit(10000)
def f(n):
    if n <=5: return 1
    return n + f(n-2)
print(f(2126)-f(2122))

