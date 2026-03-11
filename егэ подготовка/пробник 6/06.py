from turtle import *
k = 20
screensize(2000,2000)
tracer(0)
lt(90)
for i in range(2):
    fd(10*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(14*k)
lt(90)
down()
for i in range(2):
    fd(17*k)
    rt(90)
    fd(7*k)
    rt(90)
up()

for x in range(-30,30):
    for y in range(-30,30):
        dot(3,'red')
        goto(x*k, y*k)

done()