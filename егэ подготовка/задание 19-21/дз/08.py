def f(s,m):
    if s <= 19: return m%2==1
    if m==0: return 0
    h = []
    if s -5 > 0: h.append(f(s-5,m-1))
    if s%2==0: h.append(f(s//2, m-1))
    if s%3==0: h.append(f(s//3,m-1))
    if s % 2 == 1 and s % 3 != 0: h.append(f(s + 1, m - 1))
    return any(h) if m%2==1 else all(h)

print('19)', *[s for s in range(19, 250) if f(s,2)])
print('20)', *[s for s in range(19, 250) if f(s,3) and (not f(s,1))])
print('21)', *[s for s in range(19, 250) if f(s,4) and (not f(s,2))])