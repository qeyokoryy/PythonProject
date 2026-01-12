from itertools import *
k =0
for x in product(sorted('компьютер'), repeat=6):
    s = ''.join(x)
    k+=1
    if k%2!=0 and s[0]!='ь' and s.count('к')==2:
        print(k)

