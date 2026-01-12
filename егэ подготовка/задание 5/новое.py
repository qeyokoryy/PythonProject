def f(x, osn):
    s = ''
    while x>0:
        ost = x%osn
        s = str(ost)+s
        x//=osn
    return s

ans = []
for n in range(1, 100000):
    n3 = f(n,3)
    if n%3==0:
        n3+=n3[-2:]
    else:
        summa = sum(map(int,n3))
        n3+= f(summa*3,3)
    r = int(n3,3)
    if r > 208 and r%2!=0:
        ans+=[r]
print(min(ans))