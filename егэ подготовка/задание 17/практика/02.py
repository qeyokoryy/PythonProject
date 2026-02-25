f = open('2')

ans = []

a = [int(x) for x in f]

for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if (abs(x)%7==0 and abs(y)%17!=0) or (abs(y)%7==0 and abs(x)%17!=0):

        ans+=[x+y]

print(len(ans), min(ans))