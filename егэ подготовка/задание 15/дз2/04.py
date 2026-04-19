p = list(range(15,41))
q = list(range(21,64))

a  = []

for x in range(100):
    if ((x in p) <= (((x in q) and (x not in a)) <= (x not in p)))==False:
        a.append(x)
print(a[-1] - a[0])
print(a)