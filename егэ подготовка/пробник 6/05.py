ans = []
for n in range(1, 10000):
    n2 = f'{n:b}'

    if n2.count('0')%2==0:
        n2 = '1' + n2 +'1'

    else:
        n2 = '10' + n2

    r = int(n2, 2)



    if r < 100:
         ans+=[r]

print(max(ans), ans)

