from string import  *
alf = digits + ascii_lowercase
def f(x, osn):
    s = ''
    while x > 0:
        ost = x%osn
        s = alf[ost] + s
        x //= osn
    return s
a = 5 * 216 ** 3031 + 4 * 36 **3042 - 3 * 6**3053 - 3064
a6 = f(a, 6)
print(sum(map(int, str(a6))))
print(a6)