def f(n):
    if n == 1: return 1
    if n >=2 and n%2==0: return f(n/2) + 1
    if n >= 2 and n%2!=0: return f(n-1)+n
k = 0
for n in range(1, 100001):
    if f(n) == 16:
        k+=1
print(n)