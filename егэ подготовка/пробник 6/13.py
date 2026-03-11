from ipaddress import *


comp = ip_network('192.168.32.160/255.255.255.240', 0)
k = 0
for ip in comp:
    ip = bin(int(ip))[2:].zfill(32)
    if ip.count('0')>21:
        k+=1
print(k)