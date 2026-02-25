# f = open('5')
#
#
# a = [int(x) for x in f]
# ans = []
#
# max43 = max(x for x in a       if(len(str(abs(x)))==5 and abs(x)%100==43))
# for i in range(len(a)-2):
#     x = a[i]
#     y = a[i+1]
#     z = a[i+2]
#     if ((len(str(abs(x)))==5 and  abs(x)%100==43)
#     or (len(str(abs(y)))==5 and abs(y)%100==43)
#     or (len(str(abs(z)))==5 and abs(z)%100==43)) and\
#        x*x + y*y + z*z <= max43**2:
#         ans += [x*x + y*y + z*z]
# print(len(ans), min(ans))




def g(x):
    return len(str(abs(x)))==5 and abs(x)%100==43
f = open('5')


a = [int(x) for x in f]
ans = []

max43 = max(x for x in a       if g(x))
for i in range(len(a)-2):
    x = a[i]
    y = a[i+1]
    z = a[i+2]
    if (g(x) or g(y) or g(z)) and\
       x*x + y*y + z*z <= max43**2:
        ans += [x*x + y*y + z*z]
print(len(ans), min(ans))

