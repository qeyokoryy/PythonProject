from ipaddress import *
comp = ip_address('192.168.156.235')

n = ip_network(f'{comp}/255.255.255.240', 0)
print(int(comp)-int(n[0]))
