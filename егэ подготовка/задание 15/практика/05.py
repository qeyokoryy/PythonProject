def f(x):
    return (x&a!=0) <= ((x&14==0) <=(x&75!=0))

for a in range(1000,0,-1):
    if all(f(x) for x in range(1,1000)):
        print(a)
        break