# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not (y <= w) or (x==z) or x) ==0:
#                     print(x,y,z,w)
#
#
#

ans = []
for n in range(1,10000):
    n2 = f'{n:b}'
    if n%2==0:
        n2 = '1'+n2 + str(n2.count('1')%2)
    else:
        n2 =   n2 + '0' + str(n2.count('1')%2)
    r = int(n2, 2)
    if r == 101:
        print(n)
        break

  #   if r> 100: ans+=[r]
  # print(min(ans))



