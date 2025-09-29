#вводится четырехзначное число. определите сумму его цифр.
x = int(input())
a = x%10
b = x // 1000
c = (x//100)%10
d = (x//10)%10
print(a+b+c+d)

#строки
x = 5
print(5*2) #ответ: 10, т.к 5-число
x = str(x)
print(x*2) #ответ: 55, т.к 5-строка, происходит дублированние

print('И'*2,'Н'*7,'?')

x = int(input())
print(x, 'Кбайт =', x*1024, 'байт =', x*1024*8, 'бит'  )

#индексы и срезы
s= 'informatika_na_100' #от 0 до 17(номер симфола)
print(s[2:7]) #ответ: forma( с 2 символа по 7)
#s[x:y:h] x - старт, y- конец(не включая), h-шаг
s= 'informatika_na_100'
print(s[2:7:2])
#длина строки
s= 'informatika_na_100'
print(len(s)) #ответ: 18 символов

s= 'informatika_na_100'
print(s[3])
print(s[-1])
print(s[:3])
print(s[:-3])
print(s[1::2])
print(s[::2])
print(s[::-1])
print(s[::-2])
print(len(s))