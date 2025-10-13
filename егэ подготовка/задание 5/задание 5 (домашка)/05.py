ans = []
for n in range(1, 10000):
    n2 = f'{n:b}'
    if n % 3 ==0:
        n2+=n2[-2:-1]
    else:
        n2 = '1' + n2 + '1'
        r = int(n2, 2)
        if r> 700:
            ans.append(r)
            print(min(ans))
            break
