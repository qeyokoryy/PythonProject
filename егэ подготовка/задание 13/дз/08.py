from ipaddress import *
n = ip_network('172.16.80.0/255.255.248.0', 0)
k = 0
for ip in n:
    ip2 = bin(int(ip))[2:].zfill(32)
    if ip2[-1].count('1')%2!=0 and ip2[-2].count('1')%2!=0:
        k+=1
print(k)