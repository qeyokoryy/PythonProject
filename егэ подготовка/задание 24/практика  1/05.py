s = open('5.txt').readline()
maxx = 0
# print(len(s))
for i in range(len(s)):
    if i%100000==0: print(i)
    for j in range(i+maxx,len(s)):
        cut = s[i:j+1]
        if cut.count('RO')>21 or ('ORO' in cut) or ('ROR' in cut) :
            break
        if cut.count('RO')==21:

            maxx = max(maxx,len(cut))
print(maxx)