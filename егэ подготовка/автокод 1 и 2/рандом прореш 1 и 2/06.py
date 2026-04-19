from itertools import *

tab = '2347 17 14 1356 4 4 12'.split()
pic = 'ав аг вб ве вг гд гк дк'.split()

print(*range(1,9))

for var in permutations('абвгдек'):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic):
        print(*var)
