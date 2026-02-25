from itertools import *
k = 0
for x in product('вьюга', repeat=6):
    s = ''.join(x)
    if 'юг'  in s:
        k+=1

        print(k, s)
