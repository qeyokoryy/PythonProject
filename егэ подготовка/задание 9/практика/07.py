f = open('07')
k =0
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    if (a[-1]**2 > a[0]*a[1]*a[2]) or (a[1]-a[0]==a[2]-a[1]==a[3]-a[2]):
        k+=1
print(k)


