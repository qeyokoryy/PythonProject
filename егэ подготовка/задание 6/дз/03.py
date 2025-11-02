from turtle import *
screensize(2000, 2000)
k = 30
tracer(0)
lt(90)
for i in range(2):
    fd(24*k)
    rt(90)
    fd(16*k)
    rt(90)
up()
fd(10*k)
rt(90)
fd(8*k)
lt(90)
down()
for j in range(2):
    fd(15*k)
    rt(90)
    fd(28*k)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20,30):
        goto(x*k, y*k)
        dot(3, 'red')
done()