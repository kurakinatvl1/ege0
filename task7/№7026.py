from math import ceil,log2
n = 8192
i = ceil(log2(n))
I = ceil(i*1024*960/8)
a = I*160*8/14680064
print(a)