from ipaddress import *

n = ip_network('203.68.128.0/255.255.192.0', 0)
k = 0
for ip in n:
    ip2 = bin(int(ip))[2:].zfill(32)
    if ip2.count('1')%7!=0:
        k+=1
print(k)