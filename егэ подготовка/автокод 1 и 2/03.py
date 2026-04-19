from itertools import permutations

tab = '47 357 567 16 236 345 123'.split()

pic = 'ec eg ef eb ga ad db bf fc cg'.split()

print(*range(1,9))

for var in permutations('abcdefg'):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic):
        print(*var)