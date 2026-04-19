def f(x):
    return ((x & 117) != 0 and (x & 91) == 0) <= ((x & a) != 0)

for a in range(1,10000):
    if all(f(x) for x in range(1,10001)):
        print(a)
        break