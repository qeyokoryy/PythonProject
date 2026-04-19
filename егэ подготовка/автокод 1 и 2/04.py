from itertools import *

def fun(x,y,z,w):
    return (not(x or y)) and (not w) or (not (z or w)) and y

for a,b,c,d,e,f,g,h in product([0,1], repeat=8):
    table = ((a,1,b,c,1),
             (d,e,1,f,1),
             (g,1,h,1,1) )

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(fun(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)