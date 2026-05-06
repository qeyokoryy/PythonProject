s = open('4.txt').readline()
print(len(s))
maxx = 0
for i in range(len(s)):
    if i%100000==0: print(i)
    for j in range(i+maxx,len(s)):
        cut = s[i:j+1]
        if cut.count('X')>1 or cut.count('Y')>1:
            break
        if cut.count('X') == 1 and cut.count('Y') == 1:
            maxx = max(maxx,len(cut))

print(maxx)