from  itertools import *
k = 0
for x in set(permutations('амфибрахий')):
    s = ''.join(x)
    if s[4:6]=='бр':
        k+=1
print(k,s)