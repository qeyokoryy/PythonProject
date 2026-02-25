from itertools import *
k = 0

for x in product('арбуз', repeat=6):
    s = ''.join(x)
    if s.count('а')==3 and 'аа' in s and 'ааа' not in s:
        k+=1
print(k)
