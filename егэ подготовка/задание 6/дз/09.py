from turtle import *
screensize(2000, 2000)
tracer(0)
lt(90)
k = 30
for i in range(4):
    fd(27*k)
    rt(90)
    fd(21*k)
    rt(90)
up()
fd(3*k)
rt(90)
fd(7*k)
lt(90)
down()
for j in range(4):
    fd(73*k)
    rt(90)
    fd(91*k)
    rt(90)
up()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x * k, y * k)
        dot(3, 'red')
done()