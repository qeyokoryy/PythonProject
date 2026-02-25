for n in range(1, 1000000):
    def f(n):
        return sum(map(int, n))



    cc = f'{n:b}'

    if cc.count('1') % 2 == 0:
        cc2 = '1' + cc + '00'
    else:
        cc2 = '10' + cc + '1'

        r = int(cc2, 2)

        if r == 21:
            print(n)







