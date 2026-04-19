from itertools import *


pic = 'ah ab ad bc ce ef ed dg gf bh'.split()
tab = ' 34 67 148 135 47 28 258 367'.split()

print(*range(1,9))

for var in permutations('abcdefgh'):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic):
        print(*var)