
def conv(x):
    num = 3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 1* 7**(2*x)
    return int(num)
for x in range(-4,100):
    n = conv(x)
    ans = ''
    while n:
        ans += str(n%7)
        n //= 7
    if sum(map(int,ans)) ==18:
        print(x)
        break