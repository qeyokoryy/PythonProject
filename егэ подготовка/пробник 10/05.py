def f(x,osn):
    s = ''
    while x>0:
        ost  = x%osn
        s = str(ost) + s
        x //= osn
    return s
max_r = 0
ans_n = 0

for n in range(1, 100000):
    n5 = f(n,5)
    if n5[-1]=='0':
        n5= n5.replace('1','x').replace('4','1').replace('x','4')

        n5 = '33' + n5
    else:

        n5 = '3' + n5[1:] + '42'

    r = int(n5,5)
    if r < 1922:
        max_r = r
        ans_n = n


print(ans_n, max_r)


