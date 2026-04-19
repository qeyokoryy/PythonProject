from itertools import *

tab = '2345 1 147 1367 1 4 34'.split()

pic = 'ав аг ад бв вг гк гд ев'.split()

print(*range(1,9))

for var in permutations('абвгдек'):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic):
        print(*var)