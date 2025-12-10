def f(s,e):
    if s==e:
        return 1
    if s < e or s == 28:
        return 0
    if s %2 ==0:
        return f(s-2, e) + f(s//2, e)
    return f(s-3, e) + f(s-2, e)
print(f(98,1))