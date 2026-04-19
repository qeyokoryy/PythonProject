def f(x,y):
    return (353728 != 5*y + 11*x) or (a<x) or (a<y)

for a in range(1000,0,-1):
    if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        break