from string import *
alf = digits + ascii_lowercase
def f(x, osn):
    s = ''
    while x > 0:
        ost = x%osn
        s = alf[ost] + s
        x//=osn
    return s
for x in range(2400, 0, -1):
    a = 7 * 9 ** 210 + 6 * 9 ** 110 - x
    a9 = f(a, 9)
    if a9.count('0')==100:
        print(x)
        break

