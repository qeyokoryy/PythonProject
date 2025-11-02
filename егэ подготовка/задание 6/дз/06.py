from turtle import *
screensize(2000, 2000)
tracer(0)
lt(90)
k = 30
for i in range(2):
    fd(20*k)
    lt(270)
    fd(12*k)
    rt(90)
up()
fd(9*k)
rt(90)
fd(7*k)
lt(90)
down()
for j in range(2):
    fd(13*k)
    rt(90)
    fd(6*k)
    rt(90)
up()
for x in range(-20, 30):
    for y in range(-20,30):
        goto(x*k,y*k)
        dot(3, 'red')
done()