ans = []
for n in range(1, 13):
    n2 = f'{n:b}'
    if n2.count('1') % 2 == 0:
        n2 = '10' + n2
    else:
        n2 = '1' + n2 + '01'

        r = int(n2, 2)
        ans.append(r)

        print(max(ans))
