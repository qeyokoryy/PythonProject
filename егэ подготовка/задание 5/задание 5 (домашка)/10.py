ans = []
for n in range(1, 10000):
    s = f'{n:b}'
    if n % 3 == 0:
        s+=s[-1:]
    else:
        ost = n%3 * 3
        ost2 = f'{ost:b}'
        s+=ost2

        r = int(s, 2)
    if r > 195:

        ans.append(r)
        print(min(ans))
