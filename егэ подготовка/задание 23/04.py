def f(s, e):
    if s == e: return 1
    if s > e: return 0
    return f(s+1, e) + f(s + 3, e) + f(s*2, e)
print(f(2,6)* f(6, 10)* f(10,14))
