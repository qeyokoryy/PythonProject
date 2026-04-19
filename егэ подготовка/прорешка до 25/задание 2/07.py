print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x<=w) and ((not y) <= z)) <= ((z==x) or (w and (not y))))==False:
                    print(x,y,w,z)
