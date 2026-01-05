from ipaddress import *

comp1 = ip_address('201.44.240.33')
comp2 = ip_address('201.44.240.107')

k = 0

for mask in range(1,33):
    n1 = ip_network(f'{comp1}/{mask}', 0)
    n2 = ip_network(f'{comp2}/{mask}', 0)
    if n2 == n1 and n1[0]<comp1<n2[-1] and n1[0]<comp2<n2[-1]:
        if f'{n1[0]:b}'.count('1') >=5:
            k+=1
print(k)