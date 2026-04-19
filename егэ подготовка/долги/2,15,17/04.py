def f(x,y):
    return (7*y + 5*x < 1000) or (x < y) or (a < x)

for a in range(1000, 0, -1):
    if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        break