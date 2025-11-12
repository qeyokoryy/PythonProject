# from string import *
# alf = '0123456789' + ascii_lowercase
#
# def perevod (x, osn):
#     s = ''
#     while x > 0:
#         ost = x % osn
#         s = alf[ost] + s
#         x = x//osn
#     return s
#
# for x in range(2030, 0, -1):
#     a = 7**91 + 7**160 - x
#     a7 = perevod(a,7)
#     if a7.count('0')==70:
#         print(x)
#         break
#
for x in range(2030, 0, -1):
    k = 0
    a = 7**91 + 7**160 - x
    while a > 0:
        if a%7==0:
            k+=1
        a//=7
    if k == 70:
        print(x)
        break

