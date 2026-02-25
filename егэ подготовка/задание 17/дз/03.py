f = open('3.txt')

ans = []
k = 0
a = [int(x) for x in f]
mdiff = 10**9
for i in range(len(a)-2):
    x = a[i]
    y = a[i+1]
    z = a[i+2]
    if x<y<z:
        k+=1
        diff = z - x
        if diff < mdiff:
            ans +=[x+y+z]
            mdiff=diff

print(len(ans), mdiff)