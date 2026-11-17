cnt = 0
from string import printable as alph

def conv(num,sys):
    res =''
    while num:
        res+= alph[num%sys]
        num//=sys
    return res[::-1] if res else '0'
for i in range(10,10000):
    if len(conv(i,5))==4 and len(conv(i,3))==5 and conv(i,16)[-1]=='d':
        cnt+=1
print(cnt)