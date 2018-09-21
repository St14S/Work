import turtle
import math
#СМАЙЛИК
turtle.speed(7)

turtle.color("black", "yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.setheading(90)
turtle.pu()
turtle.color("black")
turtle.forward(90)
turtle.pensize(20)
turtle.pd()
turtle.forward(20)

x,y = turtle.pos()
s = 40
for i in range(1,3,1):
    turtle.pu()
    turtle.setpos(x-s,y+40)
    turtle.color("blue")
    turtle.pd()
    turtle.pensize(40)
    turtle.forward(1)
    s = (-s)

x,y = turtle.pos()
turtle.pu()
turtle.setpos(x+20,y-60)
turtle.color("red")
turtle.pensize(16)
turtle.pd()
turtle.circle(60,-180)






 
