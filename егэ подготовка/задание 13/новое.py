from ipaddress import *
n = ip_network('5.2.5.0/255.255.0.0', 0)
k=0
for ip in n:
    ip2 = bin(int(ip))[2:].zfill(32)
    if ip2.count('0')%25==0:
        k+=1
print(k)