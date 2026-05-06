s = open('1.txt').readline()
maxx = 0

for i in range(len(s)):
    for j in range(i+maxx, len(s)):
        cut = s[i:j+1]
        if ('D'  in cut ) or ('E'  in cut):
            break

        maxx = max(maxx,len(cut))
print(maxx)