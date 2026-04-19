def f(x):
    return (120%a==0) and ((not(x%a==0)) and (x%18==0)) <= ((not(x%24==0)))
for a in range(1000,0,-1):
    if all(f(x) for x in range(1,1000)):
        print(a)
        break





