f = open('06')


for s in f:
    a = [int(x) for x in s.split()]
    a3 =[x for x in a if a.count(x)==3]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a3)==3 and len(a1)==4:
      if sum(a1)/len(a1) <= a3[0]:
          print(sum(a))

#901
