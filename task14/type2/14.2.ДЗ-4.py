ans = set()

for x in range(10, 67):
    for y in range(x):
        n1 = 7 * 67**4 + 3 * 67**3 + x * 67**2 + 1 * 67**1 + y * 67**0
        n2 = 4 * x**3 + 9 * x**2 + y * x**1 + 6 * x**0
        n = n1+n2

        ans.add(n)

print(len(ans))
