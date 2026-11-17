from string import printable as alph
for p in range(16,37):
    n1 = int('17496',p)
    n2  = int('91f83',p)
    n3  = int('d9543',p)
    n = n1+n2+n3
    if n%12==0:
        print(n//12)
        break

