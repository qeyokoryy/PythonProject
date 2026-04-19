from string import *

alf =  digits + ascii_lowercase

for x in alf[:29]:
    a = int(f'923{x}874',29)
    b = int(f'524{x}6152', 29)
    if (a+b)%28==0:
        print(int(x, 29), (a+b)//28)
        print(f'частное {(a+b)//28}')

