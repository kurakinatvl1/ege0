ans = []
for n in range(1,10000):
    r = f'{n:b}'
    r = r + str(r.count('1')%2)
    r = r + str(sum(int(i)for i in r)%2)
    # r = r + str(sum(map(int,r))% 2)
    r = int(r,2)
    if r > 77:
        ans.append(r)
print(min(ans))