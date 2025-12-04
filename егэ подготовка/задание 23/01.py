def f(s, e): #s - старт, e -конец
    if s == e: # если попали в целевое число
        return 1
    if s > e:
        return 0
    return f(s+1, e) + f(s*2, e) # наши ходы
print(f(1,8))


