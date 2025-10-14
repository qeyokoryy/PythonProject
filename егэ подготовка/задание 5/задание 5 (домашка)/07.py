for n in range(99, 0, -1):
    n2 = f'{n:b}'
    k0 = n2.count('0')
    k1 = n2.count('1')
    if k0 == k1:             n2 +=n2[-1]
    elif k0<k1:              n2+='0'
    else:                    n2+='1'

    k0 = n2.count('0')
    k1 = n2.count('1')

    if k0 == k1:             n2 +=n2[-1]
    elif k0<k1:              n2+='0'
    else:                    n2+='1'

    k0 = n2.count('0')
    k1 = n2.count('1')

    if k0 == k1:             n2 +=n2[-1]
    elif k0<k1:              n2+='0'
    else:                    n2+='1'

    r = int(n2, 2)
    if r % 4 == 0 and r%8!=0:
        print(n)
        break






