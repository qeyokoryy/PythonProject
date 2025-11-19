from string import *
alf = digits + ascii_lowercase
def f (x, osn):
    s = ''
    while x > 0:
        ost = x % osn
        s = alf[ost] + s
        x //= osn
    return s

a = 3 ** 72 + 6 * 3 ** 50 - 7 * 3 ** 26 + 2 * 3**15 + 155
a9 = f(a, 9)
print(len(set(a9)))
print(a9)

