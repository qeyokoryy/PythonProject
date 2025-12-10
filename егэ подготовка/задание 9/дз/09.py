f = open('09')

k = 0

for s in f:
    a = [int(x) for x in s.split()]
    if (len(a) == len(set(a))) + (2 * (min(a) + max(a)) <= 3 * (sum(a) - min(a) - max(a))) == 1:
        k+=1

print(k)