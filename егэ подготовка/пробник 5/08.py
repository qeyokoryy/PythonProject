from itertools import *
k = 0
for x in product('масло', repeat=6):
    s = ''.join(x)


    if s.count('а')==1 and s.count('о')==1:
        k += 1


print(k,s)
