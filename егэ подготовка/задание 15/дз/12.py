p = {2,4,9,10,15}
q = {3,8,9,10,20}
a = set()

for x in range(1, 1000):
    if  ( ((x not in p)==(x not in a)) <=((x in q)==(x in a)))==False:
        a.add(x)
print(len(a))
