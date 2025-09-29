

l1 = len(input())
l2 = len(input())
l3 = len(input())

if l1 > l2 and l1 > l3:
    print(l1)
elif l2 > l3:
    print(l2)
else:
    print(l3)

#сокращение
l1 = len(input())
l2 = len(input())
l3 = len(input())

print(max(l1, l2, l3))