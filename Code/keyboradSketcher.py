import turtle

def drawUp():
    turtle.seth(90)
    turtle.fd(20)
def drawDown():
    turtle.seth(270)
    turtle.fd(20)
def drawLeft():
    turtle.seth(180)
    turtle.fd(20)
def drawRight():
    turtle.seth(0)
    turtle.fd(20)
def setRed():
    turtle.color('red')
def setGreen():
    turtle.color('green')
def setBlue():
    turtle.color('blue')
def setYellow():
    turtle.color('yellow')

turtle.onkey(drawUp,'Up')
turtle.onkey(drawDown,'Down')
turtle.onkey(drawLeft,'Left')
turtle.onkey(drawRight,'Right')

turtle.onkey(setRed,'r')
turtle.onkey(setGreen,'g')
turtle.onkey(setBlue,'b')
turtle.onkey(setYellow,'y')


turtle.listen()
