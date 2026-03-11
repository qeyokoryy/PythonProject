f = open('17.txt')

ans = []
a = [int(x) for x in f]
k = 0


for i in range(len(a)-2):
    x = a[i]
    y = a[i+1]
    z = a[i+2]
    s = x+y+z
    not_four_digit = 0

    if len(str(abs(x)))!=4 or len(str(abs(y)))!=4 or len(str(abs(z)))!=4:
        # if not_four_digit == 1 and int(s**0.5)**2 == s:
        k += 1



print(k)
