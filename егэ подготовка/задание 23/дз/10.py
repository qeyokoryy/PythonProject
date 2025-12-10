def f(s,e):
    if s == e:
        return 1
    if s < e:
        return 0
    if s%10 != 0:
        return f(s - s//10, e) + f(s - s%10, e)+ f(s//2, e)
    return f(s - s//10 , e) + f(s - 2, e)+ f(s//2, e)
print(f(47, 40) * f(40, 18) * f(18, 14))

