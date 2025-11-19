from string import  *
alf = digits + ascii_lowercase
def f(x, osn):
    s = ''
    while x> 0:
        ost = x % osn
        s = alf[ost] + s
        x //= osn
    return s
a = 2 * 729 **1021 - 2 * 243 **1022 + 81 **1023 - 2 * 27**1024 - 1025
a3 = f(a, 3)
print(a3.count('0'))
