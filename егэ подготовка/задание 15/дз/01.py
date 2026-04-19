def f(x):
    return (not (x%7==0) and (x%13==0)) <= (x > a - 40)

for a in range(1000, 0, -1):
    if all (f(x) for x in range(1, 1000)):
        print(a)
        break