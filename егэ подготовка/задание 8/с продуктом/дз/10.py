from itertools import *
k=0
for x in product(set('никита'), repeat=5):
    s = ''.join(x)
    if s.count('к')<=1 and s[0]!='к' and s[-1]!='к' and 'нк' not in s and 'кн' not in s:
        k+=1
print(k)