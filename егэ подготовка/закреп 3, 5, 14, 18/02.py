from string import *
alf = digits + ascii_lowercase
def f(x, osn):
    s = ''
    while x > 0:
        ost = x%osn
        s = alf[ost] + s
        x //= osn
    return s
maxx = 0
for x in range(1, 2006):
    a = 5**150 + 5 **98 - x
    a5 = f(a, 5)
    maxx = max(maxx, a5.count('0'))
for x in range(2005, 0, -1):
    a = 5**150 + 5 **98 - x
    a5 = f(a, 5)
    if a5.count('0') ==maxx:
        print(x)
        break
