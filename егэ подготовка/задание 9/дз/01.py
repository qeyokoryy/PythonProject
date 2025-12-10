f = open('01')

k = 0

for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    if (a[0] + a[2])/2 <= a[1]:
        k+=1
print(k)