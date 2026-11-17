ans = []
for x in range(1,3000):
    n = 9**150 + 9**30 - x
    cnt =0
    while n:
        if n % 9 == 0:
            cnt += 1
        n //= 9
    if cnt == 122:
        ans.append(x)
print(min(ans))