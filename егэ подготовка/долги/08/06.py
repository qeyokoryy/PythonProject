from itertools import *
k = 0
for x in permutations('компьютер',9 ):
    s = ''.join(x)
    if s.count('к')==1 and s.count('о')==1 and s.count('м')==1 and s.count('п')==1 and s.count('ь')==1 and s.count('ю')==1 \
        and s.count('т')==1 and s.count('е')==1 and s.count('р')==1 and s[-2]=='е':
        if list(s[:4])==sorted(s[:4]):
            k+=1
print(k)