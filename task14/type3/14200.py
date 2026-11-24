ans = []

for x in range(1,2031):
    n = 2**2025 + 2**2024 - 2**2021 - x
    cnt = 0
    while n:
        if n%4==0:cnt+=1
        n//=4
    ans.append([cnt,x])
print(max(ans))
