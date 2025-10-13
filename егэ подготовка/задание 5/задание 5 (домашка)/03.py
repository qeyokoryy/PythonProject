for n in range(1000, 10000):
    s = str(n)
    x1 = int(s[0])*int(s[1])
    x2 = int(s[2])*int(s[3])

    a = [x1, x2]
    a = sorted(a)

    r = str(a[0]) + str(a[1])
    if r == '5472':
        print(n)
        break
