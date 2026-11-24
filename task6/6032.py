from turtle import *
screensize(1000,1000)
tracer(0)
lt(90)
m = 10
for i in range(2):
    fd(m*3)
    rt(90)
    fd(m*20)
    rt(90)
up()
bk(8*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(2):
    fd(m*16)
    rt(90)
    fd(m*8)
    rt(90)
for x in range(9,18):
    for y in range(0,4):
        teleport(x*m,y*m)
        dot(3,'red')
print(21)
update()
done()