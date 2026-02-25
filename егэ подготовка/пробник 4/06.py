from turtle import *
screensize(2000,2000)
lt(90)
tracer(0)
k=30
for i in range(2):
    fd(9*k)
    rt(90)
    fd(15*k)
    rt(90)
up()
fd(12*k)
rt(90)
down()
for i in range(2):
    fd(6*k)
    rt(90)
    fd(12*k)
    rt(90)
up()

for x in range(-20,20):
    for y in range(-20, 20):
        dot(3, 'red')
        goto(x*k, y*k)

done()