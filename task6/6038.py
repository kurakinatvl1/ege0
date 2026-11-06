from turtle import *
screensize(10000,10000)
tracer(0)
m =10

lt(90)
for i in range(6):
    fd(m*33)
    rt(90)
    fd(m*20)
    rt(90)

up()

fd(3*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(6):
    fd(m*24)
    rt(90)
    fd(m*25)
    rt(90)



for x in range(9,21):
    for y in range(3,28):
        teleport(x*m,y*m)
        dot(3,'red')
update()
done()
print(10*23)