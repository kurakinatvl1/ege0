from turtle import *
screensize(10000,10000)
tracer(0)
lt(90)
m = 10
for i in range(2):
    fd(m*28)
    rt(90)
    fd(m*18)
    rt(90)
up()
fd(14*m)
rt(90)
fd(10*m)
lt(90)
down()
for i in range(2):
    fd(m*30)
    rt(90)
    fd(m*7)
    rt(90)
for x in range(10,18):
    for y in range(14,29):
        teleport(x*m,y*m)
        dot(3,'red')
print(29*19+8*31-8*15)
update()
done()