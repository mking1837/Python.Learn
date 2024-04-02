import time
import turtle

turtle.mode('logo')

h = turtle.Turtle()
h.color('red')
h.shape('arrow')
h.shapesize(1,10)

m = turtle.Turtle()
m.color('blue')
m.shape('arrow')
m.shapesize(1,14)


s=turtle.Turtle()
s.color('black')
s.shape('arrow')
s.shapesize(1,15)

def showhands():
    t = time.localtime()
    s.seth(t.tm_sec*6)
    m.seth(t.tm_min*6)
    h.seth(t.tm_hour*30 + t.tm_min*0.5)
    turtle.ontimer(showhands,1000)

def makeface():
    b= turtle.Turtle()
    b.speed(0)
    b.hideturtle()
    b.penup()
    b.dot(350)
    b.pencolor('white')
    b.dot(340)
    b.pencolor('black')
    for a in range(0,360,6):
        b.goto(0,0)
        b.seth(a)
        b.fd(160)
        b.dot(5)
    for a in range(0,360,30):
        b.goto(0,0)
        b.seth(a)
        b.fd(160)
        b.dot(10)

makeface()
showhands()
