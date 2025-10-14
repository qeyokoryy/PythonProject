# for n in range(1000, 10000):
#     s = str(n)
#     x1 = int(s[0])*int(s[1])
#     x2 = int(s[2])*int(s[3])
#
#     a = [x1, x2]
#     a = sorted(a)
#
#     r = str(a[0]) + str(a[1])
#     if r == '5472':
#         print(n)
#         break


for n in range(1000, 10000):
    n1 = str(n) # создаем строку из числа, чтобы брать оттуда цифры
    x = int(n1[0]) * int(n1[1])
    y = int(n1[0]) * int(n1[2])
    z = int(n1[0]) * int(n1[3])
    a = [x, y, z]
    a.sort()
    r = str(a[1]) + str(a[2])
    if r == '5472':
        print(n)
        break # нашли наименьший ответ, дальше не смотрим
