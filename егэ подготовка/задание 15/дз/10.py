
P = {2,4,6,8,10,12,14,16,18,20}
Q = {5,10,15,20,25,30,35,40,45,50}

a = set(range(1,1000))

for x in range(1000):
    if not(((x in a) <= (x in P)) and ((x in Q) <= (x not in a))):
        a.remove(x)
print(len(a))
print(a)