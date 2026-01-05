from ipaddress import *
comp1 = ip_address('165.112.200.70')
comp2 = ip_address('165.112.175.80')
k = 0
for mask in range(1,33):


    n1 = ip_network(f'{comp1}/{mask}', 0)
    n2 = ip_network(f'{comp2}/{mask}', 0)
    if n2 == n1 and n1[0]<comp1<n2[-1] and n1[0]<comp2<n2[-1]:
        k+=1
print(f'{n1[0]}'.count('1')+f'{n2[0]}'.count('1'))