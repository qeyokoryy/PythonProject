def fun(x,y,z,w):
    return (w and y) or ((x<=w) == (y<=z))

from itertools import *
for a,b,c,d,e,f in product([0,1], repeat=6):

    table = ((a,b,c,1,0),
             (1,d,e,1,0),
             (1,f,1,1,0)

         )
    if  len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(fun(**dict(zip(p,line))) == line[-1] for line in table ):
                print(*p)