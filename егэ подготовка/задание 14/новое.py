from string import ascii_lowercase
alf = '0123456789abcdefghijklmnopqrstuvwxyz'
for x in alf[:21]:
    a = int(f'82934{x}2',21)
    b = int(f'2924{x}{x}7',21)
    c = int(f'67564{x}8',21)
    if (a+b+c)%20==0:
        print(((a+b+c))//20)
        break
