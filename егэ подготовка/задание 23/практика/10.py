def f(s,e):
    if s == e: return 1
    if s < e: return 0
    if s**0.5 == int(s**0.5): #если ивзлекается корень, то извлечь его
        return f(s-3, e) + f(s-4, e) + f(s**0.5, e)
    return f(s-3, e) + f(s-4, e)
print(f(36, 21)*f(21, 3))
