f = open('02')

k = 0
for s in f:
    k+=1 # номера строк
    a = [int(x) for x in s.split()]
    if max(a) < sum(a) - max(a):
        if max(a) + min(a) == sum(a) - max(a) - min(a):
            print(k)

