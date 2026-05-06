s = open('10.txt').readline()
minn = 10000
print(len(s))
for i in range(len(s)):
    if i%100000==0:print(i)
    for j in range(i+minn,i,-1):
        cut = s[i:j+1]
        if cut.count('2025') < 110 or cut.count('W')<90: break
        if cut.count('2025')>=110 and cut.count('W')==90:
            minn = min(minn,len(cut))
print(minn)