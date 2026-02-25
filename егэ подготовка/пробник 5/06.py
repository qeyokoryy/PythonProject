from turtle import  *
screensize(2000, 2000)
tracer(0)
lt(90)
k = 30

for i in range(2):
    fd(10 * k)
    rt(90)
    fd(18*k)
    rt(90)
up()

bk(6*k)
rt(90)
fd(9*k)
lt(90)
down()
for i in range(2):
    fd(17*k)
    rt(90)
    fd(5*k)
    rt(90)

up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k, y*k)
        dot(5,'purple')

done()
