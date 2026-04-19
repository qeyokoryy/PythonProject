p = list(range(43,50))
q = list(range(44,54))
a = []
for x in range(1000):
    if  (((x in a) <=(x in p)) or (x in q))==False:
        a.append(x)
print(a)
