from ipaddress import *
comp = ip_address('208.207.230.65')
k = 0
for mask in range(1,33):
    nn = ip_network(f'{comp}/{mask}', 0)
    if ('208.207.224.0' in str(nn)) and (nn[0]<comp<nn[-1]):
        k+=1
print(k)