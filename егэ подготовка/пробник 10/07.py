from math import  *
pic1 = (3840 * 2160 * 20)//8
saved = 2322000 * 120 // 1024 # сохранено в байтах
pic = (1280 * 720) // 8
b = ((pic1-saved)/120)/pic
er = ceil(log2(b))
print(int(b))

