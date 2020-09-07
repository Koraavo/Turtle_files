# the bar for any value of 200 or more is filled with red,
# values between [100 and 200) are filled yellow,
# and bars representing values less than 100 are filled green.


import turtle


def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()  # start filling this shape
    t.left(90)
    t.forward(height)
    # t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()  # stop filling this shape


def fillColor(t, height):
    if height >= 200:
        t.fillcolor("red")
    elif height >= 100 and height < 200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    drawBar(t, height)


xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()  # Set up the window and its attributes
wn.setworldcoordinates(0 - border, 0 - border, 40 * numbars + border, maxheight + border)
# 0 - border is the x coordinate on the left,
# so width is basically 0-border to (40 * numbars + border) i.e 40*7 + 10,
# since each bar is 40-coordinates long + 10 spaces in the end for border
# and height is 0-border(2nd value) to maxheight of the bar, which is 260 + 10
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # create tess and set some attributes
tess.color("black")
tess.pensize(3)
alex = turtle.Turtle()
alex.pensize(3)
alex.color("black")
alex.hideturtle()

for a in xs:
    fillColor(tess, a)

for x in xs:
    alex.penup()
    alex.sety(x + 5)
    alex.write("       " + str(x), font=("Arial", 15, "bold"))
    alex.forward(40)
    alex.pendown()

wn.exitonclick()

