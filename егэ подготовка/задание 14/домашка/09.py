from string import *
alf = digits + ascii_lowercase
def f(x, osn):
    s = ''
    while x > 0:
        ost = x%osn
        s = alf[ost] + s
        x//=osn
    return s

for x in range(2005, 0, -1):
    a = 4 ** 163 * 5 +12 ** 62 - x
    a5 = f(a, 5)
    if a5.count('1') < a5.count('4'):
        print(x)
        break

