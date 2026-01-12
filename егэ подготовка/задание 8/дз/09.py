from itertools import *
k =0
for x in product('калий',repeat=6):
    s = ''.join(x)
    if s.count('й')<=1 and s[0]!='й' and s[-1]!='й' and 'ий'not in s and 'йи' not in s:
        k+=1
        print(k)