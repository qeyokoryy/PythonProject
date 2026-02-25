def f(x):
    return (a%25==0) and (((x%24==0) and (x%75==0))<= (x%a==0))
k = 0
for a in range(1, 1000):
    if all(f(x) for x in range(1,1000)):
        k+=1
print(k)