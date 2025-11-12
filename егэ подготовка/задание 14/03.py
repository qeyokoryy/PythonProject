# def p (x, osn):
#     s = ''
#     while x > 0:
#         ost = x%osn
#         s = str(ost) + s
#         x = x//osn
#     return s
# a = 9 ** 7 + 3 ** 21 - 8
# a3 = p(a,3)
# print (sum(map(int, a3)))


k = 0
a = 9 ** 7 + 3 ** 21 - 8
while a > 0:
     k+= a %3
     a //= 3
print(k)


