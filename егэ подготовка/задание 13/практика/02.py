from ipaddress import *
comp = ip_address('111.81.208.27')
for mask in range(1,33):
    nn = ip_network(f'{comp}/{mask}', 0)
    if ('111.81.192.0' in str(nn)) and (nn[0]<comp<nn[-1]):
        print(nn.netmask)
#192

