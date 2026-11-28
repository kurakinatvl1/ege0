# def conv(num):
#     ans = ''
#     while num:
#         ans += num%8
#         num //=8
#     return ans[::-1]
# for n in range(1,10000):
#     r = conv(n)
#     cnt = sum(1 for i in r if i in '0246')
#     if cnt%2!=0:
#         r = r[-3:]+'46'
#     else:
#         osti = conv(n%8*5,8)
#         r = osti+r
#     if r==n:
#         print(n)
#         break
