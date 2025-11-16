from string import *
alf = digits + ascii_lowercase

def f(x, osn):
    s = ''
    while x > 0:
        s = alf[x%osn]+s
        x//=osn
    return s
ans = []
for n in range(12, 100000):
    n12 = f(n, 12)
    if n % 12 == 0:
        n12+= n12[-2::]
    else:
        ost = (n%12) * 9
        n12 += f(ost,12)
    r = int(n12, 12)
    if r > 300:
        ans+=[r]
print(min(ans))