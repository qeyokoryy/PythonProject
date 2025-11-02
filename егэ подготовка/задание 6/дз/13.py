from turtle import *
screensize(3000, 3000)
tracer(0)
lt(90)
k = 30
for i in range(1):
    fd(25*k)
    rt(45)
    fd(50*k)
up()
for j in range(1):
    bk(50*k)
    rt(45)
    fd(15*k)
    lt(90)
    fd(30*k)
down()
for p in range(1):
    rt(180)
    fd(60*k)
    bk(5*k)
    rt(90)
    fd(31*k)
up()
for x in range(-20, 20):
    for y in range(-20, 30):
        goto(x*k, y*k)
        dot(3, 'red')
done()