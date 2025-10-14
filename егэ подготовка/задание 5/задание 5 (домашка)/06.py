for n in range(1, 10000):
    n2 = f'{n:b}'
    n2+=n2[-1:]
    if n2.count('1') % 2 == 0:
         n2+='0'
    else:
        n2+='1'
        if f'{n:b}'.count('1') % 2 == 0:
            n2+='1'
        else:
            n2+='0'

            r = int(n2, 2)
            if r > 90:
                print(n)
                break

