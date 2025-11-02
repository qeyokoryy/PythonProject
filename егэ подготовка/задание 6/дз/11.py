from turtle import *
screensize(2000, 2000)
tracer(0)
lt(90)
k = 30
for i in range(2):
    fd(3*k)
    rt(90)
    fd(20*k)
    rt(90)
up()
bk(8*k)
rt(90)
fd(9*k)
lt(90)
down()
for j in range(2):
    fd(16*k)
    rt(90)
    fd(8*k)
    rt(90)
up()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x * k, y * k)
        dot(3, 'red')
done()