ans = []
for x in range(1,2031):
    n = 6**2030+6**100 - x
    cnt = 0
    while n:
        if n % 6 == 0:
            cnt += 1
        n //= 6
    ans.append(cnt)
print(max(ans))
