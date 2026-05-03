from itertools import *

def fun(x,y,z,w):
    return (not(x<=y)) or ((not w) <= (not z)) or w
for a,b,c,d,e,f in product([0,1], repeat=6):
    table = {(a,1,0,1,0),
             (1,1,b,c,0),
             (d,e,f,1,0),


    }
    if len(table)==len(set(table)):
        for p in permutations('xyzw'):
            if all(fun(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)
                exit()