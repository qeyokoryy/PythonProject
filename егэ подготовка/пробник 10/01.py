pic = '3567 37 126 57 146 135 124'.split()
pereb = 'ab af bg bc cd dg de eg ef gf'.split()
from itertools import *
print(*range(1,9))

for var in permutations('abcdefg'):
    if all(str(var.index(x)+1) in pic[var.index(y)] for x,y in pereb):
        print(*var)