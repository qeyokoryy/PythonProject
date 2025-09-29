x = int(input())
c = x%10 #last
a = x//100 # first
b = (x//10)%10 #twelve

maxd = max(a,b,c)
mind = min(a,b,c)
medd = a+b+c - maxd - mind

res = mind*100 + medd*10 + maxd

print(res)

#намнооого проше
x = input()
c = int(x[2]) # last
a = int(x[0]) # first
b = int(x[1]) # twelve

maxd = max(a,b,c)
mind = min(a,b,c)
medd = a+b+c - maxd - mind

res = str(mind) + str(medd) + str(maxd)
print(int(res)