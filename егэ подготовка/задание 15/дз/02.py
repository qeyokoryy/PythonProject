def f(x):
    return (not x%a==0) <= ((x%14==0) <= (not (x%4==0)))

for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break