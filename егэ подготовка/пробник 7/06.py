from turtle import *
screensize(2000,2000)
k = 40
tracer(0)
lt(90)

rt(60)
for n in range(2):
    fd(7*k)
    rt(120)
rt(300)
fd(7*k)
for n in range(2):
    rt(60)
    fd(7*k)
    rt(60)

up()

for x in range(-30,30):
    for y in range(-30,30):
        dot(3,'red')
        goto(x*k, y*k)

done()