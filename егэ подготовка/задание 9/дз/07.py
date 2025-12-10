f = open('07')



for s in f:
    a = [int(x) for x in s.split()]
    if sorted(a)[::-1] == a: # в количестве убывания
        if (max(a)+min(a))//2 > (sum(a)-max(a)-min(a))//len(a):

            print(sum(a))
            break
