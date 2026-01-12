from ipaddress import *
comp = ip_address('156.132.15.138')
n = ip_network(f'{comp}/255.255.252.0', 0)

print(int(comp)-int(n[0]))

