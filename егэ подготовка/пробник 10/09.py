# f = open('09')
# k = 0
#
# for s in f:
#     k += 1
#     a  = [int(x) for x in s.split()]
#     a1 = [x for x in a if a.count(x)==1]
#     a2 = [x for x in a if a.count(x) >= 2]
#     summa1 = sum(a1)
#     summa2 = sum(a2)
#     if len(a1)==0 or len(a2)==0:
#         continue
#
#     if summa2 **2 > summa1 ** 2:
#         continue
#     if sum(a)%2==0:
#         continue
#     print(k)
#

f = open('09')
k = 0

for s in f:
    k += 1
    a  = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==1]
    a2 = [x for x in a if a.count(x) >= 2]
    summa1 = sum(a1)
    summa2 = sum(a2)
    if len(a1)>0 and len(a2)>0:


        if summa2 **2 > summa1 ** 2:

            if sum(a)%2==1:

                 print(k)



