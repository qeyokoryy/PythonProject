def p (x, osn):
    s = ''
    while x > 0:
        ost = x%osn
        s = str(ost) + s
        x = x // osn
    return s

for x  in range(1,10000):

    a = 5**2026 + 7 * 5**1013 + 107 - x
    a6 = p(a, 6)
    if a6.count('5') == a6.count('0')+ 28:
        print(x)
        break
