for n in range(100, 1000):
    s = str(n)
    x1 = int(s[0]) + 4
    x2 = int(s[1]) + 8
    x3 = int(s[2]) + 6

    a = [x1, x2, x3]
    a = sorted(a)

    r = str(a[2])+ str(a[1]) + str(a[0])
    if r == '13107':
        print(n)

