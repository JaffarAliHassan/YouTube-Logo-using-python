from turtle import *

screen = Screen()
screen.screensize(380, 400)
screen.setup(width = 380 + 4, height = 400 + 8)
t = Turtle()
t.shape("circle")
t.shapesize(0.5)
t.pensize(5)

t.color("#FF0000", "#FF0000")
t.begin_fill()
for x in range(2):
    t.fd(126)
    t.lt(90)
    t.fd(84)
    t.lt(90)
t.end_fill()

t.up()
t.fd(52)
t.lt(90)
t.fd(42)
t.down()

t.color("#FFFFFF", "#FFFFFF")
t.begin_fill()
t.fd(21)
t.rt(120)
t.fd(42)
t.rt(120)
t.fd(42)
t.rt(120)
t.fd(42)
t.end_fill()

t.up()
t.home()
t.lt(180)
t.fd(120)
t.down()

done()