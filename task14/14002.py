a = 4*625**9-25**15+2*5**11-7
def conv(n,sys):
    res = ''
    while n:
        res+= str(n%sys)
        n//=sys
    return res[::-1] if res else '0'
print(conv(a,5).count('4'))


######################################

a = 4*625**9-25**15+2*5**11-7
cnt = 0
while a:
    if a%5==4:cnt+=1
    a//=5
print(cnt)
