num = 11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
cnt = []
while num:
    if num%15 not in cnt:cnt.append(num%15)
    num //= 15
print(len(cnt))
