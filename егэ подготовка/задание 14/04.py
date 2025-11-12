from string import *
alf = '0123456789' + ascii_lowercase

def perevod (x, osn):
    s = ''
    while x > 0:
        ost = x % osn
        s = alf[ost] + s
        x = x//osn
    return s

a = 12 **34 + 7 * 12 ** 26 -3 * 12 ** 16 + 2 * 12**5 + 552
a12 = perevod(a, 12)
print(len(set(a12)))# перевод множество и подсчет его длины
