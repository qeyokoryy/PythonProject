f = open('01')#открыть файл
k = 0
for s in f:
    a = [int(x) for x in s.split()]#собираем все числа из строк в числа
    a.sort()
    if (a[0]+a[-1])**2 > a[1]**2 + a[2]**2 + a[3]**2:
        k+=1
print(k)




