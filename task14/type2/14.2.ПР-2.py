from string import printable as alph

for x in range (10,14):
    for y in range (9,x):
        n1 = (f'7{alph[x]}37{alph[y]}',14)
        n2 = int(f'9{alph[y]}63',x)
        n3 = int('15148',y)

        ############
# for x in alph[10:14]:
#     for y in alph[9:int(x,36)]:
