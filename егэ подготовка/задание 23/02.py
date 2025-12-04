def f(s, e):
    if s == e: return 1
    if s > e or s==5 or s == 10: return 0# избегаем 5 и 10
    return f(s+1, e) + f(s*2, e) + f(s+3, e)
print(f(2, 14))

