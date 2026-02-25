def f(a,b,m): # a and b кол в кучах m - код хзодов до конца
    if a + b >= 100: return m%2==0
    if m==0: return 0

    h = [f(a + 3 , b, m-1), f(a*2 , b, m-1), f(a , b+3, m-1), f(a , b*2, m-1)]
    return any(h) if m%2!=0 else all(h)

print('19)', *[s for s in range(1,83) if f(17,s,2)])
print('20)', *[s for s in range(1,83) if f(17,s,3) and (not f(17,s,1))])
print('20)', *[s for s in range(1,83) if f(17,s,4) and (not f(17,s,2)) ])


# 19) 40
# 20) 20 29
# 20) 36
