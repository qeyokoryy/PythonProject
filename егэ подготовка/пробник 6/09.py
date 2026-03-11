f = open('09')

k = 0

for s in f:
    a = [int(x) for x in s.split()]
    a1 = [ x for x in a if a.count(x)==3]
    a2 = [x for x in a if a.count(x)==2]
    a3 = [x for x in a if a.count(x)==1]

    if len(a1) == 1 and len(a2)==1 and len(a3)==2:
        suma1a2 = a1[0] + a2[0]
        suma3 = sum(a3)
        if suma1a2 >= suma3:
            k+=1
print(k)

