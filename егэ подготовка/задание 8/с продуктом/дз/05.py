from itertools import *
k=0
for x in product(sorted('гондубш'), repeat=6):
    s = ''.join(x)
    k+=1
    if k%2!=0 and s[0]!='б' and s.count('н')>=2 and s not in 'н' :
        print(k,s)
        break

