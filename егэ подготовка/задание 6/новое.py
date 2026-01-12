from turtle import *
lt(90)
screensize(3000,3000)
k = 20
tracer(0)
for i in range(4):
    fd(28*k)
    rt(90)
    fd(26*k)
    rt(90)
up()
fd(8*k)
rt(90)
fd(7*k)
lt(90)
down()
for i in range(4):
    fd(67*k)
    rt(90)
    fd(98*k)
    rt(90)
up()

for x in range(-30,70):
    for y in range(-30,80):
        dot(3,'purple')
        goto(x*k, y*k)
done()

