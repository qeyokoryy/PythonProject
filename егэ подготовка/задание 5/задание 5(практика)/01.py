for n in range(1000, 10000):
    ns = str(n)
    c1 = int(ns[0])#( число)
    c2 = int(ns[1])#( число)
    c3 = int(ns[2])#( число)
    c4 = int(ns[3])#( число)


    x1 = c1+c2 #( число)
    x2 = c3+c4 #( число)

    maxx = max(x1, x2)
    minn = min(x1, x2)

    r = str(maxx) + str(minn)#(строка)

    if r == '1412':
        print(n)




