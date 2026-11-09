def conv(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1,10000):
    r = conv(n,3)
    if n%3==0:
        r =  r + r[-2:]
    else:
        r+= conv((sum(map(int,r))*2),3)
    r = int(r,3)
    if r%2!=0 and r>520:
        ans.append(r)
print(min(ans))