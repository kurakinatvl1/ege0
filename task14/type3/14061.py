from string import printable as alph
for x in range(22):
    n = int(f'27{alph[x]}98966',22)
    n2 = int(f'26{alph[x]}33',22)
    n3 = int(f'522{alph[x]}5',22)
    n4 = n+n2+n3
    if n4%21==0:
        print(n4//21)
