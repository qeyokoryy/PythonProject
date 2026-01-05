from ipaddress import *
comp = ip_address('251.211.38.240')
k = 0
for mask in range(1,33):
    n = ip_network(f'{comp}/{mask}',0)
    if ('251.211.38.0' in str(n)) and n[0]<comp<n[-1]:
        k+=1
print(k)