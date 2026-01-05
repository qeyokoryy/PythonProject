from ipaddress import *
comp = ip_address('220.128.112.142')
for mask in range(1,33):#перебираем масски
    n = ip_network(f'{comp}/{mask}', 0)#ссоздаем сеть
    if ('220.128.96.0' in str(n)) and (n[0]<comp<n[-1]):#проверка та ли сеть and  проверка не явл ли техническим адресом
        print(n.netmask)
#224
