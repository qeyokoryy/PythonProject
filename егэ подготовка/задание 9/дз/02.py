f = open('02')

k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==2]
    a2 = [x for x in a if a.count(x) == 1]
    if max(a) < sum(a)-max(a):
        if len(a1)==2 and len(a2) == 2:
            k+=1
print(k)
