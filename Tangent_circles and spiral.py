import turtle
# More than one circle having one point of intersection is called tangent circles.

wn = turtle.Screen()
tangentcircles = turtle.Turtle()
for i in range(10):
    tangentcircles.circle(10 * i)
# wn.exitonclick()


# Circles with varying radius are called spiral.

spiral_circle = turtle.Turtle()
spiral_circle.penup()
spiral_circle.setpos(-200, -200)
spiral_circle.pendown()
size = 10
for i in range(100):
    spiral_circle.circle(size + i, 45)
wn.exitonclick()
