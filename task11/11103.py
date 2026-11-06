from math import log2,ceil

n = 70 + 10
for l in range(1,10000):
    i = ceil(log2(n))
    I = ceil(l*i/8)
    if 1234567*I>24*2**20:
        print(l)
        break

