def fun(x,y,w,z):
    return (not ((w or (not y)) and x)) or (y==z)

from itertools import *

for a,b,c,d in product([0,1], repeat=4):
    table = ((0,1,a,0,0),
             (1,1,0,b,0),
             (c,1,d,0,0)


    )
    if len(table)==len(set(table)):
        for p in permutations('xywz'):
            if all(fun(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)