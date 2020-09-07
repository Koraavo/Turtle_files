"""
Rules A gets replaced by B and
B gets replaced by AB

A - 0
B - 1
AB - 2
BAB - 3
ABBAB - 4

"""


def Rules(lchr):
    rchr = ""
    if lchr == 'A':
        rchr = 'B'
    elif lchr == 'B':
        rchr = 'AB'
    else:
        rchr = lchr

    return rchr


def letsPlay(oldchr):
    newchr = ""
    for ch in oldchr:
        newchr = newchr + Rules(ch)  # concatenation as per rules

    return newchr


def createSystem(iter, axiom):
    start = axiom
    end = ""
    for x in range(iter):
        end = letsPlay(start)
        start = end
    return end


print(createSystem(4, 'A'))

print("\n")

import turtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-F'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        #elif cmd == 'B':
            #aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()

