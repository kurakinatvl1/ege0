def conv(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

for n in range(1,10000):
    r = conv(n)
    if n%3==0: r = '1'+r+'02'
    else:r+= conv(n%3*5)
    r = int(r,3)
    if r>=177:
        print(n)
        break