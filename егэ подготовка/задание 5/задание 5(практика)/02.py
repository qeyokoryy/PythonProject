for n in range(100, 1000):
    ns = str(n)
    x1 = int(ns[0]) + int(ns[1])
    x2 = int(ns[1]) + int(ns[2])

    minn = min(x1, x2)
    maxx = max(x1, x2)

    r = str(maxx) + str(minn)

    if r == '157':
        print(n)
        break

