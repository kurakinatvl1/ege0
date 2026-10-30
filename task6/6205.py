from turtle import *
screensize(10000,10000)
tracer(0)
m =20

lt(90)
for i in range(5):
    fd(m*13)
    rt(90)
    fd(m*5)

up()

rt(90)
fd(10*m)
lt(90)
fd(7*m)
down()
for i in range(2):
    fd(m*8)
    rt(90)
    fd(m*11)
    rt(90)



for x in range(12,19):
    for y in range(-5,4):
        teleport(x*m,y*m)
        dot(3,'red')
update()
done()
print(18*18+8*11-6*8)