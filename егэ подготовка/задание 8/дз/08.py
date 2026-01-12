from itertools import *
k = 0
for x in product('вишня', repeat=6):
    s = ''.join(x)
    if s.count('в')<=1 and s[0]!='ш' and s[-1] not in 'ия':
        k+=1
print(k)