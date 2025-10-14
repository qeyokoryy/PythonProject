# for n in range(9999, 999, -1):
#     s = str(n)
#     x1 = int(s[0])+int(s[1])
#     x2 = int(s[1])+int(s[2])
#     x3 = int(s[2])+int(s[3])
#     a = [x1, x2, x3]
#     a = sorted(a)
#
#     r = str(a[1])+ str(a[2])
#
#     if r == '1115':
#         print(n)
#         break

for n in range(9999, 999, -1):
    n1 = str(n) # создаем строку из числа, чтобы брать оттуда цифры
    x = int(n1[0]) + int(n1[1])
    y = int(n1[1]) + int(n1[2])
    z = int(n1[2]) + int(n1[3])
    a = [x, y, z]
    a.sort()
    r = str(a[1]) + str(a[2])
    if r == '1115':
        print(n)
        break # нашли наибольший ответ, дальше не смотрим
#
#
#
#
#
#
