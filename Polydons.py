import turtle
import math
#радиус описанной окружности правильного многоугольника
turtle.speed(0)

def fas(n,i):
    ang = 360/n
    r = (i*ang)/(2*math.sin(math.radians(360)/(2*n)))
    turtle.circle(r)
    turtle.left(ang/2)
    fass(ang,n,r,i)

def fass(ang,n,r,l):
    for i in range(1,1+n,1):
        turtle.forward(ang*l)
        turtle.left(ang)
    turtle.setheading(0)
    turtle.pu()
    turtle.setpos(0,-r)
    turtle.pd()    
    
def mainn(n):
    for i in range(1,8,1):
        fas(n,i)
        n += 1
             
mainn(3)

 








 
