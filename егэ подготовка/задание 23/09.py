def f(s, e):
    if s==e: return 1
    if s > e: return 0
    if s%2 == 0: return f(s+1, e) + f(s*1.5, e)
    return f(s+1, e)

print(f(2,22))