import turtle
# draw a turtle clock

wn = turtle.Screen()
alex = turtle.Turtle()
jim = turtle.Turtle()
alex.shape("turtle")
alex.stamp()


for i in range(12):
    alex.penup()
    jim.penup()
    jim.forward(50)
    alex.forward(60)
    jim.stamp()
    alex.stamp()
    jim.forward(-50)
    alex.forward(-60)
    jim.right(30)
    alex.right(30)


wn.exitonclick()