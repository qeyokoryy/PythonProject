from turtle import *
screensize(2000, 2000)
lt(90)
k = 50
tracer(0)
for i in range(3):
    fd(7*k)
    rt(90)
fd(8*k)
for j in range(3):
    lt(90)
    fd(5*k)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(3, 'red')
done()

