from itertools import *

def fun(x,y,z,w):
    return (not x) and (not y) or (y==z) or w

for a,b,c,d in product([0,1], repeat=4):
    table = {(a,b,1,c,0),
             (1,0,d,1,0),
             (0,0,1,1,0)


    }
    if len(table)==len(set(table)):
        for p in permutations('xyzw'):
            if all(fun(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)