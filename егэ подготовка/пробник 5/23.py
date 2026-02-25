def f(s,e):
    if s == e: return 1
    if s > e: return 0
    return f(s*2,e)+f(s*4,e) + f(s+1,e)

print(f(36,150) * f(150,156))


