for n in range(1, 10000):
    n2 = f'{n:b}'
    if n2.count('1')%2 == 0:
        n2+='0'
        n2 = '10' + n2[2:]
    else:
        n2+='1'
        n2 = '11' + n2[2:]

        r = int(n2, 2)
    if r > 50:
        print(n)
        break


