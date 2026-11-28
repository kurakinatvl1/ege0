n =5**2022-2*5**1010+25**850+2500
cnt = 0
while n:
    if n%5==4:cnt+=1
    n//=5
print(cnt)