#из 10 в любую до 10
def perevod(x, ost):
    s = ''
    while x > 0:
        ost = x%osn
        s =str(ost) + s
        x = x//osn
    return s

from string import  *
alf = ' 0123456789' + ascii_lowercase

def perevod2 (x, osn):
    s = ''
    while x > 0:
        ost = x%osn
        s = alf[ost] + s
        x = x//osn
    return  s


