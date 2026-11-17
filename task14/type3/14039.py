res = []
for x in range(1,2030):
    n = 3**100- x
    cnt = 0
    while n:
       if n % 3==0:cnt+=1
       n//= 3
    if cnt == 1:
        res.append(x)
print(max(res))
