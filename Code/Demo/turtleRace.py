import turtle
import random

a = turtle.Turtle()
a.color('red')

b = turtle.Turtle()
b.color('purple')

c = turtle.Turtle()
c.color('green')

turtle = [a,b,c]

for item in turtle:
    item.penup()
    item.shape('turtle')
    item.shapesize(4)


a.goto(-300,-100)
b.goto(-300,0)
c.goto(-300,100)

for race in range(100):
    for item in turtle:
        item.fd(random.randint(0,12))
