#uzel = 147.98.54.36

#maska = 255.255.255.0


from ipaddress import *

nn = ip_network('147.98.54.36/255.255.255.0', 0)
for ip in nn:
    print(ip)