from string import printable as alph

for x in alph[:27]:
    n = int(f'8{x}38{x}68',27)
    n2 = int(f'37{x}3163',27)
    n3 = n+n2
    if n3%26==0:
        print(n3//26)