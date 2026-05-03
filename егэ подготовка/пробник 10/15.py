m = list(range(32,69))
n = list(range(54,77))
a = []
for x in range(100):
    if ((not((x in m) or (x in n))) == (not (x  in a)))==False:
        a.append(x)
print(a[-1] - a[0])
print(a)
