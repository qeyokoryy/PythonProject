#долгий путь
x = 10
y = 32
z = 22

if x > y and x > z:
    print('x Больше')
if y > x and y > z:
    print('y Больше')
if z > y and z > x:
    print('z Больше')
#быстрый
x = 10
y = 32
z = 22

if x > y and x > z:
    print('x Больше')
else:
    if y>z:
        print('y больше')
    else:
        print('z больше')
#+elif
if x > y and x > z:
    print('x Больше')
elif y>z:
        print('y больше')
    else:
        print('z больше')
