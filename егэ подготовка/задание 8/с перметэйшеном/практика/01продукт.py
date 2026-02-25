from itertools import *
k = 0
for x in product(sorted('парус'), repeat=5):
    s = ''.join(x)
    k+=1
    if s.count('у')<=1 and 'аа' not in s:
        print(k)
        break