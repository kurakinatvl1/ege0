from itertools import product
alph = sorted('клмняа')
for pos,val in enumerate(product(alph,repeat = 5),start = 1):
    if val[0]+val[1]=='км':
        print(pos,val)
        break