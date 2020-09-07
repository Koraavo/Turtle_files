import turtle
import math
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1, -1, 1, 1)

fred.up()
wn.tracer(100)

numdarts = 1000
insideCount = 0
for i in range(numdarts):
    # Generate random floating points within (-1, 1)
    # .uniform() allows a negative range, returns floating point ints.
    randx = random.uniform(-1, 1)
    # .random() * 2 = [0 ,2], -1 = [-1, 1]
    randy = random.random() * 2 - 1

    x = randx
    y = randy

    fred.goto(x, y)
    """
    We already know the total number of darts being thrown. 
    The variable numdarts keeps this for us. 
    What we need to figure out is how many darts land in the circle? 
    Since the circle is centered at (0,0) and it has a radius of 1, 
    the question is really simply a matter of checking to see 
    whether the dart has landed within 1 unit of the center. 
    Luckily, there is a turtle method called distance 
    that will return the distance from the turtle to any other position. 
    It needs the x,y for the other position.
    """
    if fred.distance(0, 0) <= 1.0:  # since the radius of the circle is 1
        # this would mean that it is on the circle
        fred.color("red")
        insideCount += 1
    else:
        fred.color("blue")
    fred.dot()  # creates all the random dots in red and blue

print("The number of darts landing on the board: ", insideCount / numdarts)
print("value of pi is: ", (insideCount / numdarts) * 4)

wn.exitonclick()
