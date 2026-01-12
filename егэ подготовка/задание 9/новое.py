f = open('новое')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a2 = [x for x in a if a.count(x)==2]
    aun = sorted(a)
    if len(a2)==6 and aun[0]**2 + aun[2]**2 == aun[-1]**2:
        k+=1
print(k)
