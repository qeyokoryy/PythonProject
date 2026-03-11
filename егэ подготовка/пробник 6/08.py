from itertools import *
k = 0
for x in product(sorted('кодим'), repeat=5):
    s = ''.join(x)
    k += 1
    if s.count('м')==2 and ('мм' not  in s):


        print(k)