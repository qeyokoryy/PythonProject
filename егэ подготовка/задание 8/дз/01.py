from itertools import *
k = 0
for x in product(sorted('лемур'), repeat=4):
    s = ''.join(x)
    k+=1
    if s[0] == 'л':
        print(k)
        break
