f = open('09')

k = 0

for s in f:
    a = [int(x) for x in s.split()]
    a2 = [x for x in a if a.count(x)==1]

    if len(a2)==3  :


        k+=1
        print(sum(a2), a2)