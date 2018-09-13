import turtle
#turtle.position()
#(0.00, 240.00)
#turtle.setx(-50)
#turtle.sety(-50)
#turtle.position()
#(10.00, 240.00)
turtle.pd()
a = 1
b = 1
x = 4
turtle.left(-135)
for a in range(11):
    if b != 4:
        turtle.left(135)
        for b in range(4):
            turtle.pd()
            turtle.forward(a*10)
            turtle.left(90)
        turtle.pu()  
        turtle.left(-135)
        turtle.forward(x*2-1)
        



