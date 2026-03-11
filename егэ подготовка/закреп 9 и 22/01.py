f = open('01')
k = 0

for s in f:
    a = [int(x) for x in s.split()]
    a1 =[x for x in a if a.count(3)]
    a2 = [x for x in a if a.count(3)]
    if len(a1)==1 and len(a2)==1:
