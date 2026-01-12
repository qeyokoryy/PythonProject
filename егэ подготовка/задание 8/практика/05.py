from itertools import *
k = 0
for x in product(sorted('гранит'), repeat=6):
    s = ''.join(x)
    k+=1
    if k%2!=0 and s[0] not in 'аиг' and s.count('а')==1:
        print(k)
        break