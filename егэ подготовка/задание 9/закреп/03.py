f = open('03')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    chet = [x for x in a if x%2==0]
    if max(a) < sum(a)-max(a):
        if sum(chet) * 2 == sum(a):
            k+=1
print(k)
#13
