import turtle
wn = turtle.Screen()

# Drawing triangle, square, hexagon, octagon
triangle = turtle.Turtle()
for t in range(3):
    triangle.forward(30)
    triangle.left(120)

square = turtle.Turtle()
square.color("green")
for s in range(4):
    square.forward(40)
    square.left(90)

hexagon = turtle.Turtle()
hexagon.color("blue")
for s in range(6):
    hexagon.forward(50)
    hexagon.left(60)

octagon = turtle.Turtle()
octagon.color("red")
octagon.penup()
octagon.backward(20)
octagon.pendown()
for s in range(8):
    octagon.forward(90)
    octagon.left(45)

# making a circle

wn = turtle.Screen()
circleT = turtle.Turtle()
circleT.penup()
circleT.setposition(-200, -200)
circleT.pendown()

circleT.circle(50, extent=None, steps=None)
circleT.circle(120, 180)  # half a circle


# Making a circle with sides

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)


def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    print("1. how one can come to this:\n"
          "2. perimeter is equivalent to circumference of the circle\n"
          "3. if a square has 4 sides, with each side being 40 cm\n"
          "4. perimeter = 4*40 = 160cm\n"
          "5. P = 4S\n"
          "6. or length of sides = Perimeter/4\n"
          "7. similarly: circle has a circumference\n"
          "8. C = 2*pi*r\n"
          "9. assuming the circle has 360 sides\n"
          "10. length of each side = circumference/360\n")

    drawPolygon(anyTurtle, sideLength, 360)



wheel = turtle.Turtle()

drawCircle(wheel, 20)

wn.exitonclick()