for n in range(100, 1000):
    s = str(n)
    x1 = int(s[0]) * int(s[1])
    x2 = int(s[1]) * int(s[2])

    maxx = max(x1, x2)
    minn = min(x1, x2)
    r = str(minn) + str(maxx)

    if r == '621':
        print(n)

