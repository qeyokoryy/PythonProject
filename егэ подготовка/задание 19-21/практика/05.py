from math import *

def f(a,b,m): # a and b кол в кучах m - код хзодов до конца
    if a + b <= 72: return m%2==0
    if m==0: return 0

    h = [f(a - 3 , b, m-1), f(ceil(a/2) , b, m-1), f(a , b-3, m-1), f(a , ceil(b/2), m-1)]
    return any(h) if m % 2 != 0 else all(h)
    # return any(h) if m%2!=0 else any(h)

# print('19)', *[s for s in range(23,200) if f(50,s,2)])
print('20)', *[s for s in range(23,200) if f(50,s,3) and (not f(50,s,1))])
print('21)', *[s for s in range(23,200) if f(50,s,4) and (not f(50,s,2)) ])

# 19) 94
# 20) 51 100
# 21)  103
