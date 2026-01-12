from itertools import *
k=0
c = 0
for x in product(sorted('фаворит'), repeat=6):
    s = ''.join(x)
    k += 1
    if k%2==0 and s[0]!='о' and s.count('р')==2:
        c +=1

        print(c)