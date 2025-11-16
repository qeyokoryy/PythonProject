from string import *
alf = digits+ascii_lowercase

for x in alf[:21]:
    for y in alf[:21]:
        a = int(f'943697{x}21', 21)
        b = int(f'2{y}9253',21)
        if (a-b)%20==0:
            x10 = int(x,21)
            y10 = int(y, 21)
            print(x10-y10,(a-b)//20 )

