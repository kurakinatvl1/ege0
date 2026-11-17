n = 51*7**12 - 7**3 - 22
cnt = 0
while n:
    cnt += n%7
    n //= 7
print(cnt)