from string import *
alf = digits + ascii_lowercase
def f(x, osn):
    s = ''
    while x > 0:
        ost = x%osn
        s = alf[ost] + s
        x//=osn
    return s
max0 = 0
for x in range(1, 3001):
    a = 4 **210 + 4**110 - x
    a4 = f(a, 4)
    k0 = a4.count('0')
    max0 = max(max0, k0)
for x in range(1, 3001):
    a = 4**210 + 4**110 - x
    a4 = f(a, 4)
    if a4.count('0') == max0:
        print(x)
        break
