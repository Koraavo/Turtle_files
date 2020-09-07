# Making of a small simple car
import turtle
import math


wn = turtle.Screen()

alex = turtle.Turtle()
lisa = turtle.Turtle()
lisa1 = turtle.Turtle()
fred = turtle.Turtle()
fred1 = turtle.Turtle()
bear = turtle.Turtle()
bear1 = turtle.Turtle()

alex.hideturtle()
lisa.hideturtle()
lisa1.hideturtle()
fred.hideturtle()
fred1.hideturtle()
bear.hideturtle()
bear1.hideturtle()

alex.fillcolor("blue")
alex.begin_fill()
for i in range(2):
    alex.forward(200)
    alex.left(90)
    alex.forward(50)
    alex.left(90)
alex.end_fill()


lisa.penup()
lisa.setpos(50, 50)
lisa.pendown()
lisa.forward(25)
lisa.left(90)
lisa.forward(25)
lisa.left(135)
lisa.forward(math.sqrt((25**2) + (25**2)))


lisa1.penup()
lisa1.setpos(150, 50)
lisa1.pendown()
lisa1.bk(25)
lisa1.left(90)
lisa1.forward(25)
lisa1.right(135)
lisa1.forward(math.sqrt((25**2) + (25**2)))


fred.penup()
fred.setpos(75,50)
fred.pendown()
for i in range(4):
    fred.forward(25)
    fred.left(90)


fred1.penup()
fred1.setpos(100,50)
fred1.pendown()
for i in range(4):
    fred1.forward(25)
    fred1.left(90)


bear.penup()
bear.setpos(60, -15)
bear.pendown()
bear.circle(15)


bear1.penup()
bear1.setpos(140, -15)
bear1.pendown()
bear1.circle(15)


wn.exitonclick()