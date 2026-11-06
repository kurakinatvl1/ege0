def conv(num,sys):
    res = ''
    while num:
     res+= str(num%sys)
     num//=sys
    return res[::-1]
ans = []
for n in range(1,10000):
    r = conv(n,4)
    a = sum(map(int,r))
    if a%2 ==0:
        r = r+r[-2:]
    else:
        r = '2'+r+'0'
    r = int(r,4)
    if r>120 and r%2==0:
        ans.append(r)
print(min(ans))




