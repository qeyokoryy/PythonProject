f = open('4')


a = [int(x) for x in f]
ans = []

k32 = len([x for x in a if x %32==0] )

for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if (x<0 or y<0) and (x+y)<k32:
        ans += [x+y]
print(len(ans), max(ans))