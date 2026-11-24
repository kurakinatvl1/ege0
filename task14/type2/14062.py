from string import printable as al

for x in range(22):
    n1 = int(f'27{al[x]}98876',22)
    n2 = int(f'26{al[x]}51',22)
    n3 = int(f'711{al[x]}5',22)
    n = n1+n2+n3
    if n%21==0:
        print(n//21)
        break