data = '123AD'
sum2 = sum(map(lambda x:int(x,36),data))
sum3 = data.count('1')+data.count('2')*2+data.count('3')*3

from string import printable as alph
sum4=0
for i in range(37):
    sum+= data.count(alph[i])*i


sum5 = 0
for i in set(data):
    sum5 += data.count(i)*int(i,36)

sum6 = sum([ data.count(alph[i]) for i in range (37)])
print(sum6)

sum7 = sum([data.count(i)*int(i,36) for i in set(data)])
sum8 = sum(data.count(alph[i]) for i in range (37))
