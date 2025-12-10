f = open('04')

k=0
for s in f:
    k+=1
    a = [int(x) for x in s.split()]
    a2 = [x     for x in a     if a.count(x)==2]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a2)==4 and len(a1)==3:
        if sum(a2)//len(a2) < max(a1):
            print(k)
            break
