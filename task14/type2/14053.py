from string import printable as alp
for x in range(22):
    n1 = int(f'12313{alp[x]}57',22)
    n2 = int(f'1{alp[x]}34561',22)
    n= n1+n2
    if n%21==0:
        print(n//21)
