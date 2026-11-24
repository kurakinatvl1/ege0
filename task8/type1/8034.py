from itertools import product
alph = sorted('окусф')
ans = []

for pos,val in enumerate(product(alph,repeat = 5),start = 1):
    val = ''.join(val)
    if "ф" not in val and val.count('у')==2:
        ans.append(pos)
print(max(ans))