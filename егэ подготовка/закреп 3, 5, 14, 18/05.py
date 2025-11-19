k = 0
for n in range(1, 10000):

    n16 = f'{n:x}'
    if n16.count('b')%2==0:
        n16 = '1' + n16
    else:
        n16 += '1'
    r = int(n16, 16)
    if 10 <=r<=99:
        k+=1
print(k)

