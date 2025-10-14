# ans = []
# for n in range(1, 10000):
#     n2 = f'{n:b}'
#
#     k0 = n2.count('1')
#     if k0%2==0:
#         n2+='0'
#     else:
#         n2+='1'
#
#         if n%2==0:
#             n2+='1'
#         else:
#             n2+='0'
#             r = int(n2, 2)
#             if r > 204:
#
#                 ans.append(r)
#
#                 print(min(ans))
#                 break


ans = []
for n in range(1, 1000):
    n1 = f'{n:b}'
    if n1.count('1') % 2 == 0:
        n1 += '0'
    else:
        n1 += '1'
    if n % 2 == 0:
        n1 += '1'
    else:
        n1 += '0'
    r = int(n1, 2)
    if r > 204:
        ans.append(r)
print(min(ans))
#
