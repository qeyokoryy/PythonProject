from itertools import permutations

tab = '235 134 124567 23 137 37 356'.split()
pic = 'da db dc de df dg fb be ec ca ag'.split()

print(*range(1,9))

for var in permutations('abcdefg'):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic):
        print(*var)