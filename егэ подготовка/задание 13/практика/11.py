from ipaddress import *
n = ip_network('111.111.111.111/255.255.255.128',0)
print(len(list(n.hosts())))