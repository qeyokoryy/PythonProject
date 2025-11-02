
from turtle import *

screensize(2000, 2000)
tracer(0)
lt(90)
k = 50
for i in range(7):
    fd(10 * k)
    rt(120)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(3, 'red')
done()
