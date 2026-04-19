from itertools import *

tab = '45 357 267 16 126 345 23'.split()
pic = 'аб ад бв вг де ек бд ве гк'.split()
print(*range(1,9))

for var in permutations('абвгдек'):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic):
        print(*var)