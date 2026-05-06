s = open('6.txt').readline()
print(len(s))
maxx = 0
bad = 'EFGHIJKLMNOPQRSTUVWXYZ'
for c in bad: s = s.replace(c,'!')
for i in range(len(s)):
    if i%100000==0: print(i)
    for j in range(i+maxx,len(s)):
        cut = s[i:j+1]
        if cut[0]=='0' or ('!' in cut): break
        if cut[-1] in '02468AC':
            maxx = max(maxx,len(cut))
print(maxx)