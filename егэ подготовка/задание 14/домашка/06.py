from string import *
alf = digits + ascii_lowercase
def f (x, osn):
    s = ''
    while x > 0:
        ost = x % osn
        s = alf[ost] + s
        x //= osn
    return s
for x in range(1, 3001):
    a = 9 * 11**210 + 8 * 11 ** 150 - x
    a11 = f(x, 11)
    if a11.count('0')==60:
        print(x)
#не работает хз почему


