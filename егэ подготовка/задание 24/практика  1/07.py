s = open('7.txt').readline()
print(len(s))
minn = 10000
for i in range(len(s)):
    if i%100000==0: print(i)
    for j in range(i+minn, i, -1):
        cut = s[i:j+1]
        if cut.count('.')<7:
            break
        if cut.count('.')==7:
            minn = min(minn,len(cut))
print(minn)

