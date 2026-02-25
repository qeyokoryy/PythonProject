def f(s,m):
    if s >= 351: return m%2==0
    if m==0: return 0
    h = [f(s+1, m-1), f(s+4,m-1), f(s*2,m-1)]
    return any(h) if m%2==1 else all(h)

print('19)', *[s for s in range(1,351) if f(s,2)])
print('20)', *[s for s in range(1,351) if f(s,3) and not f(s,1)])
print('21)', *[s for s in range(1,351) if f(s,4)and not f(s,1)])