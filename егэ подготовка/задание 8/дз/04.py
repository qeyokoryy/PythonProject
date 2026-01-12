from itertools import *
k =0
for x in product(sorted('egland'), repeat=7):
    s = ''.join(x)
    k+=1
    if s == 'egeland':
        print(k,s)
