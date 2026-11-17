ans = []
for x in range(1,2031):
    n = 5**150 + 5**100 - x
    cnt = 0
    while n:
        if n % 5 == 0:cnt += 1
        n //= 5
    ans.append([cnt,x])
print(max(ans))