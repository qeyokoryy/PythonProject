def f(a,b,m):
    if a+b >=30: return m%2==0
    if m==0: return 0
    h = [f(a+1, b, m-1),f(a, b+1, m-1), f(a*2, b, m-1), f(a, b*3, m-1)]
    return any(h) if m%2!=0 else all(h)
cnt = 0

for k in range(1,29):
    for s in range(1,29):
        if f(k,s,2) and (not f(k,s,0)):
            k+=1
print('19)', k)
print('20)', *[s for s in range(1, 30) if f(s,7,2) and (not f(s,7,1))])

print('21)', *[s for s in range(1,30) if f(s,1,2) and (not f(s,1,2))])



