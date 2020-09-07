import turtle
import random

def tree(branchLen,t, pensize):
    t.pensize(pensize)
    number = random.randint(5, 75)
    if branchLen > 5:

        pensize -= 0.5
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-number,t, pensize)
        t.left(40)
        tree(branchLen-number,t, pensize)
        t.right(20)
        t.backward(branchLen)



def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(1)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t, 4)

    myWin.exitonclick()

main()
