from itertools import *
k=0
for x in product(sorted('азнс'), repeat=5):
    s = ''.join(x)
    k+=1
    if s == 'сазан' or s == 'занас':
        print(k,s)
print(787-292+1)
