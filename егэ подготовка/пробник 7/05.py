def f(x,osn):
    s = ''
    while x>0:
        s = str(x%osn)+s
        x//=osn
    return s

for n in range(1000,0,-1):
    n7 = f(n,7)
    summa = sum(map(int,n7))
    if summa%2==0: n7+='555'
    else: n7 = '33' + n7 + '6'

    r = int(n7, 7)
    if r < 12717:
        print(n)
        break
