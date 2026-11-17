from string import printable as alph
for x in alph[1:13]:
    n1 = int(f'9{x}ab',13)
    n2 = int(f'{x}46c',16)
    n3 = int(f'b7{x}',15)
    n = n1 + n2 - n3
    if n%14==0:
        print(n//14)