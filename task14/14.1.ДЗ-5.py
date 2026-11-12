for n in range(10,41):
    r= f'{n:b}'
    if r[-4:]=='1011':
        print(n)