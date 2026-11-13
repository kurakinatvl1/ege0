from math import log2,ceil
l = 110
n = 10+1020
i = ceil(log2(n))
I  = ceil(i*l/8)
res = I*32768/2**10
print(res)