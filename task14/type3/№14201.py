ans = []

for x in range(1,2031):
    n = 3**100 - x
    cnt = 0
    while n:
        if n%3==0:cnt+=1
        n//=3
    ans.append([cnt,x])
print(max(ans))