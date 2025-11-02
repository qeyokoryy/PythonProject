from turtle import *
screensize(2000, 2000)
tracer(0)
lt(90)
k = 30
for i in range(2):
    fd(7*k)
    rt(60)
    fd(12*k)
    rt(120)
up()
fd(7*k)
rt(60)
down()
for j in range(2):
    fd(5*k)
    rt(120)
    fd(10*k)
    rt(60)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(3, 'red')
done()