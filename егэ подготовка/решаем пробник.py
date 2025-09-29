def f(n)
    if n < 3: return n
    else:
        if n > 2 and n//2==0:
            return f(n-1)+f(n-2)+1
        