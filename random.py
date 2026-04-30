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

# ans = []
# for n in range(1,10000):
#     n2 = f'{n:b}'
#     if n%2==0:
#         n2 = '1'+n2 + str(n2.count('1')%2)
#     else:
#         n2 =   n2 + '0' + str(n2.count('1')%2)
#     r = int(n2, 2)
#     if r == 101:
#         print(n)
#         break
#
#   #   if r> 100: ans+=[r]
#   # print(min(ans))
#
#
#


# for n in range(100000,0,-1):
#     n2 = f"{n:b}"
#     if n%3==0: n2+= n2[-3:]
#     else:
#         ost = n%3
#         ost = ost*3
#         ost2 = f'{ost:b}'
#         n2+=ost2
#
#     r = int(n2,2 )
#     if r < 130:
#         print(n)
#         break

#
# ans = []
# for n in range(19,10000):
#     n2 = f'{n:b}'
#     if n%2==0: n2 = '10' + n2
#     else:n2 = '1' + n2 + '01'
#
#
#     r = int(n2,2)
#     ans += [r]
# print(min(ans))

ans = []
def f(x,osn):


    s = ''
    while x>0:
        ost = x%osn
        s = str(ost) + s
        x //= osn
    return  s

for n in range(1, 10000):
    n3 = f(n,3)
    if n%3==0: n3 += n3[-2:]
    else:
        summa = sum(map(int,n3))
        summa*=3
        n3+= f(summa,3)

    r = int(n3,3)
    if r > 208 and r%2!=0:

        ans += [r]
print(min(ans))
