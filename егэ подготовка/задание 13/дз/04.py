from ipaddress import *
n = ip_network('158.214.121.40/255.255.255.224', 0)
k=0
for ip in n:
    ip2 = bin(int(ip))[2:].zfill(32)

print(ip)
