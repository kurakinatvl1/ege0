num = 283**382 + 9**15 + 2**3
b = 0
c = 0
while num:
    if num % 14 == 11:
        b += 1
    elif num % 14 == 12:
        c += 1
    num //= 14
print(abs(b-c))