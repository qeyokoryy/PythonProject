from itertools import *

def fun(x,y,z,w):
    return not ((((not w)<=(not y)) <= (not z)) <= x)

for a,b,c,d,e in product([0,1], repeat=5):
    table = ((a,b,1,0,1),
             (c,1,d,1,1,),
             (0,1,e,0,0)

        )

    if len(table)== len(set(table)):

        for p in permutations('xyzw'):

            if all(fun(**dict(zip(p,line))) == line[-1] for line in table):

                print(*p)
