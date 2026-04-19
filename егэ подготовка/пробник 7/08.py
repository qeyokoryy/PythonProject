def f(x,osn):
    s = ''
    while x>0:
        s = str(x%osn)+s
        x//=osn
    return s

for n in range(1,1000):
    n13 = f(n,13)


