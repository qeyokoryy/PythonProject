f = open('02')
k = 0
for s in f:
    k += 1
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==3]
    a2 = [x for x in a if a.count(x)==1]
    if len(a1)==3 and len(a2)==3:
        if max(a1) > sum(a2)/len(a2):

            print(k)
            #10493
