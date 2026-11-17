from string import printable as alph
for x in alph[:16]:
    n1 = int(f'11{x}73',16)
    n2 = int(f'94662{x}53{x}',16)
    n3 = int(f'6{x}41',16)
    n4 = int(f'31{x}77',16)
    n5 = int(f'9{x}82{x}{x}181',16)
    n = n1 + n2 + n3 + n4 + n5
    if n%15==0:
        print(n//15)
