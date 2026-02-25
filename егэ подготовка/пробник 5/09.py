f = open('09')

k = 0

for s in f:
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==1]
    a2 = [x for x in a if a.count(x)==8]
    k+=1

    if len(a1)==8 or len(a2)==1:
        if sum(a1) ** 2 > sum(a2)**2:
            if sum(a)%2!=0:

                print(k)
