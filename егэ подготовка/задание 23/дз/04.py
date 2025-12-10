def f(s,e):
    if s == e:
        return 1
    if s < e or s == 20:
        return 0
    return f(s-2, e) + f(s-3, e) + f(s//5, e)
print(f(41, 10) * f(10,5))