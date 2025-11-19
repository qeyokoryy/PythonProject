a = 5*729**2024 + 3*243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017

summa = 0
while a > 0:
    ost = a %27
    if ost % 2 == 0 and ost <= 25:
        summa +=ost
    a//=27
print(summa)