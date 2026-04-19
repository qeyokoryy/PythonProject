def f(x):
    return ((x%6==0) <= (not(x%10==0))) or (x+a>112)
for a in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(a)
        break