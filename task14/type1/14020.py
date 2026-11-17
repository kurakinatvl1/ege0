from string import printable as alph
for x in alph[:22]:
    n1 = int(f'18{x}89957',22)
    n2= int(f'80{x}33',22)
    n3 = int(f'521{x}6',22)
    n = n1+n2+n3
    if n%21==0:
        print(n//21)
        break
