s = open('2.txt').readline()
maxx = 0

for i in range(len(s)):
    # if i%1000000==0: print(i)
    for j in range(i+maxx, len(s)):
        cut = s[i:j+1]
        if len(set(cut))>1:
            break

        maxx = max(maxx,len(cut))
print(maxx)
