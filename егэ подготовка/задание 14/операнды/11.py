
alf = '0123456789abcde'

for x in alf:
    a = int(f'123{x}5', 15)
    b = int(f'1{x}233', 15)
    if (a+b)%14==0:
        print((a+b)//14)
        break