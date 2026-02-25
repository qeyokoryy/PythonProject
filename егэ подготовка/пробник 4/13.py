from ipaddress import *

comp = ip_address('175.184.48.0')



for m in range(33):
    n = ip_network(f'{comp}/{m}', 0)
    if n[0]<comp<n[-1] and '175.184.52.103' in str(n):
        m2 = f'{m:b}'
        print(m2.count('1'))