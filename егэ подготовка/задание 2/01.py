print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (x and (not y)) or (x and z)==1:
                print(x,y,z)



