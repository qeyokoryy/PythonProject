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
# a = 13*625**1320 + 12 * 125**1230 - 14 * 25 ** 1140 - 13 * 5 ** 1050 - 2500
# a25 = perevod(a, 25)
# print(a25.count('0'))

k = 0
a = 13*625**1320 + 12 * 125**1230 - 14 * 25 ** 1140 - 13 * 5 ** 1050 - 2500
while a > 0:
    ost = a % 25
    if ost == 0:
        k +=1

    a = a//25
print(k)