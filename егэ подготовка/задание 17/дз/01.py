f = open('1')

ans = []
a = [int(x) for x in f]


for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    minn = min(x, y)
    if (x<0  or y < 0) and (x+y > 0) and (x+y)%abs(minn)==0:
        ans +=  [x+y]
print(len(ans), max(ans))