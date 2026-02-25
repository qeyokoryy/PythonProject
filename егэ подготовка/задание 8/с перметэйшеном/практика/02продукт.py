from itertools import *

k = 0

for x in product('моль', repeat=5):
    s = ''.join(x)

    if s.count('ь')==s.count('мь')+s.count('ль'):
        k+=1
print(k)