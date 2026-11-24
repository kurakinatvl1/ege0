max_zeros = 0
ans_x = 0

for x in range(1, 2031):
    n = 7 ** 170 + 7 ** 100 - x
    cnt = 0
    while n> 0:
        if n % 7 == 0:
            cnt+= 1
        n//= 7
    if cnt >= max_zeros:
        max_zeros = cnt
        ans_x = x

print(ans_x)