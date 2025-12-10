f = open('05')

k = 0

for s in f:
    k += 1
    a = [int(x) for x in s.split()]

    if (min(a)+max(a)) * 2 == (sum(a)-max(a)-min(a)) * 3:
        print(k)
