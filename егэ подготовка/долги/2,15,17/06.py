p = list(range(25,241))
q = list(range(175,301))
r = list(range(270,341))

a = []

for x in range(-1000,1000):
    if not(((x in q) <= (x in p)) or (( (x not in a) <= (x in r)))):
        a.append(x)
print(len(a))
print(a)
print(a[-1]-a[0]+2)
