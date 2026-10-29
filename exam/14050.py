
res = 0
for x in range(1,3001):
    number = 9 * (11 ** 210) + 8 * (11 ** 150)
    number = number-x

    n = 0
    for i in str(number):
        n += number%11
        number = number//11
    reversed(str(n))
    if str(n).count('0') == 60:
        res = max(x,res)
print(res)

