from turtle import *

lt(90)
screensize(3000,3000)
tracer(0)
k = 25

for n in range(3):
    fd(39 *k)
    rt(90)
    fd(48 * k)
    rt(90)

up()

fd(27 * k)
rt(90)
fd(24 * k)
lt(90)
down()
for n in range(3):
    fd(29*k)
    rt(90)
    bk(18*k)
    rt(90)

up()

for x in range(-50,50):
    for y in range(-50,50):
        dot(3,'red')
        goto(x*k,y*k)

done()