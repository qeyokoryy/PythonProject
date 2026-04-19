def f(x):

    return (x%a==0) or ((170 <= x <= 220) <= (not (x%24==0)))
k=0

for a in range(1, 10000):
    if all(f(x) for x in range(1,1000)):
        k+=1

print(k)