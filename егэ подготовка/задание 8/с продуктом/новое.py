from itertools import *
k = 0

for x in product(sorted('победа'),repeat=6):
    s = ''.join(x)
    k += 1
    if k%2==0 and s[0]=='о' and len(set(s))==6:

        print(k)
