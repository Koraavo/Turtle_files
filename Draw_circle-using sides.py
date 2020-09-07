import turtle

def drawPolygon(t, sideLength, numSides):
    # equilateral triangle has 3 sides therefore angle become 360/3
    turnAngle = 360 / numSides
    for i in range(numSides):
        # following the principle of drawing a square or a triangle
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    # circumference = 2*pi*r
    circumference = 2 * 3.1415 * radius
    # sidelength = assuming circle has 360 sides
    # perimeter of a square = 4*L
    # therefore l = perimeter / 4
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)


wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel, 20)

wn.exitonclick()
