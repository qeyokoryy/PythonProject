from ipaddress import *
comp = ip_address('180.23.32.0')
k = 0
for mask in range(1,33):
    n = ip_network(f'{comp}/{mask}', 0)
    if ('255.255.240.0' in str(n)) and n[0]<comp<n[-1]:
        if f'{n:b}'.count('1')%2==0: #and
            k+=1
print()