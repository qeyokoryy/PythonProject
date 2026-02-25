f = open('2.txt')

ans = []
a = [int(x) for x in f]

sr = sum(a)//len(a)
for i in range(len(a)-2):
    x = a[i]
    y = a[i+1]
    z = a[i+2]
    if ((x < sr) or (y < sr) or (z < sr)) and ((x%3==0) or (y%3==0) or (z%3==0)):
        ans += [x+y+z]
print(len(ans), max(ans))