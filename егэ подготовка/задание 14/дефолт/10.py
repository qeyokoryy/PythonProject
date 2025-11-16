def p (x, osn):
    s = ''
    while x > 0:
        ost = x%osn
        s = str(ost) + s
        x = x // osn
    return s

max0 = 0

for x  in range(1,2031):

    a = 7**170 + 7 ** 100 - x
    a7 = p(a, 7)
    k0 = a7.count('0')
    max0 = max(max0,k0)

for x  in range(2031, 0, -1):

    a = 7**170 + 7 ** 100 - x
    a7 = p(a, 7)
    k0 = a7.count('0')
    max0 = max(max0,k0)
    if k0==max0:
        print(x)
        break



