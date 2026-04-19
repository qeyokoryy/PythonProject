def f(x):
    return (x & a !=0) <= ((x&698==0) <= (x&321!=0))

for a in range(10000, 0,-1):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break