def f(x, osn):
    s = ''
    while x > 0:
        s = str(x%osn)+s
        x//=osn
    return s
ans = []
for n in range(167, 100000):
    n3 = f(n,3)
    summa = sum(map(int, n3))
    if summa % 9==0:
        n3+='2'
    else:
        n3+=f(summa%9, 3)
    r = int(n3, 3)
    ans += [r]
print(min(ans))
