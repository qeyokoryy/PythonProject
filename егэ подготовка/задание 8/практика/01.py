from itertools import *
k = 0
for x in product('аоу', repeat=4):
    s = ''.join(x)
    k+=1
    if s[0] == 'у':
        print(k)
        break
