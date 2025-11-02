from turtle import *
screensize(2000, 2000)
tracer(0)
lt(90)
k = 20
for i in range(9):
    fd(27*k)
    rt(90)
    fd(30*k)
    rt(90)
up()
fd(3*k)
rt(90)
fd(6*k)
lt(90)
down()
for j in range(9):
    fd(77*k)
    rt(90)
    fd(66*k)
    rt(90)
up()
for x in range(-20, 30):
    for y in range(-20,30):
        goto(x*k,y*k)
        dot(3, 'red')
done()