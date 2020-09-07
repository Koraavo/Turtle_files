import turtle
# drawing some other shapes


wn = turtle.Screen()
wn.tracer(8, 25)
alex = turtle.Turtle()
john = turtle.Turtle()


alex.penup()
alex.goto(-50, -50)
alex.pendown()
sz = 1
for i in range(50):
    alex.forward(sz)
    alex.right(90)
    sz += 2


john.penup()
john.goto(50, 50)
john.pendown()
sz = 1
for x in range(50):
    john.forward(sz)
    john.right(91)
    sz += 2


wn.exitonclick()

#----------------------EOL-----------------------------

# Write a program to draw this.
# Assume the innermost square is 20 units per side,
# and each successive square is 20 units bigger, per side, than the one inside it.


def drawSquare(t,size):
    for i in range(4):
        t.forward(size)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("lightpink")
size = 20
x = 0
y = 0
for i in range (5):
    drawSquare(alex, size)
    size += 20
    alex.penup()
    x = x-10
    y = y-10
    alex.goto(x, y)
    alex.pendown()


wn.exitonclick()

#----------------------EOL-----------------------------


def drawPoly(someturtle, sz):
    for i in range(4):
        someturtle.forward(sz)
        someturtle.left(90)


wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(25):
    drawPoly(alex, 50)
    alex.right(20)


wn.exitonclick()