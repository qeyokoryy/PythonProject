def f(x,y):
    return not((x<7) or (y>=5*x + a - 60) or (x>=36) or (y<256))

for a in range(1000,-1,-1):
    if (all(f(x,y) for x in range(1, 1000) for y in range(1, 1000)))==0:
        print(a)
        break