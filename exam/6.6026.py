from turtle import *
screensize(10000,10000)
m = 6
tracer(0)
lt(90)
for i in range(8):
    fd(m*16)
    rt(90)
    fd(m*22)
    rt(90)
up()
fd(5*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(8):
    fd(m*52)
    rt(90)
    fd(m*77)
    rt(90)


for x in range(5,23):
    for y in range(5,17):
        teleport(x*m,y*m)
        dot(3,'red')
update()
done()
print(11*17)