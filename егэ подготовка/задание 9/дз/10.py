f = open('10')



for s in f:

    a = [int(x) for x in s.split()]
    chet = [x for x in a if  x%2==0]
    nechet = [x for x in a if  x%2!=0]
    if sum(chet) ** 2 > sum(nechet) ** 3:


        print(sum(a))

