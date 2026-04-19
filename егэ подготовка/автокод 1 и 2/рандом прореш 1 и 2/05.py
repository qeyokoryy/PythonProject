from itertools import *

tab = '57 67 5 567 1347 247 12456'.split()
pic = 'аб бв бг бд вд гд де дк гк ек '.split()

print(*range(1,9))

for var in permutations('абвгдек'):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic):
        print(*var)