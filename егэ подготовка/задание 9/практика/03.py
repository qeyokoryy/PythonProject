f = open('03')

k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a3 = [x      for x in a      if a.count(x)==3] # собираем тех, кто всссстретился 3раза
    a1 = [x      for x in a      if a.count(x)==1]# без повторов
    if len(a3)==3 and len(a1)==3:
        if sum(a3)**2 > sum(a1)**2:
            k+=1
print(k)
