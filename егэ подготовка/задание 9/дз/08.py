f = open('08')



for s in f:
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==2]
    a2 = [x for x in a if a.count(x) == 1]
    if len(a1)==4 and len(a2)==3:
        if a.count(max(a))==1:

            print(sum(a))
            break
