def f(s,m): #s-кол камней в куче m-кол ходов до конца игры
    if s>=82: return m%2==0
    if m==0: return 0
    h = [f(s+2, m-1), f(s+4, m-1), f(s*3, m-1)]
    # return any(h)#-для 19 когда неудачный ход
    return any(h) if m%2==1 else all(h) # для 20 и 21


print('19)', *[s for s in range(1,82) if f(s,2)] )
print('20)', *[s for s in range(1,82) if f(s,3) and (not f(s,1))] )
print('21)', *[s for s in range(1,82) if f(s,4) and (not f(s,2))] )


# 20) 9 22 23 24 25
# 21) 20 21