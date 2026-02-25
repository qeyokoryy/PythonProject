from itertools import *
k=0

for x in set(permutations('светлана')):
    s = ''.join(x)

    if s[0]!=s[1]!=s[2]!=s[3]!=s[4]!=s[5]!=s[6]!=s[7]: #if 'аа' not in s:
        k+=1
print(k)