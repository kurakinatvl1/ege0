for n in range(1,10000):
    r = f'{n:b}'
    if r.count('1')%2==0:
        r = '11'+r[2:]+'1'
    else:
        if r.count('1')==r.count('0'):
            r += '1'
        else:
            r += '0'
    r = int(r,2)
    if r>271:
        print(n)
        break