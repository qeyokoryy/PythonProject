def f(x):
    return (x&a!=0) <= (((x&17==0) and (x&5==0)) <=(x&3!=0))

for a in range(10000,0,-1):
    if all(f(x) for x in range(1,10000)):
        print(a)
        break