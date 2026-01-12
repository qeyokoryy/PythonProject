# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 10 [ Повтори 3 [ Вперёд 10 Направо 90 Вперёд 10 Направо 270] Направо 90]
# Определите площадь получившейся фигуры в квадратных единицах

from turtle import *
tracer(0)
lt(90)
screensize(2000, 2000)
k = 10
for i in range(10):
    for j in range(3):
        fd(10 * k)
        rt(90)
        fd(10* k)
        rt(270)
    rt(90)

up()

for x in range(-10, 60):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(5, 'green')


done()
