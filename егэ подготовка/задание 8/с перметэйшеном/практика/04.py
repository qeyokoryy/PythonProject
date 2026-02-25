from itertools import *

k = 0

for x in permutations('апельсин', 7):
    s = ''.join(x)
    for c in 'плсн':
        s = s.replace(c, 'н')

    if 'ь' in s:
        if 'ньн' in s:
            k+=1
    else: k+=1
print(k)