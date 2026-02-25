from ipaddress import *
n = ip_network('98.71.254.171/255.248.0.0', 0)
k = 0
for ip in n:
    ip2 = bin(int(ip))[2:].zfill(32)
    k += 1
    if ip2.count('1')%1==0:

        print(ip)
