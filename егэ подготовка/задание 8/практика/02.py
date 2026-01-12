from itertools import *
k = 0

for x in product(sorted('порт'), repeat=5):
    s = ''.join(x)
    k+=1
    if s == 'топор' or s == 'ропот':
        print(k)
print(787-532+1)
#256
