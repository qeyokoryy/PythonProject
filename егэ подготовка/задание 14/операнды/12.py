alf = '0123456789abcdefghi'
for x in alf:
    a = int(f'98897{x}21', 19)
    b = int(f'2{x}923',19)
    if (a+b)%18==0:
        print((a+b)//18)
        