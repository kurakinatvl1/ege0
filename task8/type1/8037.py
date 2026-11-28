from itertools import product
alph = sorted('победа')
ans = []
for pos,val in enumerate(product(alph,repeat=6),start=1):
    val = ''.join(val)
    if val[0]=="о" and len(set(val))==6 and pos%2==0:
        ans.append(pos)

    # if all([val.count(i)==1 for i in alph]):
    #     if pos%2==0:
    #         ans.append(pos)

print(max(ans))

