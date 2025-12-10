f = open('06')

k = 0

for s in f:
    k+=1
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==2]
    a2 = [x for x in a if a.count(x)==1]
    if len(a1)==2 and len(a2)==4:
        if a1[0] >= sum(a2)//len(a2):
            print(k)