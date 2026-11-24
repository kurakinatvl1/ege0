
for x in range(1,3001):
    n = 9*11**210+8*11**150 - x
    cnt = 0
    while n:
        if n%11==0:cnt+=1
        n//=11
    if cnt==60:
        print(x)