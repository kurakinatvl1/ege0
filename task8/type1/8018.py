from itertools import product
alph = sorted('аворт')
ans = []
for pos,val in enumerate(product(alph,repeat = 6),start = 1):
    val = ''.join(val)
    if val == 'ворота':
        print(pos)
        break