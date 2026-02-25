f = open('3')

ans = []
a = [int(x) for x in f]
sr = sum(a)/len(a)

for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if (x>sr or y > sr) and (x+y)%7==0:
        ans += [x+y]
print(len(ans), min(ans))