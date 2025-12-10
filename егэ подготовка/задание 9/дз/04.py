f = open('04')

k = 0
for s in f:
    a = [int(x) for x in s.split()]
    if max(a) < sum(a)-max(a):
        if max(a) + min(a) == sum(a) - max(a) - min(a):
            k+=1
print(k)