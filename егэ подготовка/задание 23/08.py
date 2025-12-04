def f(s, e):
    if s == e: return 1
    if s > e or s == 43: return 0
    return f(s*2+1, e) + f(s + (s-1), e) + f(s + (s + 1), e)
print(f(7,63))
