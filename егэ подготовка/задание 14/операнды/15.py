from  string import *
alf = digits+ ascii_lowercase

for x in alf[:15]:
    for y in alf[:17]:
        a = int(f'123{x}5', 15)
        b = int(f'67{y}9',17)
        if (a+b)%131==0:
            print(x, y, (a+b)//131)