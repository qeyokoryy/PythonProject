from turtle import *
screensize(2000, 2000)
lt(90)
k = 50
tracer(0)
for i in range(14):
    for j in range(3):
        fd(3* k)
        rt(90)
    lt(180)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(3, 'red')
done()
