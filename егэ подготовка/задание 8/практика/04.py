from itertools import *
k = 0
for x in product(sorted('строка'), repeat=5):
    s = ''.join(x)
    k += 1
    if k%2!=0 and s[0] not in 'ал' and s.count('с')==1:

        print(k)


