ans = []
for n in range(1,10000):
    r = f'{n:b}'
    r= r + str(r.count('1')%2)
    r= r + str(r.count('1')%2)
    r = int(r,2)
    if r>396:
        ans.append(r)
print(min(ans))
print(bin(2025))
print(int('101111101001',2))
