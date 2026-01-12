from ipaddress import *
comp1 = ip_address('157.127.182.76')
comp2 = ip_address('157.127.190.80')



for mask in range(1,33):
    n1 = ip_network(f'{comp1}/{mask}',0)
    n2 = ip_network(f'{comp2}/{mask}', 0)
    if n1!=n2 and n1[0]<comp1<n1[-1] and n2[0]<comp2<n2[-1]:
        print(mask)
        break
