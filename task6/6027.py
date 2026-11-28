from turtle import *
screensize(10000,10000)
tracer(0)
lt(90)
m = 10
for i in range(3):
    fd(m*27)
    rt(90)
    fd(m*12)
    rt(90)
up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in range(4):
    fd(m*83)
    rt(90)
    fd(m*77)
    rt(90)
for x in range(0,7):
    for y in range(0,24):
        teleport(x*m,y*m)
        dot(3,'red')
print(28*13+84*78-7*24)
update()
done()