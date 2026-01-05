from ipaddress import *

n = ip_network('192.168.32.160/255.255.255.240', 0)
k=0
for ip in n:
    ip2 = bin(int(ip))[2:].zfill(32)
    if ip2.count('1')%2==0:
        k+=1
print(k)