from string import *
alf = digits + ascii_lowercase

def f(x, osn):
    s = ''
    while x > 0:
        ost = x % osn
        s = alf[ost] + s
        x //= osn
    return s
a = 361 * 2349**84 - 89 ** 192 + 1953**481 * 4843**151

a9 = f(a, 9)
print(a9.count('5'))











