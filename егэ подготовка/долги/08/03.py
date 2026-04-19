from itertools import *
k = 0
for x in permutations('варфолмей',6):
    s = ''.join(x)
    glas = s.count('а') + s.count("о") + s.count("е")
    sogl = 6 - glas
    if glas < sogl and 'аа' not in s and 'ао' not in s and 'ае' not in s \
            and 'оа' not in s and 'оо' not in s and 'ое' not in s \
            and 'еа' not in s and 'ео' not in s and 'ее' not in s:
        k += 1

print(k,s)
