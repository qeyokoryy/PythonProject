from itertools import *

tab = '24 146 56 1267 36 23457 46'.split()
pic = 'аб ав бв вд ве вг де ге ек гк'.split()

print(*range(1,9))

for var in permutations('абвгдек'):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic ):
        print(*var)