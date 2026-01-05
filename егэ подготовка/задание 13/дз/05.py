from ipaddress import *
comp = ip_address('151.192.0.0')
k = 0
for mask in range(1,33):
    n = ip_network(f'{comp}/{mask}',0)
    if ('255.224.0.0'in str(n)) and n[0]<comp<n[-1]:
        if (f'{n:b}'.count('0'))-(f'{n:b}'.count('1'))==4:
            k+=1
print(k)

