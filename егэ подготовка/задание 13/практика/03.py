from ipaddress import *
comp = ip_address('115.12.69.38')
for mask in range(1,33):
    nn = ip_network(f'{comp}/{mask}', 0)
    if ('115.12.64.0' in str(nn)) and (nn[0]<comp<nn[-1]):
        print(mask)
        break
