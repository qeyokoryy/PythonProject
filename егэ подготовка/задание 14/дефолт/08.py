def p (x, osn):
    s = ''
    while x > 0:
        ost = x%osn
        s = str(ost) + s
        x = x//osn
    return s
for x in range(1, 3001):
    a = 9 **150 + 9 **30 -x
    a9 = p(a, 9)
    if a9.count('0')==122:
        print(x)
        break
