def f(s,e):
    if s==e: return 1
    if s < e: return 0
    total = 0
    total += f(s-3,e)
    if s%2==0:
        total+=f(s//3, e)
    if s >= 10:
       total+= f(int(str(s)[:-1]), e)
    return total

print(f(1250,20))
