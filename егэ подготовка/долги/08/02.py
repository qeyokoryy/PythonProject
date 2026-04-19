from itertools import *
k = 0

for x in set(product('святослав', repeat=7)):
    s = ''.join(x)
    glas = s.count('я') + s.count('о') + s.count('а')
    sogl = s.count('с') + s.count('в') + s.count('т') + s.count('л')
    if glas > sogl:
        k+=1
print(k)

