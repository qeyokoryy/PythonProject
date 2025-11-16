alf = '0123456789abc'
for x in alf:
    a = int(f'{x}1418', 13)
    b = int(f'1{x}037', 14)
    c = int(f'2{x}209', 19)
    if a + b == c:
        print(c)