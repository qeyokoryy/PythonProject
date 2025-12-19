f = open('01')

k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==1]
    if (a.count(max(a))==3 and len(a1)==5) or (a.count(max(a))==4 and len(a1)==4):
        if max(a1)+min(a1) <= sum(a1)-(max(a1)+min(a1)):
            k+=1
print(k)
