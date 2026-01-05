from ipaddress import *

n = ip_network('192.168.240.0/255.255.255.0', 0)
k = 0
for ip in n:
    ip2 = f'{ip:b}' #ip2 = bin(int(ip))[2:].zfill(32)
    if ip2.count('0')==ip2.count('1'):
        k+=1
print(k)
