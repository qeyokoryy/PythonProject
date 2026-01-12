from itertools import *
k=0
for x in product('игорь', repeat=8):
    s = ''.join(x)
    if s.count('о')==1 and s.count('ь')==1 and s[0]!='ь' :
        k+=1
        print(k)