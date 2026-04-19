from itertools import *

def fun(x,y,w,z):
    return not (z or (w<= y)) or (x<=z)

for a,b,c,d,e,f,g in product([0,1], repeat=7):
    table = ((0,a,0,b,0),
             (c,0,1,d,0),
             (e,1,f,g,0)


    )
    if len(table)==len(set(table)):
        for p in permutations('xywz'):
            if all(fun(**dict(zip(p,line))) == line[-1] for line in table):
                print(*p)