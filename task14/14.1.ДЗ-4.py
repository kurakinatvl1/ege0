num = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
res = []
while num:
    a= num%16
    if a not in res:
        res.append(a)
    num //= 16
print(len(res))