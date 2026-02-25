f = open('4.txt')

ans = []
a = [int(x) for x in f]
for i in range(len(a)-2):
    x = a[i]
    y = a[i+2]
    if x % 100