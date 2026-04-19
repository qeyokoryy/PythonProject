from itertools import *

tab = '235 13 1245678 36 13 347 368 37'.split()

pic = 'аб аг ав бг вг ге гд гз гж ез дж зж'.split()

print(*range(1,9))

for var in permutations('абвгдежз'):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic):
        print(*var)