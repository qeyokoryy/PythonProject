from itertools import *
k = 0
for x in product(sorted('жюяузчдоф'), repeat = 6):
    s = ''.join(x)
    k+=1
    if k%2!=0 and s[0]!='у' and s[-1]!='у' and 'юю' in s:
        print(k,s)
        break