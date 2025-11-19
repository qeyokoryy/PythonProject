def f(x, osn):
    s = ''
    while x > 0:
        ost = x % osn
        s = str(ost )+ s
        x //= osn
    return s
for n in range(10000):
    ans = []
    n4 = f(n, 4)
    if n ==0:
        n4 = '0'
    if n%2 ==0:
        ml = int(n4[-1])*3
        n4 = '12' + n4 + f(ml, 4)
    else:
        n4 = '13' + n4 +'21'
    r = int(n4, 4)
    if r > 50:
        ans += [r]
print(min(ans))