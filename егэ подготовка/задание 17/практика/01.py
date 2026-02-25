f = open('1')
ans = []
a = [int(x) for x in f]

for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if abs(x)%10==7 or abs(y)%10==7:
    #if str(x)[-1]=='7' or str(x)[-1]=='7':
        ans+=[x+y]





print(len(ans),max(ans))
