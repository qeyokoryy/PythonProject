from ipaddress import *
comp = ip_address('205.154.212.20')
for mask in range(1,33):
    n = ip_network(f'{comp}/{mask}',0)
    if ('205.154.192.0' in str(n)) and n[0]<comp<n[-1]:
        print(n.netmask)