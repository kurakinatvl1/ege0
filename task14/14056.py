num = 5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024-2025
cnt = 0
res = []
while num:
    res.append(num%36)
    num //= 36
for c in res:
    if c%2 == 0:
        cnt += 1
print(cnt)