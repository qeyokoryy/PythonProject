from string import  *

alf = digits + ascii_lowercase

def f (x, osn):
    s = ''
    while x > 0:
        ost = x % osn
        s= alf[ost] + s
        x //= osn
    return s
a = 729 ** 8 - 3 ** 18 + 85
a9 = f(a, 9)
print(a9.count('0'))
