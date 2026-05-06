s = open('3.txt').readline()
maxx = 0
# print(len(s))
for i in range(len(s)):
    if i%100000==0:print(i)
    for j in range(i+maxx, len(s)):
        cut = s[i:j+1]
        if cut.count('FSRQ')>80:
            break
        if cut.count('FSRQ')==80:
            maxx = max(maxx, len(cut))
print(maxx)