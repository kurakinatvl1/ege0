from string import printable as alph
for x in alph[:20]:
    n1 = int(f'627{x}j8',20)
    n2 = int(f'h45i{x}5hij',20)
    n3 = int(f'4idb49j{x}7',20)
    n = n1 + n2 + n3
    if n%19==0:
        print(n//19)



