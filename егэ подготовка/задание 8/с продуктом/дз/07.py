from itertools import *
k=0
for x in product('масло', repeat=6):
    s = ''.join(x)
    if s.count('с')==1 and s[0] not in 'ао' and s[-1] not in 'мсл':
        k+=1
print(k)