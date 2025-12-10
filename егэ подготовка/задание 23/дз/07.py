def f(s,e ):
    if s == e:
        return 1
    if s < e:
        return 0
    return f(s-3, e) + f(s-1, e) + f(s//2, e)
print(f(39,19)*f(19,16) * f(16,7))