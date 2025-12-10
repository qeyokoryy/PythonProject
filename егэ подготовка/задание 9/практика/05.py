f = open('05')

k = 0
for s in f:
    a=[int(x) for x in s.split()]
    a2 = [x for x in a if a.count(x)==2]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a2)==4 and len(a1)==2:
        if sum(set(a2)) > sum(a1):
            k+=1
print(k)

